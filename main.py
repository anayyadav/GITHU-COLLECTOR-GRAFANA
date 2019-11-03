import requests
import os
import json
import branch
import commit
import content
import repos
import time
#curl -H "Authorization: token a9c2fc9e74b8fdf5b61c28393eaee431af3f2c07" https://github.cms.gov/api/v3/repos
#/repos/:owner/:repo/stats/commit_activity

def getData(access_token):
	current_user_repos = repos.getRepo(access_token)
	finalOutput=[]
	timestamp = time.time()
	for i in range(len(current_user_repos)):
		final={}
		final["repositoryName"] = current_user_repos[i]["repoName"]
		print ("Collecting the data for repository : - ",current_user_repos[i]["repoName"])
		final["repositoryID"] = current_user_repos[i]["repoID"]
		branchOutput = branch.getCompleteBranchInfo(access_token,current_user_repos[i]["repoUrl"])
		final["allBranch"] = branchOutput["allBranch"]
		final["featureBranch"] = branchOutput["featureBranch"]
		final["openFeatureBranches"] = branchOutput["numberOfFreatureBranchOpen"]
		final["lineOfcode"] = content.getSizeofRepo(access_token,current_user_repos[i]["repoUrl"])
		final["commitsdoneToday"] = commit.getCommits(access_token,current_user_repos[i]["repoUrl"])
		finalOutput.append(final)

	return finalOutput


def main():
	access_token = os.environ.get('ACCESS_TOKEN', 'default')
	data = getData(access_token)
	with open("data_file.json", "w") as write_file:
		json.dump(data, write_file)

if __name__ == '__main__':
	main()

