#!/usr/bin/env python3
import json
import unittest
from pathlib import Path
from radar_relation_monitor import RelationMonitor, interval_intersects, run_case
ROOT=Path(__file__).parent
load=lambda name: json.loads((ROOT/name).read_text(encoding='utf8'))

class RadarReferenceRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a=run_case(load('CASE_A_SITE_RELATIONS.json'))
        cls.b=run_case(load('CASE_B_RIGHTS_RELATIONS.json'))
        cls.c=run_case(load('CASE_C_NEGATIVE_CONTROLS.json'))

    def test_a_overlap_raised(self):
        self.assertTrue(any(x['kind']=='POSSIBLE_ACCESS_TENSION' for x in self.a[1]['raised']))
    def test_a_original_permission_separate(self):
        self.assertTrue(any(x['kind']=='UNRESOLVED_PERMISSION' for x in self.a[2]['raised']))
    def test_a_demand_unknown_is_not_attendance_fact(self):
        self.assertTrue(any(x['kind']=='EVIDENCE_BOUNDARY' for x in self.a[3]['raised']))
    def test_a_budget_unknown_independently_preserved(self):
        self.assertTrue(any(x['kind']=='EVIDENCE_BOUNDARY' for x in self.a[4]['raised']))
    def test_a_E05_withdraws_only_temporal(self):
        r=self.a[5]
        self.assertEqual(1,len(r['withdrawn']))
        self.assertEqual('POSSIBLE_ACCESS_TENSION',r['withdrawn'][0]['kind'])
        self.assertEqual(3,len(r['active_signal_keys']))
    def test_a_E06_reactivates_temporal(self):
        self.assertEqual('POSSIBLE_ACCESS_TENSION',self.a[6]['raised'][0]['kind'])
    def test_a_repeat_draft_no_new_detection(self):
        self.assertTrue(self.a[7]['quiet'] is False) # source lineage changed (not novelty)
        self.assertEqual([],self.a[7]['raised'])
        self.assertEqual(1,len(self.a[7]['lineage_updated']))
    def test_b_permission_initial_alert(self):
        self.assertEqual('UNRESOLVED_PERMISSION',self.b[0]['raised'][0]['kind'])
    def test_b_customer_evidence_not_proved(self):
        self.assertEqual('EVIDENCE_BOUNDARY',self.b[1]['raised'][0]['kind'])
    def test_b_license_grant_withdraws_only_legal_signal(self):
        self.assertEqual('UNRESOLVED_PERMISSION',self.b[2]['withdrawn'][0]['kind'])
        self.assertEqual(1,len(self.b[2]['active_signal_keys']))
    def test_b_repeated_customer_weakness_not_novel(self):
        self.assertEqual([],self.b[3]['raised'])
        self.assertEqual(1,len(self.b[3]['lineage_updated']))
    def test_b_revocation_reissues(self):
        self.assertEqual('UNRESOLVED_PERMISSION',self.b[4]['raised'][0]['kind'])
    def test_b_regrant_retires_legal_signal(self):
        self.assertEqual('UNRESOLVED_PERMISSION',self.b[5]['withdrawn'][0]['kind'])
    def test_c_ignore_other_zone(self):
        self.assertTrue(self.c[1]['quiet'])
    def test_c_ignore_other_day(self):
        self.assertTrue(self.c[2]['quiet'])
    def test_c_real_overlap_then_cancel(self):
        self.assertEqual(1,len(self.c[3]['raised']))
        self.assertEqual(1,len(self.c[4]['withdrawn']))
    def test_c_repeat_irrelevant_is_quiet(self):
        self.assertTrue(self.c[5]['quiet'])
    def test_reject_duplicate_event_id(self):
        m=RelationMonitor('x'); e={'id':'x1','relation_key':'permission','kind':'permission','source_ref':'S','state':'PENDING'}
        m.push(e)
        with self.assertRaises(ValueError): m.push(e)
    def test_reject_implicit_overwrite(self):
        m=RelationMonitor('x');e={'id':'x1','relation_key':'permission','kind':'permission','source_ref':'S','state':'PENDING'}
        m.push(e)
        with self.assertRaises(ValueError): m.push({**e,'id':'x2'})
    def test_reject_wrong_replaces(self):
        m=RelationMonitor('x');e={'id':'x1','relation_key':'permission','kind':'permission','source_ref':'S','state':'PENDING'}
        m.push(e)
        with self.assertRaises(ValueError): m.push({**e,'id':'x2','replaces':'x999'})
    def test_endpoint_is_no_overlap(self):
        self.assertFalse(interval_intersects({'day':'Mon','start':'10:00','end':'11:00'}, {'day':'Mon','start':'11:00','end':'12:00'}))
    def test_invalid_time_interval(self):
        with self.assertRaises(ValueError): interval_intersects({'day':'Mon','start':'11:00','end':'10:00'}, {'day':'Mon','start':'11:00','end':'12:00'})
    def test_signal_without_authority(self):
        for result in self.a+self.b+self.c:
            for signal in result['raised']:
                self.assertEqual('NONE',signal['authority'])
                self.assertEqual('RELATION_WORTH_INSPECTING_NOT_TRUTH',signal['confidence'])

if __name__=='__main__': unittest.main(verbosity=2)
