from components.render_json import message
from components.page import (
    Page, FolderNotFoundError, PageNameError, PageFolderNameError)


class PagesApi:
    async def put(payload):
        name = payload['name']
        folder = payload['folder']
        page_type = payload['page_type']
        description = payload['description']

        page = Page()

        try:
            await page.addPage(name, folder=folder,
                               page_type=page_type,
                               description=description)
        except (FolderNotFoundError, PageNameError) as error:
            return message(None,
                           message=error, code=400)

        return {'status': True}

    def get():
        return {
            'data': 'It works!'
        }
