import sys
import random
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


github_repo = sys.argv[1]

repo_name = github_repo.split('/')[1]
github_url = 'https://github.com/'+ github_repo +'/network/members'
git_url = "https://github.com"

reponse = requests.get(github_url)
soup = BeautifulSoup(reponse.text, "lxml")

all_forked_repo = []
for anchor in soup.select('div.repo [href]'):
	if repo_name in anchor['href']:
		all_forked_repo.append(anchor['href'])
for get_commits_info in all_forked_repo:
	forked_repo = git_url+get_commits_info
	response_from_forked_repo = requests.get(forked_repo)
	soup = BeautifulSoup(response_from_forked_repo.text, "lxml")
	for read_commit_message in soup.select('div.branch-infobar'):
		commit_message = read_commit_message.text
		if "ahead" in commit_message:
			print "Repo Name is: " +forked_repo+commit_message.splitlines()[12]
