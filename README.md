# spark-docker

spark-docker is a project that provides a local setup of a Spark cluster using Docker Compose. It allows you to test and debug the behavior of your Spark applications in a distributed environment.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Local Spark cluster setup using Docker Compose
- Easy testing and debugging of Spark applications
- Simulates a distributed environment for accurate testing
- Utilizes justfile for simplified command execution

## Prerequisites

Before getting started with spark-docker, ensure that you have the following prerequisites installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)
- justfile: [Install justfile](https://github.com/casey/just#installation)


## Usage

TLDR; `just demo` 

Here an example flow:

1. Start the Spark cluster using Docker Compose:
   ```
   just start
   ```

2. Access the Spark web UI by opening a web browser and navigating to `http://localhost:8080`.

3. Submit your Spark application to the cluster using the Spark submit command:
   ```
   just submit <path-to-your-application>
   ```

4. Monitor the progress and logs of your Spark application through the Spark web UI.

5. Stop the Spark cluster when you're done:
   ```
   just stop
   ```

## Configuration

The spark-docker project provides a default configuration for the Spark cluster. If you need to customize the configuration, you can modify the following files:

- `docker-compose.yaml`: Adjust the Docker Compose configuration for the Spark cluster.
- `spark-defaults.conf`: Configure Spark-specific settings.
- `log4j.properties`: Customize the logging configuration for Spark.

Make sure to rebuild the Docker images after making any configuration changes.

## Troubleshooting

As of some changes in the spark distribution in the Bitnami spark image, the following error may occur:

```
$ /opt/bitnami/spark# bin/run-example SparkPi

WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Exception in thread "main" org.apache.spark.SparkException: Failed to get main class in JAR with error 'File file:/opt/bitnami/spark/run-example does not exist'.  Please specify one with --class.
...
```
This is because someone added `--driver-java-options` to the `bin/spark-class org.apache.spark.deploy.SparkSubmit ` call which breaks argument parsing for `run-example`.

To get run-example working again, you can call it directly with the `spark-submit` command. Here is the example for `SparkPi`:

```
$SPARK_HOME/bin/spark-class org.apache.spark.deploy.SparkSubmit run-example SparkPi
```

## Contributing

Contributions to spark-docker are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Or just reach out to us directly.

## License

This project is licensed under the [MIT License](LICENSE).
