"""changeroles table updated

Revision ID: abd10ba9eede
Revises: f4cc77e4f748
Create Date: 2023-02-21 12:41:09.821845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abd10ba9eede'
down_revision = 'f4cc77e4f748'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('change_roles', schema=None) as batch_op:
        batch_op.alter_column('changed',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('change_roles', schema=None) as batch_op:
        batch_op.alter_column('changed',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=True)

    # ### end Alembic commands ###
