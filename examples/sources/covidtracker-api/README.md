# COVID-19 Case Tracker

This project contains a Python script that fetches the total number of COVID-19 cases worldwide from the Worldometer website.
It is exposing these numbers as an HTTP Rest API Endpoint as json. To reduce the load on the Worldometer website and the risk to be blocked, the script caches the data.

```json
{
  "cases": 704753890,
  "timestamp": "2024-06-03T07:30:03.643574+00:00"
}
```

## Usage

Start the server with Docker or manually with `just run` and you will be presented with the endpoints of the api.

Here is an example output:

```bash
➜ just init run
 * Serving Flask app 'api.py'
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.178.137:5000
```

## Development

You will need the following tools to run this project:

- [just](https://github.com/casey/just/)
- python >= 3.12
- pipenv

Now use the just recipies like `just run` to start the server. Or `just test` to run the tests. More recipies can be found in the `Justfile` or with `just help`.
