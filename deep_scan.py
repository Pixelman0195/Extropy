from map import save_db, load_db, db_content_name
from sho_free import shodan_db
deep_db='hassh_file.json'

def main():
	data = dict()
	profile=load_db(db_content_name)
	enrich=load_db(shodan_db)
	for ip in profile:
		hassh_num = profile[ip]['hassh']
		if hassh_num != '':
			tmp = profile[ip].copy()
			tmp.pop('hassh', None)
			if hassh_num not in data:
				data[hassh_num] = {}
			data[hassh_num][ip] = tmp
			if ip in enrich:
				data[hassh_num][ip].update(enrich[ip])
	save_db(data, deep_db)
	print(f"[*] Successfully generated the {deep_db} database. Found {len(data)} unique signatures")

if __name__ == '__main__':
	main()