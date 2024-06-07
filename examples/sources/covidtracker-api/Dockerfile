# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv
RUN pip install pipenv

# Install the dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code to the container
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["/bin/bash", "./run.sh"]
