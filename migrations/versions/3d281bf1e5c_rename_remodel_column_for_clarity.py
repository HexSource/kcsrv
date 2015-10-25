"""Rename remodel column for clarity

Revision ID: 3d281bf1e5c
Revises: af50c5d131
Create Date: 2015-10-25 02:09:17.145736

"""

# revision identifiers, used by Alembic.
revision = '3d281bf1e5c'
down_revision = 'af50c5d131'

from alembic import op
import sqlalchemy as sa


def upgrade():
### commands auto generated by Alembic - please adjust! ###
    op.add_column('remodel', sa.Column('ship_api_id', sa.Integer(), nullable=True))
    op.drop_column('remodel', 'remodel_api_id')
    ### end Alembic commands ###


def downgrade():
### commands auto generated by Alembic - please adjust! ###
    op.add_column('remodel', sa.Column('remodel_api_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('remodel', 'ship_api_id')
    ### end Alembic commands ###
