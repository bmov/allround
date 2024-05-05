from flask import Response, abort
from app import create_app
from components.render_json import message
from components.fileio import read_file

app = create_app()
