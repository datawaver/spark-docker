from datetime import UTC, datetime
from time import sleep

from flask import Flask, jsonify
from flask_caching import Cache

from sources.covidtracker.fetch_remote_data import fetch_covid_cases

cache = Cache(config={"CACHE_TYPE": "SimpleCache"})

app = Flask(__name__)
cache.init_app(app)


@app.route("/")
@cache.cached(timeout=20)
def covid_cases():
    sleep(5)
    cases = fetch_covid_cases()
    timestamp = datetime.now(tz=UTC).isoformat()
    return jsonify({"timestamp": timestamp, "cases": cases})
