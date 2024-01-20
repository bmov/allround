"""Initial database

Revision ID: c9ddcdcf0b2d
Revises: 
Create Date: 2024-01-19 06:23:07.200256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9ddcdcf0b2d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gc_docs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('date', sa.Integer(), nullable=False),
    sa.Column('update_date', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('gc_docs', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_gc_docs_date'), ['date'], unique=False)
        batch_op.create_index(batch_op.f('ix_gc_docs_update_date'), ['update_date'], unique=False)
        batch_op.create_index(batch_op.f('ix_gc_docs_username'), ['username'], unique=False)

    op.create_table('gc_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('passwd', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('intro_text', sa.Text(), nullable=True),
    sa.Column('signdate', sa.Integer(), nullable=False),
    sa.Column('confirm', sa.Integer(), nullable=False),
    sa.Column('confirm_key', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('gc_users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_gc_users_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_gc_users_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('gc_users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_gc_users_username'))
        batch_op.drop_index(batch_op.f('ix_gc_users_email'))

    op.drop_table('gc_users')
    with op.batch_alter_table('gc_docs', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_gc_docs_username'))
        batch_op.drop_index(batch_op.f('ix_gc_docs_update_date'))
        batch_op.drop_index(batch_op.f('ix_gc_docs_date'))

    op.drop_table('gc_docs')
    # ### end Alembic commands ###
