import re

class IOCExtractor:
    def __init__(self):
        self.ip_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
        self.sha256_pattern = r'\b[A-Fa-f0-9]{64}\b'
        self.md5_pattern = r'\b[A-Fa-f0-9]{32}\b'
        self.domain_pattern = r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b'

    def extract_all(self, text: str) -> dict:
        return {
            "ips": list(set(re.findall(self.ip_pattern, text))),
            "sha256": list(set(re.findall(self.sha256_pattern, text))),
            "md5": list(set(re.findall(self.md5_pattern, text))),
            "domains": list(set(re.findall(self.domain_pattern, text)))
        }
