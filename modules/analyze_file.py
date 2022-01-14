import core as u
import re

meta = {
		'name': 'File Analyzer',
		'version': '0.0.1',
		'description': 'Analyzes file with several antivirus softwares.',
		'syntax': 'dns_record -q <SHA256 file hash>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engine = getattr(u, util)
	value = engine.run(self, q)
	info = value['meta']['file_info']
	data_attr = value['data']['attributes']
	data_results = value['data']['attributes']['results']
	
	self.output("File Info:")
	for each in info:
		self.list_output(f"{each}: {info[each]}")
	self.output("Stats:")
	for each in data_attr['stats']:
		self.list_output(f"{each}: {data_attr['stats'][each]}")
	self.output("AV Scan Results:")
	for each in data_results:
		self.list_output(f"{each}: {data_results[each]['category']}")
	
