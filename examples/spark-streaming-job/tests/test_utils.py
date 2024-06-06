from unittest.mock import patch

import pytest
import requests

from tweets.utils import fetch_any_rest_endpoint


def test_fetch_any_rest_endpoint_returns_json_from_remote():
    # Mock the requests.get method to return the expected response
    with patch("tweets.utils.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"key": "value"}
        assert fetch_any_rest_endpoint(url="foo.bar") == {"key": "value"}
        mock_get.assert_called_once_with(url="foo.bar", timeout=5)


def test_fetch_any_rest_endpoint_timeout_returns_none():
    with patch("tweets.utils.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout()
        response = fetch_any_rest_endpoint("foo")

        assert response is None


def test_fetch_any_rest_endpoint_on_error_raises():
    #  Test the scenario where the request raises an exception (other than timeout)
    with patch("tweets.utils.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.HTTPError()
        with pytest.raises(requests.exceptions.HTTPError):
            fetch_any_rest_endpoint("foo")
