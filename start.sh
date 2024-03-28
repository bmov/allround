#!/bin/bash

export GUNICORN_DAEMON=1

function new_dir {
    [[ -d $1 ]] || mkdir $1
}

PROC_ALLROUND="./data/process/allround.pid"
PROC_ALLROUND_VIEWER="./data/process/allround-viewer.pid"

PORT_ALLROUND=9000
PORT_ALLROUND_VIEWER=8000

if [ "$1" == "stop" ]; then
    if [ -f $PROC_ALLROUND ] || [ -f $PROC_ALLROUND_VIEWER ]; then
        kill $(cat $PROC_ALLROUND)
        kill $(cat $PROC_ALLROUND_VIEWER)

    else
        echo "No running processes."
    fi
else
    if [ -f $PROC_ALLROUND ] || [ -f $PROC_ALLROUND_VIEWER ]; then
        echo "It seems already running."
    else
        new_dir "./data"
        new_dir "./data/process"
        new_dir "./data/logs"

        gunicorn --pid $PROC_ALLROUND --bind 0.0.0.0:$PORT_ALLROUND main:app
        gunicorn --pid $PROC_ALLROUND_VIEWER --bind 0.0.0.0:$PORT_ALLROUND_VIEWER main_viewer:app

        echo "=== ALLROUND DAEMON STARTED ==="
        echo ""
        echo "Main API: 0.0.0.0:$PORT_ALLROUND"
        echo "Main Viewer: 0.0.0.0:$PORT_ALLROUND_VIEWER"
    fi
fi
