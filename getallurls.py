from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


path_to_chromedriver = 'C:/Users/Suggu/Downloads/chromedriver_win32/chromedriver'
#list_of_indexes = ['A', 'AA', 'AAF', 'AAO', 'AAX', 'ABM', 'AC' 'ACE', 'ACM', 'ACS', 'AD', 'ADH', 'ADS', 'AE', 'AES', 'AFE', 'AFO', 'AFW', 'AGR', 'AHP', 'AID', 'AIP', 'AJ', 'AK', 'AL', 'ALM', 'AM', 'AMI', 'AMS', 'AN', 'ANM', 'AO', 'AP', 'APG', 'APP', 'AQ', 'ARE', 'ARP', 'AS', 'ASD', 'ASM', 'AST', 'AT', 'ATL', 'AU', 'AV', 'AW', 'AX']
list_of_indexes =['A','AA','B','BA']
all_urls = []
for index in list_of_indexes:
	browser = webdriver.Chrome(executable_path = path_to_chromedriver)
	url = 'http://www.acronymfinder.com/Index-%s.html'%index
	browser.get(url)
	urls = browser.find_elements_by_css_selector("table.acidx tr td a")
	for url in urls:
		print url.get_attribute('href')
		all_urls.append(url.get_attribute('href'))
print all_urls
print len(all_urls)
df = pd.DataFrame(all_urls)
df.to_csv('allurls.csv',encoding="UTF-8")
