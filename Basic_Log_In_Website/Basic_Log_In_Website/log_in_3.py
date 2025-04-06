import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import requests
from bs4 import BeautifulSoup


session = requests.Session()
login_url = "https://quotes.toscrape.com/login"

login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, "html.parser")

csrf_token = soup.select_one('input[name="csrf_token"]')["value"] if soup.select_one('input[name="csrf_token"]') else None

crsf_token_extractor = soup.select_one('input')
print(crsf_token_extractor) 

'''

# Notice that crsf Token are Changing man 

Results are 
<input name="csrf_token" type="hidden" 
value="VgunWvRLAxbiJEesHUkrNSFGjzIDaTZCfmwXoMBqhdYytKOQlpcP"/>

<input name="csrf_token" type="hidden"
 value="FvpkTzjNeUrVIaLPigxWADBqCHdMmsoychRuwGZQtSKnJbYlEfOX"/>
'''