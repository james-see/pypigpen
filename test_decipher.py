import json

def get_file(filename):
	with open(filename) as f:
		jsondict = json.loads(f.read())
	return jsondict

def test_answer():
	dictt = get_file('jsondata.json')
	assert ''.join(dictt['a']) == '_|'
