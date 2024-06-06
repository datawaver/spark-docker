import os

from pymongo import MongoClient
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

from tweets.process import process

# Environment variables
TWITTER_STREAM_HOST = os.getenv("TWITTER_STREAM_HOST")
TWITTER_STREAM_PORT = int(os.environ.get("TWITTER_STREAM_PORT", 5555))
MONGODB_HOST = os.getenv("MONGODB_HOST")
MONGODB_PORT = int(os.environ.get("MONGODB_PORT", 27017))
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")


BUFFER_SIZE_IN_SECONDS = 5  # Batch interval of 20 seconds


def main():
    spark = SparkSession.builder.appName("TwitterCovidStream").getOrCreate()

    sc = spark.sparkContext
    ssc = StreamingContext(sparkContext=sc, batchDuration=BUFFER_SIZE_IN_SECONDS)
    tweets = ssc.socketTextStream(TWITTER_STREAM_HOST, TWITTER_STREAM_PORT)
    tweets.foreachRDD(process_rdd)

    ssc.start()
    ssc.awaitTermination()


def process_rdd(rdd):
    if not rdd.isEmpty():
        with MongoClient(MONGODB_HOST, MONGODB_PORT) as mongodb_client:
            tweets = rdd.collect()
            data = process(tweets)
            write_to_sink(mongodb_client, data)


def write_to_sink(client, data):
    db = client[MONGODB_DATABASE]
    collection = db[MONGODB_COLLECTION]
    collection.insert_one(data)


if __name__ == "__main__":
    main()
