import requests

url = "https://192.168.222.3/era/v0.9/databases/name/migra"


headers = {
	'Content-Type': "application/json",
	'Authorization': "Basic YWRtaW46QUhWNGV2ZXIv"
}

requests.packages.urllib3.disable_warnings()
response = requests.request("GET", url, headers=headers, verify=False)

print(response.status_code)
print(response.text)
