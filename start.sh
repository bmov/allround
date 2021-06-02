#!/bin/bash

export GUNICORN_DAEMON=1

function new_dir {
    [[ -d $1 ]] || mkdir $1
}

new_dir "./data"
new_dir "./data/process"
new_dir "./data/logs"

gunicorn --pid ./data/process/allround.pid --bind 0.0.0.0:9000 app_init:app
gunicorn --pid ./data/process/allround-dashboard.pid --bind 0.0.0.0:8000 dashboard_init:app
