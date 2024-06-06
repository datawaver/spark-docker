import json
import requests


#
# Utility method to fetch data from any REST endpoint
#
def fetch_any_rest_endpoint(url, timeout=5):
    """
    Fetches data from a REST endpoint which returns json data.

    Args:
        url (str): The URL of the REST endpoint.
        timeout (int, optional): The timeout value in seconds. Defaults to 5.

    Returns:
        dict: The JSON response from the REST endpoint or
              None if the request timed out.

    Raises:
        requests.HTTPError: If the response status code is not 2xx.
    """
    try:
        response = requests.get(url=url, timeout=timeout)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
    except requests.Timeout:
        print(f"Request to {url} timed out after {timeout} seconds.")
        return None
    return response.json()


def fetch_enrichment_data(config, ignore_errors=True):
    result = dict()
    for entry in config:
        response_data = fetch_any_rest_endpoint(entry["url"])
        if response_data is None:
            continue
        for mapping in entry["mappings"]:
            result[mapping["target"]] = (
                response_data[mapping["src"]]
                if response_data and mapping["src"] in response_data
                else None
            )
    return result
