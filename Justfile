#!/usr/bin/env just

# Default recipe
default:
  just --list

# Start the Spark cluster in detached mode
start:
  docker-compose up -d

# Stop and remove the Spark cluster containers
stop:
  docker-compose down

# Submit a Spark application to the cluster
submit APP_PATH:
  docker-compose exec master spark-submit {{APP_PATH}}

# Display the logs of a specific node in the Spark cluster
logs SERVICE="":
  docker-compose logs -f {{SERVICE}}

# Do nothing but a hint to clean-all
clean: stop 
  @echo "Run 'just clean-all' to perform a complete cleanup of the docker environment"

# Perform a complete cleanup of the docker environment
clean-all:
  docker-compose down --rmi all --volumes --remove-orphans

