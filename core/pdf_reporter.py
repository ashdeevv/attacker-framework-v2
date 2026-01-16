from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import red, orange, green, black
from reportlab.pdfgen import canvas

class PDFReporter:
    def __init__(self, report_data):
        self.report = report_data

    def severity_color(self, text):   
        if "open_ports" in text.lower():
            return orange
        if "error" in text.lower():
            return red
        return black

    
    def generate(self, filename):
        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4

        y = height - 50

        # Title
        c.setFont("Helvetica-Bold", 18)
        c.drawString(50, y, "Attacker Recon Framework - Report")
        y -= 30

        # Metadata
        c.setFont("Helvetica", 10)
        meta = self.report.get("metadata", {})
        c.drawString(50, y, f"Target: {meta.get('target')}")
        y -= 15
        c.drawString(50, y, f"Generated: {meta.get('generated_at')}")
        y -= 30

        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "Findings:")
        y -= 20

        c.setFont("Helvetica", 10)

        modules = self.report.get("modules", {})

        for name, data in modules.items():
            c.setFillColor(black)
            c.drawString(50, y, f"- Module: {name}")
            y -= 15

            for key, value in data.items():
                line = f"  • {key}: {value}"
                c.setFillColor(self.severity_color(str(value)))
                c.drawString(60, y, line[:95])  # éviter lignes trop longues
                y -= 12

                if y < 50:
                    c.showPage()
                    y = height - 50
                    c.setFont("Helvetica", 10)

            y -= 10

        c.showPage()
        c.save()

        print(f"[+] PDF report generated: {filename}")