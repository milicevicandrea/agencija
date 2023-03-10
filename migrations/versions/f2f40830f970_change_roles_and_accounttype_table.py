"""change roles and accounttype table

Revision ID: f2f40830f970
Revises: a1690a2e911b
Create Date: 2023-02-13 15:16:37.210604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2f40830f970'
down_revision = 'a1690a2e911b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_type', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'account_type', ['account_type'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    op.drop_table('account_type')
    # ### end Alembic commands ###
