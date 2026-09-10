import map, sho_free, deep_scan, reporter
import keyring as kr
header=r'''=========================================================================================
 ██████████ █████ █████ ███████████ ███████████      ███████    ███████████  █████ █████
▒▒███▒▒▒▒▒█▒▒███ ▒▒███ ▒█▒▒▒███▒▒▒█▒▒███▒▒▒▒▒███   ███▒▒▒▒▒███ ▒▒███▒▒▒▒▒███▒▒███ ▒▒███ 
 ▒███  █ ▒  ▒▒███ ███  ▒   ▒███  ▒  ▒███    ▒███  ███     ▒▒███ ▒███    ▒███ ▒▒███ ███  
 ▒██████     ▒▒█████       ▒███     ▒██████████  ▒███      ▒███ ▒██████████   ▒▒█████   
 ▒███▒▒█      ███▒███      ▒███     ▒███▒▒▒▒▒███ ▒███      ▒███ ▒███▒▒▒▒▒▒     ▒▒███    
 ▒███ ▒   █  ███ ▒▒███     ▒███     ▒███    ▒███ ▒▒███     ███  ▒███            ▒███    
 ██████████ █████ █████    █████    █████   █████ ▒▒▒███████▒   █████           █████   
▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒   ▒▒▒▒▒    ▒▒▒▒▒▒▒    ▒▒▒▒▒           ▒▒▒▒▒    
=========================== The CTI Project by Pixelman0195 v1.0 ============================='''

def main():
	print()
	print(header)
	print('''Options:
	[1]. Profile IP Addresses from Cowrie logs and generate an interactive map.
	[2]. Enrich IP data using InternetDB.
	[3]. Sort the data using hassh numbers and client versions.
	[4]. Report IP addresses to AbuseIPDB.
	[5]. Help.
	[6]. API keys configuration.
	[7]. Exit''')
	while True:
		choice = input("Choose your option (1-7):")
		if choice == '1':
			map.main()
		elif choice == '2':
			sho_free.main()
		elif choice == '3':
			deep_scan.main()
		elif choice == '4':
			reporter.main()
		elif choice == '5':
			print("Help option is a work in progress. For now try the readme file. Sorry for the inconvenience!")
		elif choice == '6':
			api_keys()
		elif choice == '7':
			exit()
		else:
			print("Wrong selection: Please choose a valid option.")

def api_keys():
	print()
	print('''Which API key would you like to configure?
		  [1]. AbuseIPDB
		  [2]. Return''')
	while True:
		choice=input('Choose your option (1-2): ')
		if choice == '1':
			cfg_api_key('AbuseIPDB')
		elif choice == '2':
			break
		else:
			print("Invalid input. Please choose a correct option.")

def cfg_api_key(serv):
	print()
	while True:
		choice=input("Do you want to update or delete your API key? (update/delete/return): ")
		if choice == 'update':
			#profile = input("Enter your local username: ")
			profile='extropy'
			key = input("Enter your new API key: ")
			kr.set_password(serv,profile,key)
			print("Key updated successfully!")
			break
		elif choice == 'delete':
			#profile = input("Enter your local username: ")
			profile='extropy'
			try:
				kr.delete_password(serv,profile)
				print("Key deleted successfully!")
			except kr.errors.PasswordDeleteError:
				print("[-] Error: No API key found to delete.")
			break
		elif choice == 'return':
			break
		else:
			print("Invalid input. Please choose a correct option.")
if __name__ == '__main__':
	main()



