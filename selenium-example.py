import time, os, io
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pyvirtualdisplay import Display

def download(_url, _folder):
	resp = requests.get(_url)
	if resp.status_code == 200:
		tempStorage = io.BytesIO()
		for block in resp.iter_content(1024):
			tempStorage.write(block)

		name = os.path.basename(_url)
		with open(os.path.join(_folder, name), 'wb') as f:
			f.write(tempStorage.getvalue())
		return True
	else:
		print(resp.status_code)
		return False
	pass

def main():
	URL = 'http://chromedriver.storage.googleapis.com/index.html?path=73.0.3683.68/'
	br = webdriver.Chrome()
	br.get(URL)

	try:
		link = WebDriverWait(br, 10).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'mac')))
		download(link.get_attribute('href'), "./")
	except Exception as e:
		raise e
	finally:
		br.quit()
	pass

if __name__ == '__main__':
	# display = Display(visible=0, size=(1366, 768))
	# display.start()
	main()
	# display.stop()
