from app.models import Pages, PageFolders
from app.database import async_session

from sqlalchemy.sql.expression import select


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
    async def addPage(self, name, folder=0,
                      page_type='text', description=None):
        async with async_session() as session:
            find_folder = await session.execute(
                select(PageFolders).
                filter_by(id=folder)
            ).scalar_one()
            if not find_folder and folder:
                raise FolderNotFoundError()  # Folder not found

            find_name = await session.execute(
                select(Pages).
                filter_by(name=name, folder=folder)
            ).scalar_one()

            if find_name:
                raise PageNameError()  # Page name already exists

            page = Pages(name=name, folder=folder,
                         page_type=page_type, description=description)
            session.add(page)
            await session.commit()

        return True

    async def addFolder(self, name, parent=0, description=None):
        async with async_session() as session:
            find_name = await session.execute(
                select(PageFolders).
                filter_by(name=name, parent=parent)
            ).scalar_one()
            if find_name:
                raise PageFolderNameError()  # Folder name already exists

            page_folder = PageFolders(
                name=name, parent=parent, description=description)
            session.add(page_folder)
            await session.commit()

        return True
