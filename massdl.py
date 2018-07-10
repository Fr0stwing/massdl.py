import urllib.request

i = 1
while i < 10:
	try:
		# First arg: file location / Second arg: file name (with extension)
		urllib.request.urlretrieve("http://*.*/.gif?id="+str(i), str(i)+".gif")
	except Exception:
		print("File " + str(i) + " doesn't exist. - Moving on...")
		i += 1
	else:
		print("Saved file number " + str(i))
		i += 1