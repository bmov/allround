"""Fix page type

Revision ID: 09e5caa0b47a
Revises: 308fc4ae3f90
Create Date: 2024-10-21 06:43:45.765187

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09e5caa0b47a'
down_revision: Union[str, None] = '308fc4ae3f90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('folder_id', sa.Integer(), nullable=False))
        batch_op.drop_index('ix_pages_folder')
        batch_op.create_index(batch_op.f('ix_pages_folder_id'), ['folder_id'], unique=False)
        batch_op.drop_column('folder')

    with op.batch_alter_table('token_refreshers', schema=None) as batch_op:
        batch_op.drop_index('ix_token_refreshers_refresh_token')
        batch_op.create_index(batch_op.f('ix_token_refreshers_refresh_token'), ['refresh_token'], unique=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('token_refreshers', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_token_refreshers_refresh_token'))
        batch_op.create_index('ix_token_refreshers_refresh_token', ['refresh_token'], unique=False)

    with op.batch_alter_table('pages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('folder', sa.INTEGER(), nullable=False))
        batch_op.drop_index(batch_op.f('ix_pages_folder_id'))
        batch_op.create_index('ix_pages_folder', ['folder'], unique=False)
        batch_op.drop_column('folder_id')

    # ### end Alembic commands ###