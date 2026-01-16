import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Attacker Recon Framework V2")

    parser.add_argument("--target", required=True, help="Target domain or IP")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--output", default="attack_report", help="Base report name")

    return parser.parse_args()