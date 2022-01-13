from bs4 import BeautifulSoup
import re

def run(self, q):
	records = []
	send_records = {}
	try:
		self.info(f"file upload: Uploading ...")
		url_prod = f"https://dns-lookup.com/{q}"
		url_stage = "http://localhost:9000/fileupload.json"
		res = self.request('GET',url=url_stage)
		data = res.json()
	except:
		self.error(f"file upload: Something went wrong. Please try again.")
	else:
#		print(data)
		return data
