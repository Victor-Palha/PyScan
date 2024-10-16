import socket
from datetime import datetime, timedelta
from typing import List


def identify_service(port: int) -> str:
    services: dict[int, str] = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        21: "FTP",
        25: "SMTP",
    }
    return services.get(port, "Unknown service")


class PortScanner:
    def __init__(self, ip: str, start_port: int = 1, end_port: int = 1024) -> None:
        self.ip: str = ip
        self.start_port: int = start_port
        self.end_port: int = end_port
        self.open_ports: List[int] = []

    def scan(self) -> List[int]:
        print(f"Scanning {self.ip} from port {self.start_port} to port {self.end_port}...")
        start_time: datetime = datetime.now()

        for port in range(self.start_port, self.end_port + 1):
            if self.is_port_open(port):
                self.open_ports.append(port)
                service: str = identify_service(port)
                print(f"Port {port} is open ({service})")

        end_time: datetime = datetime.now()
        scan_duration: timedelta = end_time - start_time
        print(f"\nScan complete with {scan_duration}")
        return self.open_ports

    def is_port_open(self, port: int) -> bool:
        sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout
        result: int = sock.connect_ex((self.ip, port))
        sock.close()
        return result == 0

    def display_open_ports(self) -> None:
        if self.open_ports:
            print("\nOpen ports found:")
            for port in self.open_ports:
                service: str = identify_service(port)
                print(f"- Port {port} ({service})")
        else:
            print("None open ports found")


if __name__ == "__main__":
    target_ip: str = input("What IP do you want to scan?: ")
    start_port: int = int(input("What port do you want to start looking? (Default 1) "))
    end_port: int = int(input("What port do you want to end looking? (Default 1024) "))

    scanner: PortScanner = PortScanner(target_ip, start_port, end_port)
    scanner.scan()
    scanner.display_open_ports()
