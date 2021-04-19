import json

i = open("message.json")

data = json.load(i)

import pdb; pdb.set_trace()

for k in data:
	print(k)
	print("\n")
