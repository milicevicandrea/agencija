"""reservation table

Revision ID: 9ef4f44079fd
Revises: f2f40830f970
Create Date: 2023-02-17 13:16:05.839502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ef4f44079fd'
down_revision = 'f2f40830f970'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('destination_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('reserved_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['destination_id'], ['destination.id'], ),
    sa.ForeignKeyConstraint(['reserved_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    # ### end Alembic commands ###
