import httplib2
h = httplib2.Http()
resp = h.request("http://forum.home.news.cn/detail/131973139/1.html", 'HEAD')

status = int(resp[0]['status'])
print status