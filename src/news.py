import sys
from googleapiclient.discovery import build
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureqs
import re
import urllib.parse
import urllib.request
from googlesearch import search
from newsapi import NewsApiClient
import os
import datetime
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


NEWSTOKEN = os.environ.get("NEWSAPITOKEN")
newsapi = NewsApiClient(api_key=NEWSTOKEN)

today = datetime.date.today()
fromdate = today - datetime.timedelta(days=7)

# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)
# sources = newsapi.get_sources()


def get_covid_articles():
    articles = newsapi.get_everything(q="COVID",
                                      from_param=str(fromdate),
                                      to=str(today),
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
    return articles


def get_covid_headlines():
    headlines = newsapi.get_top_headlines(q="COVID",
                                          language='en',
                                          page=1)
    return headlines


def get_covid_newsources():
    # TODO: can return in a nice, clickable format instead
    sources = newsapi.get_sources()
    return sources


local_news = []


def get_covid_local_news(country):

    global local_news
    news = []

    query = "covid {}".format(country)
    for i in search(query,        # The query you want to run
                    tld='com',  # The top level domain
                    lang='en',  # The language
                    num=10,     # Number of results per page
                    start=0,    # First result to retrieve
                    stop=10,  # Last result to retrieve
                    pause=0.0,  # Lapse between HTTP requests
                    ):
        news.append(i)
    if news == local_news:
        local_news = news[3:]
    else:
        local_news = news
    return local_news
