import httplib2
h = httplib2.Http()
resp = h.request("http://auto.caijing.com.cn/2014-04-28/114137376.html", 'HEAD')

status = int(resp[0]['status'])
print status