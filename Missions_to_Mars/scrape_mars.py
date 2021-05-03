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
    browser = init_browser()
    facts_url = 'https://galaxyfacts-mars.com/
    mars_facts = pd.read_html(facts_url)
    mars_data = mars_df.to_html()
    mars_info['mars:facts'] = data

    return mars_info

def scrape_mars_hemispheres():
    browser = init_browser()
    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(hemispheres_url)
    html_hem = browser.html
    soup = BeautifulSoup(html_hem, 'html.parser')
    items_url = soup.find_all('div', class_='item')
    hem_list = []
    hem_main_url = 'https://marshemispheres.com/'

    for x in items_url: 
        title = i.find('h3').text
        img_url = i.find('a', class_='itemLink product-item')['href']
        browser.visit(hem_main_url + img_url)
        img_html = browser.html
        soup = BeautifulSoup( partial_img_html, 'html.parser')
        img_url = hem_main_url + soup.find('img', class_='wide-image')['src']
        hem_list.append({"title" : title, "img_url" : img_url})

        mars_info['hem_list'] = hem_list

        return mars_info

        browser.quit()
  



