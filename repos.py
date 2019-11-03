import requests
import json
def getRepo(access_token):
	api_url = "https://github.cms.gov/api/v3/user/repos"
	header = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(access_token)}
	response = requests.get(api_url, headers=header)
	if response.status_code == 200:
		repositoriesData= response.json()
	else:
		print ("unable to pull the repositories name, status code return = ", response.status_code)
		repositoriesData=[]

	repositories=[]
	for i in range(len(repositoriesData)):
		repo={}
		repo["repoName"]= repositoriesData[i]["name"]
		repo["repoID"]= repositoriesData[i]["id"]
		repo["repoUrl"]= repositoriesData[i]["url"]
		repositories.append(repo)

	return repositories

