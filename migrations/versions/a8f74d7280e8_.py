"""empty message

Revision ID: a8f74d7280e8
Revises: 
Create Date: 2020-09-25 18:15:58.234852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8f74d7280e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('asin', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('product_id'),
    sa.UniqueConstraint('asin')
    )
    op.create_table('reviews',
    sa.Column('review_id', sa.Integer(), nullable=False),
    sa.Column('asin', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('review', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['asin'], ['products.asin'], ),
    sa.PrimaryKeyConstraint('review_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('products')
    # ### end Alembic commands ###