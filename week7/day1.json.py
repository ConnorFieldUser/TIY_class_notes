
import json

l = ["5", "joel", 3, 4]

string_list = str(l)

print(string_list)

json_list = json.dumps(l)
print(json_list)


print(json.dumps({"joel": 'codes'}))
