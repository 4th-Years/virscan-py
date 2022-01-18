import core as u
import re
import time

meta = {
		'name': 'File Analyzer',
		'version': '0.0.1',
		'description': 'Analyzes file with several antivirus softwares.',
		'syntax': 'analyze_file -q <file id>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engine = getattr(u, util)
	value = engine.run(self, q)
	info = {
		'sha256': value['data']['attributes']['sha256'],
		'md5': value['data']['attributes']['md5'],
		'sha1': value['data']['attributes']['sha1']
	}
	data_attr = value['data']['attributes']
	data_results = data_attr['last_analysis_results']
	threat_label = data_attr['popular_threat_classification']

	time.sleep(5)
	self.output("File Info:")
	for each in info:
		self.list_output(f"{each}: {info[each]}")
	self.output("Stats:")
	for each in data_attr['last_analysis_stats']:
		self.list_output(f"{each}: {data_attr['last_analysis_stats'][each]}")
	self.output(f"Threat Labelled as: {threat_label['suggested_threat_label']}")
	self.output("AV Scan Results:")
	for each in data_results:
		av_result = data_results[each]['category']
		if not av_result == 'undetected' and not av_result == 'type-unsupported':
			self.list_output(f"{each}: {av_result}")
	
