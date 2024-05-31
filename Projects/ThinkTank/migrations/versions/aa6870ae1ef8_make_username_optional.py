"""Make username optional

Revision ID: aa6870ae1ef8
Revises: c3a2f969698b
Create Date: 2024-05-26 00:38:26.145761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa6870ae1ef8'
down_revision = 'c3a2f969698b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=64),
               nullable=True)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=60),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=15),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###