import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except socket.gaierror:
        print("Hostname could not be resolved")
    except socket.error:
        print("Could not connect to the server")

def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

# Example usage
ip = "192.168.1.1"
start_port = 1
end_port = 1000
scan_ports(ip, start_port, end_port)