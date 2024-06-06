#!/bin/bash

export FLASK_APP=api.py 
pipenv run flask run --host=0.0.0.0
