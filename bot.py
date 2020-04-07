import arrow
import json
import logging
import praw
import webbrowser
from urlextract import URLExtract


def interesting_url(urls):
    for u in urls:
        if "turnip.exchange/island" in u:
            return u

    return False


# Setup

extractor = URLExtract()

with open("./config.json", "r") as f:
    config = json.loads(f.read())

reddit = praw.Reddit(
    client_id=config["client_id"],
    client_secret=config["client_secret"],
    user_agent=config["user_agent"],
)

logging.basicConfig(format="%(message)s", level=logging.INFO)

for post in reddit.subreddit(config["subreddit"]).stream.submissions():
    numbers = [int(s) for s in post.title.split() if s.isdigit()]
    if numbers:
        # Hide posts with too little gain
        price = numbers[0]

        # Hide posts too old
        tt = arrow.get(post.created_utc)
        delta = arrow.utcnow() - tt

        if price > config['min_price'] and delta.seconds < 10 * 60:
            logging.info(
                f"[{tt.to('Europe/Rome').format('YYYY-MM-DD HH:mm:ss')}] {post.title} - {post.url}"
            )

            webbrowser.open(post.url)

            all_urls = extractor.find_urls(post.selftext)
            url = interesting_url(all_urls)
            if url:
                logging.info("===========> Opening turnip.exchange as well")
                webbrowser.open(url)
