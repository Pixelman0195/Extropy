import requests
import keyring as kr
from map import save_db, load_db, db_content_name
from time import sleep
db=load_db(db_content_name)

def report_ip(ip,categs,comment,times,key):
	url = 'https://api.abuseipdb.com/api/v2/report'
	params = {
		'ip':ip,
		'categories':categs,
		'comment':comment,
		'timestamp':times
	}
	headers = {
		'Accept': 'application/json',
		'Key': key
	}

	try:
		response = requests.request(method='POST', url=url, headers=headers, params=params)
		if response.status_code == 200:
			print(f"[+] Reported {ip} | Categories: {categs}")
			return True
		else:
			print(f"[-] Error for {ip}: {response.status_code} - {response.text}")
			return False
	except Exception as e:
		print(f"[-] Exception when reporting - {ip}: {e}")
		return False

def main():
	key=kr.get_password('AbuseIPDB','extropy')
	if not key:
		print('[-] Error while getting your API key! Did you configure it first?')
		return
	'''while len(key)<5:
		key=input("Please enter your AbuseIPDB API key: ")
		if len(key)<5:
			print("[-] Error: Invalid Key")'''
	for ip in db:
		if not db[ip].get('reported',False):
			data=db[ip]
			timestamp=data['timestamp']
			categs="22"
			comment = f'{timestamp} SSH '
			creds=len(data['credentials'])
			hassh=1 if data['hassh']!='' else 0
			client_version=1 if data['client_version']!='' else 0
			commands=data['commands']
			tmp=False
			for command in commands:
				if 'busybox' in command or 'armv7l' in command:
					categs+=",23"
					tmp=True
					comment+='IoT targeting '
					break
			if creds>0:
				categs+=",18"
				tmp=True
				comment+="brute-force attack on port 22 blocked by "
			elif creds==0 and hassh+client_version>0:
				categs+=",14"
				tmp=True
				comment+="port scanning blocked by "
			comment+="Cowrie Honeypot"
			if tmp:
				res=report_ip(ip, categs, comment,timestamp,key)
				db[ip]['reported']=res
			sleep(1)
	save_db(db,db_content_name)

if __name__ == '__main__':
	main()