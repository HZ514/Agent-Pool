from selenium import webdriver

from day6.get_agency_ip import get_ip
from day6.proxy_pool_helper import get_proxy

proxy = get_proxy()
# proxy = get_ip()

# proxy = '47.75.169.32:808'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')
