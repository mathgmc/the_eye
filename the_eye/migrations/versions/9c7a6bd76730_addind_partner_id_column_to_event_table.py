"""Addind partner_id column to event table

Revision ID: 9c7a6bd76730
Revises: f45e48722aa1
Create Date: 2022-05-17 02:23:45.219588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c7a6bd76730'
down_revision = 'f45e48722aa1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('event', sa.Column('partner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'event', 'partner', ['partner_id'], ['id'])
    

def downgrade():
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_column('event', 'partner_id')
    