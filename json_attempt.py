import json
import urllib.request
address="0xf3918988eb3ce66527e2a1a4d42c303915ce28ce"
urlData = "https://api-moonbeam.moonscan.io/api?module=account&action=balance&address="+address+"&apikey=YourApiKeyToken"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
Json_data=json.loads(data.decode(encoding))
print(Json_data)
print(Json_data.get('result'))
