import re

def run(self, q):
	records = []
	send_records = {}
	try:
		self.info(f"Analysing using sigma rules on {q}...")
		url_prod = f"https://www.virustotal.com/api/v3/sigma_analyses/{q}"
		url_stage = f"http://localhost:9000/sigmaanalysis.json"
		res = self.request('GET',url=url_stage)
		data = res.json()
	except:
		self.error(f"Something went wrong. Please try again.")
	else:
		return data
