from bs4 import BeautifulSoup
import re

def run(self, q):
	records = []
	send_records = {}
	try:
		self.info(f"Searching for report for {q}...")
		url_prod = f"https://dns-lookup.com/{q}"
		url_stage = f"http://localhost:9000/allbehaviourrep.json"
		res = self.request('GET',url=url_stage)
		data = res.json()
	except:
		self.error(f"Something went wrong. Please try again.")
	else:
		return data
