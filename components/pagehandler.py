from app.models import db, Pages, PageFolders


class FolderNotFoundError(Exception):
    def __str__(self):
        return 'The selected folder does not exist.'


class PageNameError(Exception):
    def __str__(self):
        return 'This page name already exists or is invalid.'


class PageFolderNameError(Exception):
    def __str__(self):
        return 'This folder name already exists or is invalid.'


class PageHandler:
    def addPage(self, name, folder=0, page_type='text', description=None):
        find_folder = PageFolders.query.filter_by(id=folder).first()
        if not find_folder and folder:
            raise FolderNotFoundError()  # Folder not found

        find_name = Pages.query.filter_by(name=name, folder=folder).first()
        if find_name:
            raise PageNameError()  # Page name already exists

        page = Pages(name=name, folder=folder,
                     page_type=page_type, description=description)
        db.session.add(page)
        db.session.commit()

        return True

    def addFolder(self, name, parent=0, description=None):
        find_name = PageFolders.query.filter_by(
            name=name, parent=parent).first()
        if find_name:
            raise PageFolderNameError()  # Folder name already exists

        page_folder = PageFolders(
            name=name, parent=parent, description=description)
        db.session.add(page_folder)

        return True
