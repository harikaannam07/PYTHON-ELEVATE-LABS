import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML from the news website
url = 'https://www.bbc.com/news'
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to fetch page. Status code: {response.status_code}")
    exit()

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract headline tags (h1, h2, h3)
headline_tags = soup.find_all(['h1', 'h2', 'h3'])

# Step 4: Clean and store headlines
headlines = []
for tag in headline_tags:
    text = tag.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)

# Step 5: Save headlines to a .txt file
with open('top_headlines.txt', 'w', encoding='utf-8') as file:
    for i, headline in enumerate(headlines, start=1):
        file.write(f"{i}. {headline}\n")

print(f"✅ {len(headlines)} headlines saved to 'top_headlines.txt'")
