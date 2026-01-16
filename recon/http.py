import requests
from datetime import datetime

class HTTPRecon:
    def __init__(self, target, verbose=False):
        self.target = target if target.startswith("http") else "http://" + target
        self.verbose = verbose
    
    def run(self):
        try:
            r = requests.get(self.target, timeout=10)
            result = {
                "url": self.target,
                "status_code": r.status_code,
                "server": r.headers.get("Server", "Unknowm"),
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            result = {"error": str(e)}
        
        if self.verbose:
            print("[HTTP] Result:", result)
        
        return result