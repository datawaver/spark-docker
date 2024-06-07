from distutils.command import clean
import os
from datetime import datetime, timezone

from tweets.utils import fetch_enrichment_data

#
# This code will handle all the transformation and enrichements of the tweets
#

COVIDDATA_TRACKER_API_URL = os.getenv("COVIDDATA_TRACKER_API_URL")


def process(tweets):
    cleaned_tweets = [clean_tweet(tweet) for tweet in tweets]

    #
    # Enrichtment of any REST API data by configuration
    #
    enrichtment_data = fetch_enrichment_data(
        config=[
            {
                "url": COVIDDATA_TRACKER_API_URL,
                "mappings": [
                    {"src": "cases", "target": "total_case_count"},
                    # demo of adding more enrichments (does not exist in the api response :_)
                    # { "src": "deaths", "target": "total_death_count", },
                ],
            }
        ],
        ignore_errors=True,  # this will ignore non existing fields (src) in api response
    )

    timestamp = timestamp = datetime.now(tz=timezone.utc).isoformat()

    data = {
        "content": cleaned_tweets,
        "timestamp": timestamp,
    }
    # add the enrichments to the data
    data.update(enrichtment_data)

    return data


def clean_tweet(tweet):
    return tweet.replace("RT:", "")
