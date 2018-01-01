from urllib import request
if __name__ == "__main__":
	req=request.Request("http://fanyi.baidu.com")
	response=request.urlopen(req)
	print ('geturl %s' %(response.geturl()))
	print ('info %s'%(response.info()))
	print ('getcode %s' %(response.getcode()))

