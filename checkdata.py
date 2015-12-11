import json,httplib,urllib
connection = httplib.HTTPSConnection('api.parse.com', 443)
#params = urllib.urlencode({"where":"1"})
connection.connect()
connection.request('GET', '1/classes/', '', {
    "X-Parse-Application-Id": "QrNi3zPI91mQq60eFZBsdNrB9LpuTfMB8MPhTJ0n",
    "X-Parse-REST-API-Key": "N9Ix3DMj34l06b1FTPuwtScWQ2nSt6Q5TAVGsbcv"
    })
result = json.loads(connection.getresponse().read())
for m in result:
    print result

#print result
print "COMPLETE"
