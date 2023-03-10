"""New Update

Revision ID: d27c79721f8f
Revises: f0d6248bd55c
Create Date: 2023-03-10 09:13:24.274241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd27c79721f8f'
down_revision = 'f0d6248bd55c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('profile_picture',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.LargeBinary(),
               existing_nullable=True)
        batch_op.alter_column('phone_number',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=11),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('phone_number',
               existing_type=sa.String(length=11),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('profile_picture',
               existing_type=sa.LargeBinary(),
               type_=sa.VARCHAR(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###
