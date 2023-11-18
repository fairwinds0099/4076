import socket 

GREEN = "\033[92m"
RESET = "\033[0m"

def scan_ports(target, start_port, end_port, message): 
    print(f"Scanning target {target} for open ports...\n") 

    for port in range(start_port, end_port + 1): 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.settimeout(500) 
        result = sock.connect_ex((target, port)) 
        if result == 0: 
            print(f"Port {port}: {GREEN}Open{RESET}") 
            #sock.sendall(message.encode())
            #data = sock.recv(1024)
            #decoded_data = data.decode('utf-8', errors='replace')
            sock.send(b"GET / HTTP/1.1\r\n\r\n")
            banner = sock.recv(1024)
            #print(f"Received {decoded_data}")
            print(f" Benner: {banner.decode('utf-8', errors='replace')}")
        else: 
            print(f"Port {port}: Closed") 

        sock.close() 
  

if __name__ == "__main__": 
    target_host = input("Enter the target IP address:") 
    start_port = int(input("Enter the start port: ")) 
    end_port = int(input("Enter the end port: ")) 
    message = input("Enter transmitting message:")

     
    scan_ports(target_host, start_port, end_port, message) 

 
