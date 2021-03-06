import requests

PROXY_POOL_URL = 'http://127.0.0.1:5555/random'

def get_proxy():
	try:
		response = requests.get(PROXY_POOL_URL)
		if response.status_code == 200:
			return response.text
	except ConnectionError:
		return None


if __name__ == '__main__':
	print(get_proxy())