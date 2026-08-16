class ThreatScorer:
    @staticmethod
    def calculate_ip_score(abuse_confidence_score: int, reports_count: int) -> dict:
        score = min(100, int((abuse_confidence_score * 0.7) + (reports_count * 0.3 * 10)))
        
        if score >= 75:
            severity = "CRITICAL"
        elif score >= 50:
            severity = "HIGH"
        elif score >= 25:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        return {"score": score, "severity": severity}
