import hashlib

for i in range(10000000, 99999999):
    find = str(i) + "salt_for_you"
    hashstr = hashlib.sha1(find.encode('utf-8'))
    # print("first find: " + find)
    # print("firsthash : " + hashstr.hexdigest())
    for z in range(99):
        hashstr = hashlib.sha1(hashstr.hexdigest().encode('utf-8'))
        # print("hash100 : " + hashstr.hexdigest())

    hash100 = hashstr.hexdigest()
    # print(hash100)
    if hash100 == "3c66ea536ef70934f4af883d8f2098255d59f3f9":
        print("find!!!: " + find)
        exit()