from pymd5 import md5, padding

m = "Use HMAC, not MD5"
x = "good advice"
h = md5()
h.update(m)

#Calculate the padding and final message length for the message m
digest = h.hexdigest()
cnt = (len(m) + len(padding(len(m)*8)))*8

#Set hash state md5 to the point at which md5(m) is computed
h = md5(state = digest.decode("hex"), count = cnt)

#Update md5 object to the existing hash to compute the new hash.
h.update(x)

#Now check if this matches with our length extension attack hash computation.
a = md5()
a.update(m + padding(len(m)*8) + x)

print h.hexdigest(), a.hexdigest()
if h.hexdigest() == a.hexdigest():
	print "MD5 length extension attack successful"

