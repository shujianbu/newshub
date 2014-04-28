import httplib2
h = httplib2.Http()
resp = h.request("http://www.google.com", 'HEAD')

status = int(resp[0]['status'])
if (status < 400):
	print 'exist!'
else:
	print 'deleted!'