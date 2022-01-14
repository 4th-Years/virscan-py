import core as u
import re

meta = {
		'name': 'Sigma Analyzer',
		'version': '0.0.1',
		'description': 'Sigma analyses run in sandbox generated sysmon logs.',
		'example': 'sigma_analyze -q <SHA256 file hash>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engine = getattr(u, util)
	value = engine.run(self, q)

	self.output("Rule Matches:")
	for each in value['data']['attributes']['rule_matches']:
		self.output(f"Rule Title: {each['rule_title']}")
		self.list_output(f"Rule Level: {each['rule_level']}\nMatch Context:\n{each['match_context']}")
	
	self.output("Severity Stats:")
	for each in value['data']['attributes']['severity_stats']:
		self.list_output(each)

