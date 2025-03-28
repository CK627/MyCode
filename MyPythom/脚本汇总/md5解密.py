import hashlib
def md5sum(str):
	a=hashlib.md5()
	a.update(str)
	return a.hexdigest()

print md5sum(raw_input('please string:'))

