from app.models import Tables, TableColumns, TableRows, TableValues


class TableExistsError(Exception):
    def __str__(self):
        return 'This table already exists.'


class TableNotFoundError(Exception):
    def __str__(self):
        return 'Table not found.'


class ColumnExistsError(Exception):
    def __str__(self):
        return 'This column already exists.'


class TableHandler:
    def addTable(self, name):
        find_exists = Tables.query.filter_by(name=name).first()
        if find_exists:
            raise TableExistsError()  # Table already exists

        table = Tables(name=name)
        db.session.add(table)
        db.session.commit()

        return True

    def addColumn(self, table_id, name, column_type):
        find_table = Tables.query.filter_by(table_id=table_id).first()
        if not find_table:
            raise TableNotFoundError()  # Table not found

        find_column = TableColumns.query.filter_by(
            table_id=table_id, name=name).first()

        if find_column:
            raise ColumnExistsError()  # Column already exists

        column = TableColumns(table_id=table_id, name=name,
                              column_type=column_type)
        db.session.add(column)
        db.session.commit()

        return True

    def addRow(self, table_id, data):
        row = TableRows(table_id)
        db.session.add(row)
