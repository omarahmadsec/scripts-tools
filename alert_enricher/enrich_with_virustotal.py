"""
Enrich a URL using VirusTotal's API v3
"""
import requests
import base64

# Replace this with your real VirusTotal API key
API_KEY = 'your_api_key_here'

def encode_url(url):
    """VirusTotal requires the URL to be base64 encoded (without padding)."""
    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")

def enrich_url(url):
    encoded_url = encode_url(url)
    headers = {
        "x-apikey": API_KEY
    }
    vt_url = f"https://www.virustotal.com/api/v3/urls/{encoded_url}"
    response = requests.get(vt_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        stats = data['data']['attributes']['last_analysis_stats']
        print(f"VirusTotal Analysis for: {url}")
        print(f"- Harmless: {stats['harmless']}")
        print(f"- Malicious: {stats['malicious']}")
        print(f"- Suspicious: {stats['suspicious']}")
    else:
        print(f"[!] Error {response.status_code}: {response.text}")

# Example usage:
# enrich_url("http://example.com")
