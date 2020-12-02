# %%
from urllib import request, parse

api = "https://www.kaggle.com/requests/CompetitionService/ListCompetitions"
request_payload = {
    "pageSize":50,
    "pageToken":"",
    "selector":{
        "competitionIds":[],
        "listOption":4,
        "hostSegmentIdFilter":0,
        "sortOption":0,
        "searchQuery":""
        }
        }
header = {
    "Host": "www.kaggle.com",
    "Origin": "https://kaggle.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0",
    "DNT":1}


