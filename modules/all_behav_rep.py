import core as u
import re

meta = {
		'name': 'All Behaviour File Report',
		'version': '0.0.1',
		'description': 'Returns a summary with behavioural information about the file.',
		'syntax': 'all_behav_rep -q <SHA256 file hash>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engine = getattr(u, util)
	value = engine.run(self, q)
	
	for each in value['data']:
		self.output(each.replace('_', ' ').title()+':')
		for every in value['data'][each]:
			self.list_output(every)
			









