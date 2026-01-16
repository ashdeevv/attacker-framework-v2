import json
from datetime import datetime

class Reporter:
    def __init__(self, report_data, output="report"):
        """
        report_data = dict contenant le rapport
        output = nom de base du fichier (sans extension)
        """
        self.report_data = report_data
        self.output = output

    def save_json(self):
        filename = f"{self.output}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.report_data, f, indent=4, ensure_ascii=False)

        print(f"[+] Rapport JSON sauvegardé : {filename}")
        return filename