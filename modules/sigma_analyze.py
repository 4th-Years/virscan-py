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
	for each in value:
		self.output(each)
		headers = (' '*10).join(value[each][0])
		self.list_output(headers.ljust(20))
		for entries in value[each][1]:
			elements = ''
			for x in entries.contents:
				if not x == '\n':
					elements += x.string + '\t'
			self.list_output(elements.ljust(20))
