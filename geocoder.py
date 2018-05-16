# TSH00

def callBaiduGeocoderAPI(address):
	params = {
		'city':'上海市',
		'address':address,
		'output':'json',
		'ret_coordtype':'gcj02ll',
		#'ak':'gBoRjgnsDen72Gmj9l2SkXUwVyOu1AFQ'
		'ak':'TgzQWTwQh3FLuOYXOHr1l1qQ9jvM2Pq7'
	}

	# create the query
	queryStr = '/geocoder/v2/?' + '&'.join([k+'='+v for k,v in params.iteritems()])
	 
	# make it safe and encoded
	encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
	 
	# add the sk to create the sn
	# rawStr = encodedStr + '8Qg9v9RNlzepKHYlWv9Ya7d9O9Pl3Gxy'
	rawStr = encodedStr + 'MwrPsuE1dD5OtLkmhiLYrIRL71BXs1I4'
	# create the sn and add it to the query line 
	sn = hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()
	query = 'http://api.map.baidu.com' + queryStr + '&sn=' + sn

	result = requests.get(query)
	resultJson = result.json()
	
	try:
		lat = resultJson['result']['location']['lat']
		lon = resultJson['result']['location']['lng']
	except Exception, e:
		if 'msg' in resultJson:
	 		print resultJson['msg'].encode('utf-8')
	 	else:
	 		print 'reached api limit', resultJson['message'].encode('utf-8')
	 		exit()
		return None, None
	latitude, longitude = gcj02_decrypt(lat, lon)
	return latitude, longitude
