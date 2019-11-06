import requests
import json
import datetime

def getBranchage(access_token,repourl,branchname):
	api_url = repourl+"/branches/"+branchname
	header = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(access_token)}
	response = requests.get(api_url, headers=header)
	if response.status_code == 200:
		branch= response.json() #
	else:
		print ("calculating the age of a branch for repositories",repourl,", return status code = ", response.status_code)
		branch=[]

	if len(branch) != 0:
		date = branch["commit"]["commit"]["committer"]["date"]
		d1 = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%Sz')
		d2 = datetime.datetime.strptime(datetime.datetime.today().strftime('%Y-%m-%dT%H:%M:%Sz'), '%Y-%m-%dT%H:%M:%Sz')
		return (d2-d1).days
	else:
		return 0


def getBranch(access_token,repourl):
	api_url = repourl+"/branches"
	header = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(access_token)}
	response = requests.get(api_url, headers=header)
	if response.status_code == 200:
		branchData= response.json()
	else:
		print (" unable to pull branch names for repositories",repourl,", return status code = ", response.status_code)
		branchData=[]

	branches=[]
	for i in range(len(branchData)):
		branch={}
		branch["branchName"]= branchData[i]["name"]
		branch["branchAge"]= getBranchage(access_token,repourl,branchData[i]["name"])
		branches.append(branch)

	return branches

def getCompleteBranchInfo(access_token,repourl):
	allBranch = getBranch(access_token,repourl)
	featureBranch=[]
	numberOfFreatureBranchOpen = 0
	for i in range(len(allBranch)):
		if(allBranch[i]["branchName"] != "master"):
			f={}
			f["fbranchName"] = allBranch[i]["branchName"]
			f["fbranchAge"] = allBranch[i]["branchAge"]
			numberOfFreatureBranchOpen = numberOfFreatureBranchOpen +1 
			featureBranch.append(f)

	output={}
	output["allBranch"] = allBranch
	output["featureBranch"] = featureBranch
	output["numberOfFreatureBranchOpen"] = numberOfFreatureBranchOpen
	return output






