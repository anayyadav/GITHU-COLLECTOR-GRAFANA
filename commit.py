import requests
import json
import datetime

def getCommits(access_token,repourl):
	today = int(datetime.datetime.today().weekday())
	api_url = repourl+"/stats/punch_card"
	header = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(access_token)}
	response = requests.get(api_url, headers=header)
	if response.status_code == 200:
		commitData= response.json()
	else:
		print ("unable to pull commits for repositories",repourl,", return status code = ", response.status_code)
		commitData=[]

	commitsDoneToday=0
	for i in range(len(commitData)):
		if commitData[i][0] == today:
			commitsDoneToday = commitsDoneToday + commitData[i][2]

	return commitsDoneToday
