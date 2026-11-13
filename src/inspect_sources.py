import urllib.request
import urllib.parse
import ssl
import json
import re
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        return r.read().decode('utf-8', errors='ignore')

# 1. USGS water
print("--- D9: USGS ---")
try:
    html = fetch("https://water.usgs.gov/watuse/data/")
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        if any(w in href for w in ['2015', '2020', 'county', 'watuse', 'data']):
            print("USGS Link:", urllib.parse.urljoin("https://water.usgs.gov/watuse/data/", href), "| Text:", a.text.strip())
except Exception as e:
    print("USGS error:", e)

# 2. D3: MSD-LIVE
print("\n--- D3: MSD-LIVE ---")
try:
    html = fetch("https://data.msdlive.org/records/65g71-a4731")
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        if 'download' in a['href'] or 'files' in a['href']:
            print("MSD-LIVE link:", urllib.parse.urljoin("https://data.msdlive.org/records/65g71-a4731", a['href']), a.text.strip())
except Exception as e:
    print("MSD-LIVE error:", e)

# 3. D4: FracTracker
print("\n--- D4: FracTracker ---")
try:
    html = fetch("https://fractracker.org/data-centers/")
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        if any(w in a['href'].lower() for w in ['download', 'arcgis', 'csv', 'sheet', 'drive', 'data']):
            print("FracTracker link:", a['href'], a.text.strip())
except Exception as e:
    print("FracTracker error:", e)

# 4. D6: EPRI
print("\n--- D6: EPRI ---")
try:
    html = fetch("https://powering-intelligence.epri.com/")
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        if any(w in a['href'].lower() for w in ['download', 'report', 'data', 'csv', 'pdf', 'xlsx']):
            print("EPRI link:", urllib.parse.urljoin("https://powering-intelligence.epri.com/", a['href']), a.text.strip())
except Exception as e:
    print("EPRI error:", e)

# 5. D7: EIA-930
print("\n--- D7: EIA-930 ---")
try:
    html = fetch("https://www.eia.gov/electricity/gridmonitor/")
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        if any(w in a['href'].lower() for w in ['download', 'data', 'eia930', 'bulk', 'csv']):
            print("EIA-930 link:", urllib.parse.urljoin("https://www.eia.gov/electricity/gridmonitor/", a['href']), a.text.strip())
except Exception as e:
    print("EIA-930 error:", e)

# 6. D10: Zenodo EJScreen
print("\n--- D10: Zenodo EJScreen ---")
try:
    html = fetch("https://zenodo.org/records/14767363")
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        if 'files' in a['href']:
            print("Zenodo link:", urllib.parse.urljoin("https://zenodo.org/records/14767363", a['href']), a.text.strip())
except Exception as e:
    print("Zenodo error:", e)
