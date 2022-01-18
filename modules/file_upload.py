import core as u
import re
import time

meta = {
		'name': 'File Uploader',
		'version': '0.0.1',
		'description': 'Upload file to get a file hash for further scanning.',
		'example': 'file_upload -q <file path>'
}

def options(self):
	for each in meta:
		self.output(f"{each}:\t{meta[each]}")


def mod_run(self, util, q):
	engine = getattr(u, util)
	value = engine.run(self, q)
	time.sleep(5)
	self.output(f"File Uploaded Successfully!\nFile Analysis id: {value['data']['id']}")

