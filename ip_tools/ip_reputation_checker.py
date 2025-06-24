"""
Check IP reputation using AbuseIPDB
"""
import requests

# Replace this with your actual AbuseIPDB API key
API_KEY = 'your_api_key_here'

def check_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {
        "ipAddress": ip,
        "maxAgeInDays": "90"
    }
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()["data"]
        print(f"IP: {data['ipAddress']}")
        print(f"- Abuse Confidence Score: {data['abuseConfidenceScore']}%")
        print(f"- Country: {data['countryCode']}")
        print(f"- Total Reports: {data['totalReports']}")
        print(f"- Last Reported: {data['lastReportedAt']}")
    else:
        print(f"[!] Error {response.status_code}: {response.text}")

# Example usage:
# check_ip("8.8.8.8")
