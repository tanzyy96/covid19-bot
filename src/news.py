from newsapi import NewsApiClient
import os
import datetime

NEWSTOKEN = os.environ.get("NEWSAPITOKEN")
newsapi = NewsApiClient(api_key=NEWSTOKEN)

today = datetime.date.today()
fromdate = today - datetime.timedelta(days=7)


# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')

# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# # /v2/sources
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

