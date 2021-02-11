import requests

url = 'https://www.kaggle.com/requests/CompetitionService/GetCompetition'
headers = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0','Cookie': 'CSRF-TOKEN=CfDJ8LdUzqlsSWBPr4Ce3rb9VL9BwMerSZbdeS-YkYaeOEBeUfbKRXRxflE_bHyjXksJKd60HfotT5jeTxYRtRmSCPX16IS7HnW58TnWfe2_uBh5Cu_7LaUHYYxiQzlhckEl-FroFrFkNyHiiyUA84cI2os; XSRF-TOKEN=CfDJ8LdUzqlsSWBPr4Ce3rb9VL888xXxFweg_xqS6dSns3r8nNj0LPB9QjXFIfKUNdE3lYHdVlibq-9BpcliLbw46rINakSArOsmVczgHU_JKKRC6MT34ZEdEFQooQyBmlKRCqjf5t9PFVK-bScDMaUVjk4; CLIENT-TOKEN=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOm51bGwsIm5idCI6IjIwMjEtMDItMTFUMDc6NDE6MjEuOTE4MTkyMVoiLCJpYXQiOiIyMDIxLTAyLTE…SZW5hbWUiLCJEYXRhc2V0c0Zyb21HY3MiLCJUUFVDb21taXRTY2hlZHVsaW5nIl0sInBpZCI6ImthZ2dsZS0xNjE2MDciLCJzdmMiOiJ3ZWItZmUiLCJzZGFrIjoiQUl6YVN5REFOR1hGSHRTSVZjNTFNSWRHd2c0bVFGZ20zb05yS29vIiwiYmxkIjoiNmQxOGRlZjMyYzQ3OWVkZWQxYTliYzdhYWM5Mzc2NmE5MDk4MDBhNCJ9.; GCLB=CPnV8sO7nO_8vwE; .AspNetCore.Mvc.CookieTempDataProvider=CfDJ8LdUzqlsSWBPr4Ce3rb9VL_6F9uq6qZHKzB3Qyst8hzWlkGQv05MACJNZJIUOV90MQdp8ogpHbqatd24rxFtnzzVjzszdaQ-xdIi0ygzFnZpiFiz2IkyStGyCCyxyoNAd7mxvxiIU_GZiQyxHkbvYKM; ka_sessionid=c5ae1ce9df6eebcaef9075ed996b8510,ka_sessionid=c85c6cab1197508a32ec73ba8e4daa77; GCLB=CM3h2aKO-uGEGA','x-xsrf-token': 'CfDJ8LdUzqlsSWBPr4Ce3rb9VL888xXxFweg_xqS6dSns3r8nNj0LPB9QjXFIfKUNdE3lYHdVlibq-9BpcliLbw46rINakSArOsmVczgHU_JKKRC6MT34ZEdEFQooQyBmlKRCqjf5t9PFVK-bScDMaUVjk4'}
body = """{
  "competitionId": 6675,
  "competitionName": ""
}"""

req = requests.post(url, headers=headers, data=body)

print(req.status_code)
print(req.headers)
print(req.text)
