import requests
import time
#						change url to your website
request = requests.get('https://www.google.com')
if request.status_code == 200:
	print('Website is up')
else:
	print('Website is down')
	#to check if there was a false alarm
	time.sleep(15)
	if request.status_code != 200:
		print('Website is still down')
	else:
		print('Website is up')