from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest
from pymongo import MongoClient
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

from tweets.spark_job import process_rdd


@pytest.fixture
def spark_context():
    # Create a SparkSession for testing
    spark = SparkSession.builder.appName("TestProcessRDD").getOrCreate()
    sc = spark.sparkContext
    yield sc
    spark.stop()


@pytest.fixture
def streaming_context(spark_context):
    # Create a StreamingContext for testing
    ssc = StreamingContext(spark_context, 1)  # Batch interval of 1 second
    yield ssc
    ssc.stop(stopSparkContext=False, stopGraceFully=True)


@pytest.fixture
def mock_db_client():
    # Create a mock MongoDB client
    return MagicMock(spec=MongoClient)


@patch("tweets.utils.fetch_any_rest_endpoint")
@patch("MongoClient")
def test_process_rdd(
    mock_fetch_any_rest_endpoint, mock_MongoClient, spark_context, streaming_context
):
    # Create a sample RDD with tweets
    tweets = [
        "This is a tweet about COVID-19 #coronavirus",
        "RT:Another retweet related to the pandemic",
        "A tweet with a URL https://example.com",
    ]
    rdd = spark_context.parallelize(tweets)

    # Set up the expected cleaned tweets
    expected_cleaned_tweets = [
        "This is a tweet about COVID-19 #coronavirus",
        "RT:Another retweet related to the pandemic",
        "A tweet with a URL https://example.com",
    ]

    # Set up the mock return value for fetch_coronavirus_data
    mock_fetch_any_rest_endpoint.return_value = {"cases": 42, "deaths": 23}

    process_rdd(rdd)

    # Assert that write_to_sink is called with the expected data
    mock_MongoClient.__getitem__.return_value.__getitem__.return_value.insert_one.assert_called_once()
    call_args = mock_db_client.__getitem__.return_value.__getitem__.return_value.insert_one.call_args[
        0
    ]
    inserted_data = call_args[0]

    assert inserted_data["content"] == expected_cleaned_tweets
    assert inserted_data["total_case_count"] == 1000
    assert inserted_data.keys() == {"content", "total_case_count", "timestamp"}
    assert isinstance(inserted_data["timestamp"], str)

    # Assert that the timestamp is in ISO format
    try:
        datetime.fromisoformat(inserted_data["timestamp"])
    except ValueError:
        pytest.fail("Invalid timestamp format")
