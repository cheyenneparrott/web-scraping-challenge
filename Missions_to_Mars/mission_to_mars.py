#!/usr/bin/env python
# coding: utf-8

# # Cheyenne's Web Scraping Homework - Mission to Mars

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


# In[2]:


# "C:/Program Files(x86)/Google/Chrome/Application/chromedriver.exe"
def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


# ### NASA Mars News

# In[3]:

def marsscraping ():

    browser = init_browser()
    # executable_path = {"executable_path": "chromedriver.exe"}
    # browser = Browser("chrome", **executable_path, headless=False)

    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)


    # In[10]:


    # browser.is_element_present_by_css("ul.item_list li.slide", wait_time = 2)


    # In[4]:


    mars_html = browser.html
    mars_soup = bs(mars_html, "html.parser")


    # In[5]:


    # display(mars_soup)


    # In[11]:


    # news_title = mars_soup.find("div", class_ = "bottom_gradient" )
    # news_title.text

    find_item = mars_soup.select_one("ul.item_list li.slide")
    find_item


    # In[13]:


    news_title = find_item.find("div", class_ = "content_title").get_text()
    news_title


    # In[14]:


    news_paragraph = find_item.find("div", class_ = "article_teaser_body").get_text()
    news_paragraph


    # ### JPL Mars Space Images - Featured Image

    # In[16]:


    # "C:/Program Files(x86)/Google/Chrome/Application/chromedriver.exe"

    # executable_path = {"executable_path": "chromedriver.exe"}
    # browser = Browser("chrome", **executable_path, headless=False)

    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

    jpl_html = browser.html
    jpl_soup = bs(jpl_html, "html.parser")
        
    # display(jpl_soup)


    # In[17]:


    jpl_element = browser.find_by_id("full_image")
    jpl_element.click()


    # In[18]:


    more_jpl_element = browser.links.find_by_partial_text("more info")
    more_jpl_element.click()


    # In[20]:


    jpl_html = browser.html
    jpl_soup = bs(jpl_html, "html.parser")
        
    # display(jpl_soup)


    # In[21]:


    image = jpl_soup.select_one("figure.lede a img").get("src")
    image


    # In[22]:


    featured_image_url = "https://www.jpl.nasa.gov" + image
    featured_image_url


    # In[23]:


    facts_url = "https://space-facts.com/mars/"
    facts_table = pd.read_html(facts_url)[0]
    facts_table


    # In[24]:


    facts_table.columns = ["mars_characteristics", "mars_measurements"]
    facts_table.set_index("mars_characteristics", inplace = True)
    facts_table


    # In[26]:


    marshtml = facts_table.to_html(classes = "table table-striped")


    # ### Mars Hemispheres

    # In[35]:


    # "C:/Program Files(x86)/Google/Chrome/Application/chromedriver.exe"

    # executable_path = {"executable_path": "chromedriver.exe"}
    # browser = Browser("chrome", **executable_path, headless=False)

    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(hemi_url)

    hemi_html = browser.html
    hemi_soup = bs(hemi_html, "html.parser")
        
    # display(hemi_soup)


    # In[36]:


    find_hemi = hemi_soup.find_all("div", class_= "item")
    # display(find_hemi)


    # In[37]:


    len(find_hemi)


    # In[41]:


    hemi_list = []
    for link in find_hemi:
        final_url = link.find("a")['href']
        image_title = link.find("div", class_ = "description").find("a").find("h3").text
        scrape_url = "https://astrogeology.usgs.gov" + (final_url)
        browser.visit(scrape_url)
        scrape_html = browser.html
        scrape_soup = bs(scrape_html, "html.parser")
        image = scrape_soup.find("div", class_ = "downloads").find("ul").find("li").find("a")["href"]
        hemi_list.append({"title": image_title, "img_url": image})

    hemi_list

    marsscrapedict = {
        "title": news_title, "paragraph": news_paragraph,
        "image": featured_image_url, "table": marshtml, "hemispheres": hemi_list
    }
    return marsscrapedict

    

