"""criaçao da tabela credit_cad

Revision ID: 4751cb372b68
Revises: 36838f3c7753
Create Date: 2021-06-25 20:08:04.543123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4751cb372b68'
down_revision = '777225a2427c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('credit_cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('expire_date', sa.String(), nullable=False),
    sa.Column('number', sa.String(), nullable=False),
    sa.Column('provider', sa.String(length=50), nullable=False),
    sa.Column('security_code', sa.String(length=3), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('credit_cards')
    # ### end Alembic commands ###
