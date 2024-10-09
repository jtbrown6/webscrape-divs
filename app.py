from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    div_selector = request.form['div_selector']
    
    # Send a GET request to the webpage
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the div by the provided selector (assuming it is a class name)
        div_content = soup.find('div', class_=div_selector)
        
        # If the div is found, extract and display its text content
        if div_content:
            scraped_text = div_content.get_text().strip()
        else:
            scraped_text = "Div not found"
    else:
        scraped_text = f"Failed to retrieve the webpage. Status code: {response.status_code}"
    
    return render_template('result.html', scraped_text=scraped_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
