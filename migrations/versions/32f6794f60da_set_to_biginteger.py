"""set to BigInteger()

Revision ID: 32f6794f60da
Revises: 09e5caa0b47a
Create Date: 2025-06-25 14:16:21.077946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32f6794f60da'
down_revision: Union[str, None] = '09e5caa0b47a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

bind = op.get_bind()


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('docs', schema=None) as batch_op:
        if bind.engine.name == 'postgresql':
            batch_op.alter_column('id',
                                  existing_type=sa.INTEGER(),
                                  type_=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  existing_nullable=False)
        else:
            batch_op.alter_column('id',
                                  existing_type=sa.INTEGER(),
                                  type_=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  existing_nullable=False,
                                  autoincrement=True)
        batch_op.alter_column('date',
                              existing_type=sa.INTEGER(),
                              type_=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                              existing_nullable=False)
        batch_op.alter_column('update_date',
                              existing_type=sa.INTEGER(),
                              type_=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                              existing_nullable=True)

    with op.batch_alter_table('token_refreshers', schema=None) as batch_op:
        if bind.engine.name == 'postgresql':
            batch_op.alter_column('id',
                                  existing_type=sa.INTEGER(),
                                  type_=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  existing_nullable=False)
        else:
            batch_op.alter_column('id',
                                  existing_type=sa.INTEGER(),
                                  type_=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  existing_nullable=False,
                                  autoincrement=True)
        batch_op.alter_column('expire',
                              existing_type=sa.INTEGER(),
                              type_=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                              existing_nullable=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        if bind.engine.name == 'postgresql':
            batch_op.alter_column('id',
                                  existing_type=sa.INTEGER(),
                                  type_=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  existing_nullable=False)
        else:
            batch_op.alter_column('id',
                                  existing_type=sa.INTEGER(),
                                  type_=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  existing_nullable=False,
                                  autoincrement=True)
        batch_op.alter_column('signdate',
                              existing_type=sa.INTEGER(),
                              type_=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                              existing_nullable=False)

    with op.batch_alter_table('page_folders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.BigInteger().with_variant(
            sa.Integer(), 'sqlite'), nullable=False))
        batch_op.add_column(sa.Column('update_date', sa.BigInteger(
        ).with_variant(sa.Integer(), 'sqlite'), nullable=True))
        batch_op.create_index(batch_op.f('ix_page_folders_date'), [
                              'date'], unique=False)
        batch_op.create_index(batch_op.f('ix_page_folders_update_date'), [
                              'update_date'], unique=False)

    with op.batch_alter_table('pages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.BigInteger().with_variant(
            sa.Integer(), 'sqlite'), nullable=False))
        batch_op.add_column(sa.Column('update_date', sa.BigInteger(
        ).with_variant(sa.Integer(), 'sqlite'), nullable=True))
        batch_op.create_index(batch_op.f('ix_pages_date'), [
                              'date'], unique=False)
        batch_op.create_index(batch_op.f('ix_pages_update_date'), [
                              'update_date'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('signdate',
                              existing_type=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                              type_=sa.INTEGER(),
                              existing_nullable=False)
        if bind.engine.name == 'postgresql':
            batch_op.alter_column('id',
                                  existing_type=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  type_=sa.INTEGER(),
                                  existing_nullable=False)
        else:
            batch_op.alter_column('id',
                                  existing_type=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  type_=sa.INTEGER(),
                                  existing_nullable=False,
                                  autoincrement=True)

    with op.batch_alter_table('token_refreshers', schema=None) as batch_op:
        batch_op.alter_column('expire',
                              existing_type=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                              type_=sa.INTEGER(),
                              existing_nullable=False)
        if bind.engine.name == 'postgresql':
            batch_op.alter_column('id',
                                  existing_type=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  type_=sa.INTEGER(),
                                  existing_nullable=False)
        else:
            batch_op.alter_column('id',
                                  existing_type=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  type_=sa.INTEGER(),
                                  existing_nullable=False,
                                  autoincrement=True)

    with op.batch_alter_table('docs', schema=None) as batch_op:
        batch_op.alter_column('update_date',
                              existing_type=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                              type_=sa.INTEGER(),
                              existing_nullable=True)
        batch_op.alter_column('date',
                              existing_type=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                              type_=sa.INTEGER(),
                              existing_nullable=False)
        if bind.engine.name == 'postgresql':
            batch_op.alter_column('id',
                                  existing_type=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  type_=sa.INTEGER(),
                                  existing_nullable=False)
        else:
            batch_op.alter_column('id',
                                  existing_type=sa.BigInteger().with_variant(sa.Integer(), 'sqlite'),
                                  type_=sa.INTEGER(),
                                  existing_nullable=False,
                                  autoincrement=True)

    with op.batch_alter_table('pages', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_pages_update_date'))
        batch_op.drop_index(batch_op.f('ix_pages_date'))
        batch_op.drop_column('update_date')
        batch_op.drop_column('date')

    with op.batch_alter_table('page_folders', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_page_folders_update_date'))
        batch_op.drop_index(batch_op.f('ix_page_folders_date'))
        batch_op.drop_column('update_date')
        batch_op.drop_column('date')

    # ### end Alembic commands ###
