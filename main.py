import requests
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("Please run this script as administrator")
    exit()

url = "https://adobe.isdumb.one/list.txt"
response = requests.get(url)

host = []
try:
	if response.status_code == 200:
		print("Successfully downloaded the list")
		with open("list.txt", "w") as file:
			for line in response.text.split("\n"):
				if not line.startswith("#"):
					host.append(line)
	else:
		print("Failed to download the list from original, trying other mirror")
		url_mirror = ['https://fastly.jsdelivr.net/gh/ignaciocastro/a-dove-is-dumb@latest/list.txt','https://gcore.jsdelivr.net/gh/ignaciocastro/a-dove-is-dumb@latest/list.txt','https://quantil.jsdelivr.net/gh/ignaciocastro/a-dove-is-dumb@latest/list.txt','https://gh-proxy.com/https://raw.githubusercontent.com/ignaciocastro/a-dove-is-dumb/main/list.txt']
		for i in range(len(url_mirror)):
			response_mirror = requests.get(url_mirror)
			if response_mirror.status_code == 200:
				break
		if response_mirror.status_code == 200:
			print("Successfully downloaded the list from mirror")
			with open("list.txt", "w") as file:
				for line in response_mirror.text.split("\n"):
					if not line.startswith("#"):
						host.append(line)
except Exception as e:
	print(f"An error occurred: {e}")
	print("Exiting...")
	exit()

with open('C:\\Windows\\System32\\Drivers\\etc\\hosts', "r+") as f:
	content = f.read()
	for line in host:
		if line not in content:
			f.write("\n" + line)
