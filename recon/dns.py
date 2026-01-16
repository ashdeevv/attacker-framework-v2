import dns.resolver 
from datetime import datetime

class DNSRecon:
    def __init__(self, target, verbose=False):
        self.target = target
        self.verbose = verbose
    
    def resolve(self, record):
        try:
            answers = dns.resolver.resolve(self.target, record)
            return [str(rdata) for rdata in answers]
        except Exception:
            return []
    
    def run(self):
        results = {
            "target": self.target,
            "timestamp": datetime.utcnow().isoformat(),
            "records": {
                "A": self.resolve("A"),
                "MX": self.resolve("MX"),
                "NS": self.resolve("NS"),
                "TXT": self.resolve("TXT")
            }
        }

        if self.verbose:
            print("[DNS] Collected records:", results)
        
        return results