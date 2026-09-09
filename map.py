import json
import requests
import folium
from folium.plugins import MarkerCluster
import os
import time
from pathlib import Path
db_ip_name = "attack_data.json"
db_content_name = "hacker_profile.json"
directory = Path('var/log/cowrie')
LOG_FILE="var/log/cowrie/cowrie.json"
LOG_FILES = ["var/log/cowrie/"+f.name for f in directory.glob('*.json*')]
def load_db(db_name):
	if os.path.exists(db_name):
		with open(db_name, 'r', encoding='utf-8') as file:
			return json.load(file)
	return {}


def save_db(db_data, db_name):
	with open(db_name, 'w', encoding='utf-8') as file:
		json.dump(db_data, file, indent=4)


def get_ips(db):
	print("Scanning the logs for new IP addresses...")
	ips = set()
	try:
		with open(LOG_FILE, 'r') as f:
			for line in f:
				try:
					data = json.loads(line)
					ip = data.get('src_ip')
					if ip and ip != "127.0.0.1" and ip not in db:
						ips.add(ip)
				except json.JSONDecodeError:
					pass
		return ips
	except FileNotFoundError:
		print("Log file not found")
		return None


def generate_map(ips, db):
	m = folium.Map(location=[50.0, 10.0], zoom_start=3)
	marker_cluster = MarkerCluster().add_to(m)

	print("Fetching the coordinates of new IP addresses...")
	for ip in ips:
		try:
			response = requests.get(f"http://ip-api.com/json/{ip}").json()
			if response.get('status') == 'success':
				lat = response['lat']
				lon = response['lon']
				country = response['country']
				db[ip] = [lat, lon, country]
				print(f"[+] New IP found: {ip} -> {country}")
			else:
				db[ip] = [0.0, 0.0, "Unknown"]
				print(f"[-] Error for IP (Saved as Unknown): {ip}")
			time.sleep(1.5)
		except Exception as e:
			print(f"[-] Error for IP {ip}: {e}")

	for ip in db:
		lat, lon, country = db[ip]
		if lat != 0.0 and lon != 0.0:
			folium.Marker(
				location=[lat, lon],
				popup=f"IP: {ip}<br>Country: {country}",
				icon=folium.Icon(color="red", icon="fire")
			).add_to(marker_cluster)

	m.save("attack_map.html")
	print("Done! Map has been saved as attack_map.html")


def profiler(db):
	print("Scanning logs for new login attempts...")
	try:
		for log in LOG_FILES:
			with open(log, 'r', encoding='utf-8') as f:
				for line in f:
					try:
						data = json.loads(line)
						ip = data.get("src_ip")
						if not ip or ip == "127.0.0.1":
							continue
						if ip not in db or len(db[ip]) < 4:
							db[ip] = {"credentials": [], "commands": [], "client_version": "", "hassh": ""}
						event_id = data.get('eventid')
						if event_id in ['cowrie.login.failed', 'cowrie.login.success']:
							user = data.get('username', '')
							passwd = data.get('password', '')
							cred_combo = f"{user}:{passwd}"

							if cred_combo not in db[ip]["credentials"]:
								db[ip]["credentials"].append(cred_combo)
								#print(f"[+] New Login:Passwd harvested from {ip} - {cred_combo}")

						elif event_id == 'cowrie.command.input':
							cmd = data.get('input', '')
							if cmd and cmd not in db[ip]["commands"]:
								db[ip]["commands"].append(cmd)
						elif event_id == 'cowrie.client.version':
							cmd = data.get('version', '')
							#print(f"[+] Client version found for {ip}: {cmd}")
							db[ip]['client_version'] = cmd
						elif event_id == 'cowrie.client.kex':
							cmd = data.get('hassh', '')
							#print(f"[+] HASSH found for {ip}: {cmd}")
							db[ip]['hassh'] = cmd
					except json.JSONDecodeError:
						pass
		return db
	except FileNotFoundError:
		print(f"File not found: {log}")
		return db


def main():
	print("--- Starting the CTI analysis ---")

	db_ip = load_db(db_ip_name)
	ips = get_ips(db_ip)

	if ips is not None:
		print(f"Found {len(ips)} new unique IP addresses.")
		generate_map(ips, db_ip)
		save_db(db_ip, db_ip_name)
		db_content = load_db(db_content_name)
		db_content = profiler(db_content)
		save_db(db_content, db_content_name)
	print("--- Analysis Finished ---")


if __name__ == '__main__':
	main()
