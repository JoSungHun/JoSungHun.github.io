import hashlib

for i in range(10000000, 99999999):
    find = str(i) + "salt_for_you"
    hashstr = hashlib.sha1(find.encode('utf-8'))
    # print("first find: " + find)
    # print("firsthash : " + hashstr.hexdigest())
    for z in range(500):
        hashstr = hashlib.sha1(hashstr.hexdigest().encode('utf-8'))
        # print("hash100 : " + hashstr.hexdigest())

    hash100 = hashstr.hexdigest()
    # print(hash100)
    if hash100 == "3f37be195d7eee5cd9bdff531b30305c6c8cca51":
        print("find!!!: " + find)
        exit()
