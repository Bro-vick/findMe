"""Remove email authentication

Revision ID: e47873cefb6e
Revises: 69fa46651ae6
Create Date: 2023-02-27 10:24:57.896322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e47873cefb6e'
down_revision = '69fa46651ae6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('confirmed')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('confirmed', sa.BOOLEAN(), nullable=True))

    # ### end Alembic commands ###