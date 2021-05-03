import os
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager

def init_browser(): 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', headless=True, **exec_path)

mars_info = {}

def scrape_mars_news():
    browser = init_browser()
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    mars_info['news_title'] = news_title
    mars_info['news_p'] = news_p

    return mars_info

def scrape_mars_facts():

    facts_url = 'https://galaxyfacts-mars.com/
    mars_facts = pd.read_html(facts_url)
    mars_data = mars_df.to_html()
    mars_info['mars:facts'] = data

    return mars_info



