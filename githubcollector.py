import os
import json
import time
from prometheus_client import start_http_server, Metric, REGISTRY
from prometheus_client.core import GaugeMetricFamily,SummaryMetricFamily,CounterMetricFamily, REGISTRY


class GithubCollector(object):
  def collect(self):
    with open("data_file.json", 'r') as f:
      response = json.load(f)

    ofb = GaugeMetricFamily("OpenFeatureBranches", 'Number of feature branch added', labels=['repository'])
    wkt = GaugeMetricFamily("workingtrend", 'hisotry', labels=['repository'])
    branchAge = CounterMetricFamily("branchAge", 'Branch Age', labels=['repository','branchname'])
    allnonbranch = CounterMetricFamily("allnonbranch", 'Branch Age', labels=['repository','branchname'])
    projectsize = CounterMetricFamily("projectsize", 'line of code', labels=['repository','branchname'])
    #commitDoneToday = GaugeMetricFamily("Commitsperday", 'commit history per day', labels=['repository'])
    for i in range(len(response)):
      wkt.add_metric([response[i]["repositoryName"]],response[i]["commitsdoneToday"])
      yield wkt

      ofb.add_metric([response[i]["repositoryName"]],response[i]["openFeatureBranches"])
      yield ofb

      projectsize.add_metric([response[i]["repositoryName"],"Master"], response[i]["lineOfcode"])
      yield projectsize

      branches = response[i]['allBranch']
      for j in range(len(branches)):
        branchAge.add_metric([response[i]["repositoryName"],branches[j]["branchName"]], branches[j]["branchAge"])
        yield branchAge
      fbranches = response[i]['featureBranch']
      for k in range(len(fbranches)):
        allnonbranch.add_metric([response[i]["repositoryName"],fbranches[k]["fbranchName"]], fbranches[k]["fbranchAge"])
        yield allnonbranch

if __name__ == '__main__':
	start_http_server(int(8080))
	REGISTRY.register(GithubCollector())
	while True: time.sleep(600)


