import os
import requests
from datetime import datetime

# Load cookies from environment variables or paste directly here
cookies = {
    "advanced-frontend": os.environ.get("LEME_ADVANCED_FRONTEND"),
    "_identity-frontend": os.environ.get("LEME_IDENTITY_FRONTEND"),
    "_csrf-frontend": os.environ.get("LEME_CSRF"),
    # Optional: add _ga or others if needed
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "X-PJAX": "true",
    "X-PJAX-Container": "#p0",
    "X-CSRF-Token": os.environ.get("LEME_CSRF_TOKEN"),
    "Referer": "https://lemehost.com/server/3098476/free_plan",
    "Accept": "text/html, */*; q=0.01",
}

url = "https://lemehost.com/server/3098476/free_plan?extend_time=1&_pjax=%23p0"

response = requests.get(url, headers=headers, cookies=cookies)

if response.status_code == 200:
    print(f"✅ Extend time success at {datetime.now()}")
else:
    print(f"❌ Failed with status {response.status_code}")
