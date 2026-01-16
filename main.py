#!/usr/bin/env python3
import argparse
import json
import sys
from datetime import datetime, timezone

# ===== IMPORTS DE TON FRAMEWORK =====
from recon.dns import DNSRecon
from recon.http import HTTPRecon
from recon.port_scan import PortScanner
from core.reporter import Reporter
from core.pdf_reporter import PDFReporter


def parse_args():
    parser = argparse.ArgumentParser(description="Attacker Recon Framework V2")
    parser.add_argument("--target", required=True, help="Cible (ex: example.com)")
    return parser.parse_args()


def main():
    args = parse_args()
    target = args.target

    print("\n======================================")
    print("  ATTACKER RECON FRAMEWORK - V2")
    print("======================================\n")
    print(f"[+] Target: {target}")
    print(f"[+] Start: {datetime.now(timezone.utc).isoformat()}\n")

    # Structure de base du rapport (FIX du bug JSON)
    report_data = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "tool": "Attacker Recon Framework V2",
            "target": target,
        },
        "modules": {}
    }

    # ======== MODULE 1: DNS RECON ========
    print("[*] Running DNS Recon...")
    try:
        dns = DNSRecon(target)
        dns_records = dns.run()

        report_data["modules"]["dns_recon"] = {
            "target": target,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "records": dns_records,
        }
        print("[+] DNS Recon completed.\n")
    except Exception as e:
        print(f"[-] DNS Recon error: {e}")
        report_data["modules"]["dns_recon"] = {
            "target": target,
            "error": str(e),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    # ======== MODULE 2: HTTP RECON ========
    print("[*] Running HTTP Recon...")
    try:
        http = HTTPRecon(target)
        http_result = http.run()

        report_data["modules"]["http_recon"] = {
            "url": f"http://{target}",
            "status_code": http_result.get("status_code"),
            "server": http_result.get("server"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        print("[+] HTTP Recon completed.\n")
    except Exception as e:
        print(f"[-] HTTP Recon error: {e}")
        report_data["modules"]["http_recon"] = {
            "url": f"http://{target}",
            "error": str(e),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    # ======== MODULE 3: PORT SCAN (CORRIGÉ) ========
    print("[*] Running Port Scan...")

    scanner = PortScanner(target)

    # Ports classiques (tu pourras les rendre paramétrables plus tard)
    COMMON_PORTS = [21, 22, 23, 25, 53, 80, 443, 8080]

    open_ports = []

    for port in COMMON_PORTS:
        try:
            if scanner.scan_port(port):  # ✅ CORRECTION ICI
                open_ports.append(port)
        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")

    report_data["modules"]["port_scan"] = {
        "target": target,
        "tested_ports": COMMON_PORTS,
        "open_ports": open_ports,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    print(f"[+] Open ports: {open_ports}")
    print("[+] Port Scan completed.\n")

    # ======== SAUVEGARDE DU RAPPORT ========
    print("[*] Saving reports...")

    safe_filename = f"report_{target.replace('.', '_')}_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"

    # JSON
    json_path = f"{safe_filename}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)

    print(f"[+] JSON saved: {json_path}")

    # PDF
    pdf_path = f"{safe_filename}.pdf"
    pdf = PDFReporter(report_data)
    pdf.generate(pdf_path)

    print(f"[+] PDF saved: {pdf_path}")
    print("\n=== Recon Completed ===\n")


if __name__ == "__main__":
    main()
