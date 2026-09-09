import map, sho_free, deep_scan, reporter
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
	[6]. Exit.''')
	while True:
		choice = input("Choose your option (1-5):")
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
			exit()
		else:
			print("Wrong selection: Please choose a valid option.")


if __name__ == '__main__':
	main()



