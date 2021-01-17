import requests
import json
import logging
import schedule
import time
import sys

logging.basicConfig(
	filename="server.log",
	filemode='a',
	level=logging.INFO,
	format='{levelname} {asctime} {name} : {message}',
	style='{'
)

log = logging.getLogger(__name__)


def main(url):
	try:
		r = requests.get(url)
		data = json.loads(r.content)
		
		logging.info('Сервер доступний. Час на сервері: %s', data['date'])
		logging.info("Запитувана сторінка: : %s", data['current_page'])
		logging.info("Відповідь сервера місти наступні поля:")
		for key in data.keys():
			logging.info("Ключ: %s, Значення: %s", key, data[key])
	except:		
		logging.error('Сервер не доступний.')
		# return 0
	


if __name__ == '__main__':
	if '--once' in sys.argv:
		main("http://docker.for.win.localhost:8000/health")		
		exit(0)	
	
	schedule.every(1).minutes.do(main,"http://docker.for.win.localhost:8000/health")
	while True:
		schedule.run_pending()
		time.sleep(1)
	
