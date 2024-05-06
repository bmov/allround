from app.models import (
    Tables, TableColumns, TableRows, TableValues)
from app.database import async_session

from sqlalchemy.sql.expression import select


class TableExistsError(Exception):
    def __str__(self):
        return 'This table already exists.'


class TableNotFoundError(Exception):
    def __str__(self):
        return 'Table not found.'


class ColumnExistsError(Exception):
    def __str__(self):
        return 'This column already exists.'


class Table:
    async def addTable(self, name):
        async with async_session() as session:
            get = await session.scalars(
                select(Tables).
                filter_by(name=name).
                limit(1)
            )

            find_exists = get.first()
            if find_exists:
                raise TableExistsError()  # Table already exists

            table = Tables(name=name)
            session.add(table)
            await session.commit()

        return True

    async def addColumn(self, table_id, name, column_type):
        async with async_session() as session:
            get = await session.scalars(
                select(Tables).
                filter_by(table_id=table_id).
                limit(1)
            )

            find_table = get.first()
            if not find_table:
                raise TableNotFoundError()  # Table not found

            find_column = TableColumns.query.filter_by(
                table_id=table_id, name=name).first()

            if find_column:
                raise ColumnExistsError()  # Column already exists

            column = TableColumns(table_id=table_id, name=name,
                                  column_type=column_type)
            session.add(column)
            await session.commit()

        return True

    async def addRow(self, table_id, data):
        async with async_session() as session:
            row = TableRows(table_id)
            await session.add(row)
