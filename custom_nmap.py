import nmap

def perform_version_scan (target):
	nm = nmap.PortScanner()
	nm.scan(target, arguments='-sV')
	
	for host in nm.all_hosts():
		print(f"Host:{host}")
		for proto in nm[host].all_protocols():
			print(f"Protocol: {proto}")
			ports =  nm[host][proto].keys()
			for port in ports:
				service = nm[host][proto][port]
				print(f"Port:{port} \n Host:{host} \n Protocol:{proto} \n Service:{service['name']} \n Version:{service['version']}")
				
if __name__ == "__main__":
	target_host = input("Enter target host:\n")
	perform_version_scan(target_host)
