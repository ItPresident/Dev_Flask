"""add language to post

Revision ID: 656c80c6b416
Revises: 1c997121c7ff
Create Date: 2021-03-04 13:06:07.251783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '656c80c6b416'
down_revision = '1c997121c7ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
