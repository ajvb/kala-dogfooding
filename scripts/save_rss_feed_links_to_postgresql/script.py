
#TODO:
# 1. Connect to postgresl
# 2. Get the most recent row from database
# 3. If one doesn't exist, use time from one month ago
# 4. Parse list of RSS Feeds
# 5. Grab all postings of that have occurred since time from 2 or 3
# 6. Load into postgresql


###
##  Run this job every 12 hours
###

import feedparser
from future import Future

FEEDS = [
    'http://feeds.feedburner.com/TechCrunch/startups',
    'http://worrydream.com/quotes/feed.xml',
    'http://martinfowler.com/feed.atom',
    'https://theintercept.com/feed/?rss'
]

# Utilizes futures to pull down all feeds, then sorts so the the most recent entry is the first entry
def get_all_feeds(feeds):
    future_calls = [Future(feedparser.parse, rss_url) for rss_url in feeds]
    feeds = [future_obj() for future_obj in future_calls]
    for feed in feeds:
        try:
            sorted_entries = sorted(feed.entries, key=lambda entry: entry['published'])
        except KeyError:
            try:
                sorted_entries = sorted(feed.entries, key=lambda entry: entry['updated'])
            except KeyError:
                continue

        sorted_entries.reverse()
        feed.entries = sorted_entries
    return feeds
