from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import string
import sys
import time


domain = sys.argv[1]
driver = webdriver.Chrome()
driver.get("http://bgp.he.net/")
driver.find_element_by_id('search_search').send_keys(domain)
driver.find_element_by_name("commit").click()
time.sleep(2)
response = driver.page_source
soup = BeautifulSoup(response, "lxml")
all_asn=[]
all_ip = []
for find_asn in soup.select('td a[href]'):
	if 'AS' in find_asn.string:
		all_asn+=find_asn.string.split()
	else:
		all_ip += find_asn.string.split()
for asn in all_asn:
	driver.get("http://bgp.he.net/"+asn)
	response = driver.page_source
	soup = BeautifulSoup(response, "lxml")
	for link in soup.select('td.nowrap a'):
		all_ip += link.text.split()

print all_ip
driver.quit()
