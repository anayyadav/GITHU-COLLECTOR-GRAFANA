import requests
import json

def getSizeofRepo(access_token,repourl):
	api_url = repourl+"/contents"
	header = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(access_token)}
	response = requests.get(api_url, headers=header)
	if response.status_code == 200:
		repoData= response.json()
	else:
		print ("unable to pull line of code details for repositories",repourl,", return status code = ", response.status_code)
		repoData=[]

	sizeofRepo = 0
	for i in range(len(repoData)):
		sizeofRepo = sizeofRepo + repoData[i]["size"]

	return sizeofRepo
