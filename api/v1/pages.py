from flask import request
from flask_restx import fields, Resource, Namespace, abort

from components.pagehandler import (
    PageHandler, FolderNotFoundError, PageNameError, PageFolderNameError)

Pages = Namespace('Pages')

model_put_page = Pages.model('NewPage', {
    'name': fields.String(description='Page name',
                          required=True),
    'folder': fields.Integer(description='Add page to children',
                             required=True),
    'page_type': fields.String(description='Page type (default: `text`)',
                               required=False),
    'description': fields.String(description='Description',
                                 required=False)

})


@Pages.route('/viewRoute')
class ViewRoute(Resource):
    def post(self):
        return {
            'data': 'It works!<br>test'
        }

    def get(self):
        return {
            'data': 'It works!'
        }


@Pages.route('/page')
class Page(Resource):
    @Pages.expect(model_put_page)
    def put(self):
        name = request.json.get('name')
        folder = request.json.get('folder')
        page_type = request.json.get('page_type')
        description = request.json.get('description')

        page_handler = PageHandler()

        try:
            page_handler.addPage(name, folder=folder,
                                 page_type=page_type, description=description)
        except (FolderNotFoundError, PageNameError) as error:
            return abort(500, error, status=False)

        return {'status': True}

    def get(self):
        return {
            'data': 'It works!'
        }
