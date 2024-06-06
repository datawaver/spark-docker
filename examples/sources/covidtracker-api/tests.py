from sources.covidtracker.fetch_remote_data import fetch_covid_cases


def test_fetch_covid_cases():
    cases = fetch_covid_cases()
    assert cases > 0
