import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_dam_data():
    date = datetime.today().strftime('%d.%m.%Y')
    print(date)
    
    try:
        page_url = "https://dams.kseb.in/?page_id=45"
        response = requests.get(page_url)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')
        article = soup.find('article')
        if not article:
            raise ValueError("Article not found")

        date_link = article.find('h3').find('a')
        if not date_link:
            raise ValueError("Date link not found")

        link = date_link['href']
        print(f"Date: {date}, Link: {link}")

        if not link:
            raise ValueError(f"No data found for {date}")

        data_response = requests.get(link)
        data_response.raise_for_status()  # Raise an exception for bad status codes

        data_soup = BeautifulSoup(data_response.content, 'html.parser')
        table = data_soup.find('table')
        if not table:
            raise ValueError("Data table not found")

        rows = table.find_all('tr')
        if len(rows) < 2:  # Check if table has at least two rows (header and data)
            raise ValueError("No rows found")

        header = [th.text.strip().encode('ascii', 'ignore').decode('ascii') for th in rows[0].find_all('td')]
        data = []
        for row in rows[2:]:  # skip the header row
            cols = row.find_all('td')
            cols = [col.text.strip().replace(u'\u00a0', ' ') for col in cols]
            data.append(dict(zip(header, cols)))

        json_data = json.dumps(data, indent=4)
        print(json_data)

        return {
            "date": date,
            "data": data
        }
    except Exception as e:
        print(f"Error occurred: {e}")
        return {
            "date": date,
            "error": str(e)
        }

def save_to_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving to JSON: {e}")

if __name__ == "__main__":
    dam_data = scrape_dam_data()
    if dam_data:
        filename = f"dam_data.json"
        save_to_json(dam_data, filename)
        print(f"Data saved to {filename}")
    else:
        print("Failed to scrape data")
