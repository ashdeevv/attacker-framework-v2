import socket
from datetime import datetime

class PortScanner:
    def __init__(self, target, verbose=False):
        self.target = target
        self.verbose = verbose
    
    def scan_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((self.target, port))
        sock.close()
        return result == 0
    
    def run(self):
        open_ports = []
        for port in [21, 22, 80, 443, 8080]:
            if self.scan_port(port):
                open_ports.append(port)
        
        result = {
            "target": self.target,
            "open_ports": open_ports,
            "timestamp": datetime.utcnow().isoformat()
        }

        if self.verbose:
            print("[PORTS] Open ports:", open_ports)
        
        return result