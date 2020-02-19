import base64

id = b"admin"
pw = b"nimda"
for i in range(20):
    id = base64.b64encode(id)
    pw = base64.b64encode(pw)

id = id.decode("utf-8")
pw = pw.decode("utf-8")

id = id.replace("1", "!")
id = id.replace("2", "@")
id = id.replace("3", "$")
id = id.replace("4", "^")
id = id.replace("5", "&")
id = id.replace("6", "*")
id = id.replace("7", "(")
id = id.replace("8", ")")

pw = pw.replace("1", "!")
pw = pw.replace("2", "@")
pw = pw.replace("3", "$")
pw = pw.replace("4", "^")
pw = pw.replace("5", "&")
pw = pw.replace("6", "*")
pw = pw.replace("7", "(")
pw = pw.replace("8", ")")

print(id)
print("----------------------------")
print(pw)