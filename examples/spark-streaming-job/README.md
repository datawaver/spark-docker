# Example Job Tweet Processor

This spark stream processor listens to the Twitter Stream, clean and enrich the tweets with the latest coronavirus data, and writes the processed data to MongoDB.

## Usage

To submit the job to the cluster, you can use the following command:

```bash
just build submit
```

Per default it will submit to `master:7077`, see the [Justfile](Justfile).

Build with conda environment in docker on an arm64 machine (like Apple Silicon M1) doesn't work yet. 

## Development

You will need the following tools to run this project:

- [just](https://github.com/casey/just/)
- python >= 3.9

`just init test` to run the tests. More recipies can be found in the `Justfile` or with `just help`.

