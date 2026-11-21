#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SAC Translation Structure/Tension Checker
TOY / APPLIED SAC INSTRUMENT

Modes:
  prompt SOURCE.txt TARGET.txt
  score assessment.json
  run SOURCE.txt TARGET.txt
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path
from typing import Any, Dict

STRUCTURE_FIELDS = ("causality", "agent", "action", "tension_structure")
TENSION_FIELDS = ("causal_gap", "agent_ambiguity", "action_open", "semantic_conflict")

# Toy-local thresholds. Not SAC theory claims.
STRUCTURE_HIGH = 9
TENSION_HIGH = 6


def read_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def clamp_int(value: Any, low: int, high: int, field: str) -> int:
    try:
        n = int(value)
    except Exception as exc:
        raise ValueError(f"{field} must be an integer") from exc
    if not low <= n <= high:
        raise ValueError(f"{field} must be between {low} and {high}")
    return n


def normalize_assessment(data: Dict[str, Any]) -> Dict[str, Any]:
    structure = data.get("structure") or {}
    tension = data.get("tension") or {}

    normalized_structure = {
        key: clamp_int(structure.get(key), 0, 3, f"structure.{key}")
        for key in STRUCTURE_FIELDS
    }
    normalized_tension = {
        key: clamp_int(tension.get(key), 0, 2, f"tension.{key}")
        for key in TENSION_FIELDS
    }

    distortions = data.get("distortions") or []
    notes = data.get("notes") or []

    if not isinstance(distortions, list):
        raise ValueError("distortions must be a list")
    if not isinstance(notes, list):
        raise ValueError("notes must be a list")

    return {
        "structure": normalized_structure,
        "tension": normalized_tension,
        "distortions": [str(x) for x in distortions],
        "notes": [str(x) for x in notes],
    }


def verdict(data: Dict[str, Any]) -> Dict[str, Any]:
    a = normalize_assessment(data)

    structure_score = sum(a["structure"].values())
    tension_score = sum(a["tension"].values())

    structure_high = structure_score >= STRUCTURE_HIGH
    tension_high = tension_score >= TENSION_HIGH

    if structure_high and tension_high:
        label = "PRESERVED"
        zh = "結構與張力大致存活"
    elif structure_high and not tension_high:
        label = "STRUCTURE_OK_TENSION_LOST"
        zh = "骨架大致正確，但張力被翻順／補掉"
    elif not structure_high and tension_high:
        label = "STRUCTURE_BROKEN_TENSION_ALIVE"
        zh = "仍有張力，但結構已明顯漂移"
    else:
        label = "COLLAPSED"
        zh = "結構與張力都明顯崩壞"

    return {
        **a,
        "scores": {
            "structure": {
                "score": structure_score,
                "max": 12,
                "threshold_high": STRUCTURE_HIGH,
            },
            "tension": {
                "score": tension_score,
                "max": 8,
                "threshold_high": TENSION_HIGH,
            },
        },
        "verdict": {"label": label, "zh": zh},
        "standing": "TOY_OUTPUT_NOT_GROUND_TRUTH",
    }


def build_prompt(source: str, target: str) -> str:
    schema = {
        "structure": {
            "causality": 0,
            "agent": 0,
            "action": 0,
            "tension_structure": 0,
        },
        "tension": {
            "causal_gap": 0,
            "agent_ambiguity": 0,
            "action_open": 0,
            "semantic_conflict": 0,
        },
        "distortions": [],
        "notes": [],
    }

    return f"""You are auditing structural survival under translation/rewrite.

Do NOT judge fluency, beauty, politeness, or preference.
Compare SOURCE against TARGET.

A. STRUCTURE (0-3 each; toy-local rubric)
3 = preserved
2 = minor drift
1 = major drift
0 = broken

- causality: causal relations preserved without invention/deletion
- agent: actors/subjects/agency relations preserved
- action: actions, incompletion, event relations preserved
- tension_structure: structural tensions/gaps/conflicts preserved as structure

B. TENSION (0-2 each; source rubric)
2 = original unresolved structure preserved
1 = partially narrowed/weakened
0 = completed/rationalized/eliminated

- causal_gap: unexplained causality remains unexplained
- agent_ambiguity: source ambiguity remains ambiguous
- action_open: incomplete/open action remains open
- semantic_conflict: contradiction remains unresolved

Typical distortions:
causal_completion, agent_stabilization, action_completion,
semantic_rationalization, smoothening, structural_drift,
language_constraint_loss

Rules:
- Do not reward making text easier to understand.
- Added explanation may be distortion.
- Do not punish surface difference when relation structure survives.
- Distinguish model distortion from unavoidable language constraint when possible.
- Return JSON only, matching this schema:
{json.dumps(schema, ensure_ascii=False, indent=2)}

SOURCE:
---BEGIN SOURCE---
{source}
---END SOURCE---

TARGET:
---BEGIN TARGET---
{target}
---END TARGET---
"""


def extract_json(text: str) -> Dict[str, Any]:
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
        if text.lower().startswith("json"):
            text = text[4:].lstrip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start:end + 1])
        raise


def call_openai_compatible(prompt: str) -> Dict[str, Any]:
    url = os.getenv("LLM_API_URL")
    key = os.getenv("LLM_API_KEY")
    model = os.getenv("LLM_MODEL")

    if not url or not model:
        raise RuntimeError(
            "LLM_API_URL and LLM_MODEL are required for run mode. "
            "LLM_API_KEY is optional."
        )

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Return only the requested JSON."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0,
    }

    headers = {"Content-Type": "application/json"}
    if key:
        headers["Authorization"] = f"Bearer {key}"

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc

    content = body["choices"][0]["message"]["content"]
    return extract_json(content)


def usage() -> None:
    print(
        "Usage:\n"
        "  python checker.py prompt SOURCE.txt TARGET.txt\n"
        "  python checker.py score assessment.json\n"
        "  python checker.py run SOURCE.txt TARGET.txt"
    )


def main() -> int:
    if len(sys.argv) < 3:
        usage()
        return 2

    mode = sys.argv[1].lower()

    try:
        if mode == "prompt" and len(sys.argv) == 4:
            print(build_prompt(read_text(sys.argv[2]), read_text(sys.argv[3])))
            return 0

        if mode == "score" and len(sys.argv) == 3:
            print(json.dumps(verdict(json.loads(read_text(sys.argv[2]))),
                             ensure_ascii=False, indent=2))
            return 0

        if mode == "run" and len(sys.argv) == 4:
            prompt = build_prompt(read_text(sys.argv[2]), read_text(sys.argv[3]))
            print(json.dumps(verdict(call_openai_compatible(prompt)),
                             ensure_ascii=False, indent=2))
            return 0

        usage()
        return 2

    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
