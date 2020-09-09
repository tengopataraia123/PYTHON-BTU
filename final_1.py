import json
file = open("sample.json","r")



j = json.load(file)




print(j["quiz"]["maths"]["q2"]["question"])
print(j["quiz"]["maths"]["q2"]["options"])


