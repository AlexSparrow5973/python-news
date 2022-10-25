"""del column 'mail' in model users

Revision ID: 1f6473ed91e8
Revises: fc5e47d06a7e
Create Date: 2022-10-25 22:53:56.873882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f6473ed91e8'
down_revision = 'fc5e47d06a7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['mail'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    # ### end Alembic commands ###