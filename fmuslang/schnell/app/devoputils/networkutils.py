import psutil

def list_listening_ports():
    # Get all network connections
    connections = psutil.net_connections(kind='inet')

    # Filter only listening ports
    listening_ports = [conn for conn in connections if conn.status == psutil.CONN_LISTEN]

    # Sort the listening ports based on port number
    listening_ports.sort(key=lambda x: x.laddr.port)

    # Print the details of listening ports
    print("Listening Ports:")
    print("{:<20} {:<20} {:<10}".format("Local Address", "PID", "Status"))
    print("-" * 60)

    for port in listening_ports:
        local_address = f"{port.laddr.ip}:{port.laddr.port}"
        pid = port.pid if port.pid else "-"
        status = port.status

        print("{:<30} {:<20} {:<10}".format(local_address, pid, status))

if __name__ == "__main__":
    list_listening_ports()
