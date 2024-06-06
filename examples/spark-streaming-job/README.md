# Example Job Tweet Processor

This spark stream processor listens to the Twitter Stream, clean and enrich the tweets with the latest coronavirus data, and writes the processed data to MongoDB.

## Development

You will need the following tools to run this project:

- [just](https://github.com/casey/just/)
- python >= 3.9

`just init test` to run the tests. More recipies can be found in the `Justfile` or with `just help`.
