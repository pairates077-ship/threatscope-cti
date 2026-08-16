from core.extractor import IOCExtractor
from core.aggregator import ThreatAggregator
from core.scorer import ThreatScorer

def main():
    print("=" * 60)
    print("      THREATSCOPE - CYBER THREAT INTELLIGENCE ENGINE      ")
    print("=" * 60)

    sample_log = """
    Suspicious connection detected from 185.220.101.5 and 8.8.8.8.
    Associated hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    Domain callback: evil-malware-c2.com
    """

    print("\n[*] Extracting IOCs from raw input...")
    extractor = IOCExtractor()
    iocs = extractor.extract_all(sample_log)

    print(f"Found IPs: {iocs['ips']}")
    print(f"Found Hashes: {iocs['sha256']}")
    print(f"Found Domains: {iocs['domains']}")

    print("\n[*] Analyzing Threat Intelligence & Risk Scores...")
    aggregator = ThreatAggregator()
    scorer = ThreatScorer()

    for ip in iocs['ips']:
        intel = aggregator.check_ip(ip)
        risk = scorer.calculate_ip_score(intel.get("abuse_score", 0), intel.get("reports", 0))
        print(f"[-] Target IP: {ip} | Risk: {risk['severity']} ({risk['score']}/100) | Country: {intel['country']}")

    print("\n[+] Threat Analysis Complete.")

if __name__ == "__main__":
    main()
