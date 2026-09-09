import requests
from time import sleep
from map import save_db, load_db
db_name = "hacker_profile.json"
shodan_db="shodan_data.json"

try:
	db = load_db(db_name)
except Exception as e:
	print(f"Error loading the external database: {e}")
	exit()
try:
	shodan_data = load_db(shodan_db)
except Exception as e:
	print(f"Error loading the shodan database file: {e}")
	exit()

def get_ips():
	vip_ips=[]
	for ip, data in db.items():
		commands=len(data['commands'])
		passwds=len(data['credentials'])
		if ip not in shodan_data and (commands>0 or passwds>0):
			vip_ips.append(ip)
	return vip_ips

def enrich(vip_ips):
	for ip in vip_ips:
		shodan_data[ip] = {}
		try:
			response=requests.get(f"https://internetdb.shodan.io/{ip}")
			if response.status_code == 200:
				sleep(1)
				new_query=response.json()
				shodan_data[ip].update(new_query)
			else:
				print(f"Error in web request (InternetDB failed request): {response}")
				shodan_data[ip]["InternetDB Error"] = f"Failed with code: {response.status_code}"
		except Exception as e:
			print(f"Exception for {ip}: {e}")
			shodan_data[ip]["InternetDB Error"]=f"Exception: {e}"
		try:
			sleep(1)
			l=['status','message','country','city','lat','lon','isp','org','as','reverse','mobile','proxy','hosting']
			fields=",".join(l)
			response=requests.get(f"http://ip-api.com/json/{ip}?fields={fields}")
			response=response.json()
			if response['status']=='fail':
				print(f"IP-API error for {ip}: {response['message']}")
				shodan_data[ip]["IP-API Error"]=f"Failed with message: {response['message']}"
			else:
				for field in l[2::]:
					data=response.get(field,'Unknown')
					if field=='as' and data!='Unknown':
						data=data.split()[0]
					shodan_data[ip][field]=data
		except Exception as e:
			print(f"Error in web request (IP-API failed request): {e}")
			shodan_data[ip]["IP-API Error"]=f"Exception: {e}"
def main():
	vip_ips = get_ips()
	enrich(vip_ips)
	save_db(shodan_data,shodan_db)
if __name__ == '__main__':
	main()
