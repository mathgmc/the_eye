"""Addind partner table

Revision ID: 14d579e8a0ca
Revises: 
Create Date: 2022-05-12 11:51:03.891136

"""
from alembic import op
import sqlalchemy as sa


revision = '14d579e8a0ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('partner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('api_token', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_partner_api_token'), 'partner', ['api_token'], unique=True)


def downgrade():
    op.drop_index(op.f('ix_partner_api_token'), table_name='partner')
    op.drop_table('partner')
