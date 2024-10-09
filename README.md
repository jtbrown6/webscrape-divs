# Web Scrape Site using Div Content
 
## Overview
This is a very simple application that allows the user to pull in website information that helps with querying from LLM's with the latest technical documentation. 

### How to Run

```bash
# Running Locally
docker build -t webscraper .
docker run -d -p 5000:5000 web-scraper

# Running on docker
docker pull jtbrown6/webscraper
docker run -d -p 5000:5000 jtbrown6/webscraper
```

### How to Use App
1. Pass in the url on which website you want to scrape
2. Right Click on website -> Inspect -> Find the top level class
3. Look for div class="field_needed"

```bash
# Test URL
https://docs.ansible.com/ansible/latest/os_guide/windows_setup.html
# Test Div/Class
wy-nav-content
```