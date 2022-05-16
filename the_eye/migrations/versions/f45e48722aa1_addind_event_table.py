"""Addind event table

Revision ID: f45e48722aa1
Revises: 14d579e8a0ca
Create Date: 2022-05-16 11:01:04.757427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f45e48722aa1'
down_revision = '14d579e8a0ca'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.String(length=36), nullable=False),
    sa.Column('category', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('data', sa.JSON(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_category'), 'event', ['category'], unique=False)
    op.create_index(op.f('ix_event_name'), 'event', ['name'], unique=False)
    op.create_index(op.f('ix_event_session_id'), 'event', ['session_id'], unique=False)
    

def downgrade():
    op.drop_index(op.f('ix_event_session_id'), table_name='event')
    op.drop_index(op.f('ix_event_name'), table_name='event')
    op.drop_index(op.f('ix_event_category'), table_name='event')
    op.drop_table('event')
    