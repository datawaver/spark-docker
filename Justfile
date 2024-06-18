#!/usr/bin/env just

MASTER_SPARK_UI_PORT := env_var_or_default('MASTER_SPARK_UI_PORT', '8080')

# Default recipe
@default:
  just --list
  echo 
  echo "Master Spark UI port: {{MASTER_SPARK_UI_PORT}}"

alias run := start
# Start the Spark cluster in detached mode
start SERVICE="":
  docker-compose up -d {{SERVICE}}
  @echo "To access the spark master use: http://localhost:{{MASTER_SPARK_UI_PORT}}"

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
  just _find_and_remove_dir ".*_cache"
    
@_find_and_remove_dir PATTERN:
    find . -name "{{PATTERN}}" -type d -maxdepth 1 -exec rm -rf {} \;

# Perform a complete cleanup of the docker environment
clean-all:
  docker-compose down --rmi all --volumes --remove-orphans
  docker image prune -f

# Test is we just can start everything
@test:
  just start || echo "🚫 [ERROR] Failed to start everything successfully. 🚫"
  just stop

# ----------------------------------------
# Additional recipes for debugging and testing
# ----------------------------------------

# Display important information about the Docker Compose setup
@info:
    echo
    echo "Here some environement information about the Docker Compose setup:"
    echo "-----------------------------"
    echo "Services:"
    echo "-----------------------------"
    docker-compose config --services
    echo "\n >> Running containers:"
    docker-compose ps
    echo "-----------------------------"
    echo "Container resource usage:"
    echo "-----------------------------"
    docker-compose top
    echo "-----------------------------"
    echo "Exposed ports:"
    echo "-----------------------------"
    just _ports
    echo "-----------------------------"
    echo "Images used by services:"
    echo "-----------------------------"
    docker-compose images
    echo "\n >> Container logs (last 10 lines):"
    docker-compose logs --tail 10

_ports:
    #!/usr/bin/env bash
    docker-compose ps --format json | jq -r '.Name, .Ports'


# Start a bash shell in the submitter
submitter: 
  docker-compose build submitter 
  just start submitter
  docker-compose exec submitter bash

# Check the tweets in the mongodb
@check:
    echo "Checking mongo db ..."
    docker-compose exec mongodb bash -c "mongo twitter_data --eval 'db.stats()'"
    docker-compose exec mongodb bash -c "mongo twitter_data --eval 'db.tweets.find().sort({ timestamp: -1 }).limit(2).pretty()'"

@demo:
  echo "Starting everything and submit ... hit ctrl+c to stop the demo ... "
  echo "Afterwardsyou can check the tweets in the mongodb with \`just check\`"
  echo "Press any key to continue ..."
  read -n 1 -s
  just start
  docker compose exec submitter bash -c "cd /app && just submit"
