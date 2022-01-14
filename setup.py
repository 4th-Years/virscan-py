from setuptools import setup, find_packages
import json

with open("config.json", "r") as config:
	configs = json.loads(config.read())

setup(
	name = configs['meta']['name'],
	version = configs['meta']['version'],
	url = configs['data']['source_link']
	creator = configs['meta']['author']
	description = configs['meta']['description'],
	content_type = "text/markdown",
	packages = find_packages()
	install_requires = ['requests']
	classifiers = [
	"Programming Language :: Python :: 3",
	'License :: OSI Approved :: not yet',
	'Operating System :: POSIX :: Linux',
	'Environment :: Console',
	],
	python_requires = '>=3.8',
)
