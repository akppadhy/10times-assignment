import feedparser

def fetch_rss_data(url):
    feed = feedparser.parse(url)
    print("Feed Title:", feed.feed.title)
    for entry in feed.entries:
        print("Entry Title:", entry.title)
        print("Entry Link:", entry.link)
        
        # Check if 'published' exists before printing
        if 'published' in entry:
            print("Entry Published Date:", entry.published)
        
        # Check if 'summary' exists before printing
        if 'summary' in entry:
            print("Entry Summary:", entry.summary)
        
        print("\n")

rss_feed_urls = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
]

for url in rss_feed_urls:
    fetch_rss_data(url)

# Using feedparser correctly
f1 = feedparser.parse('Terrorism OR protest OR political unrest OR riot')
for entry in f1.entries:
    print(entry.title)
    print(entry.link)
    print(entry.summary)

f2 = feedparser.parse('positive OR uplifting')
for entry in f2.entries:
    print(entry.title)
    print(entry.link)
    print(entry.summary)

f3 = feedparser.parse('Natural Disaster')
for entry in f3.entries:
    print(entry.title)
    print(entry.link)
    print(entry.summary)

f4 = feedparser.parse('others')
for entry in f4.entries:
    print(entry.title)
    print(entry.link)
    print(entry.summary)

