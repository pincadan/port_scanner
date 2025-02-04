# port_scanner

Here's a simple port scanner implemented in Python:

This script defines two functions:

1. scan_port(ip, port): This function attempts to connect to a specific port on a given IP address. If the connection succeeds, it prints that the port is open.

2. scan_ports(ip, start_port, end_port): This function iterates through a range of ports and calls scan_port on each port to scan them.

In the example usage, you can specify the target IP address, the starting port, and the ending port to scan. The script will then scan all the ports in the specified range and print the open ports.

Please note that port scanning is a potentially dangerous activity and should be done with proper authorization and ethical considerations. It's important to use this script responsibly and ensure that you have the necessary permissions to scan the target systems.
