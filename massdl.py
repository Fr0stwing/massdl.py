import urllib.request

startNum = 1
stopNum = 10

while startNum < stopNum:
	try:
		# First arg: file location / Second arg: file name (with extension)
		urllib.request.urlretrieve("http://*.*/.gif?id="+str(startNum), str(startNum)+".gif")
	except Exception:
		print("File " + str(startNum) + " doesn't exist. - Moving on...")
		startNum += 1
	else:
		print("Saved file number " + str(startNum))
		startNum += 1