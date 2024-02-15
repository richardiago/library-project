"""empty message

Revision ID: 2ec64fd5b324
Revises: 3bf290a0af7c
Create Date: 2024-02-14 22:10:58.872583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ec64fd5b324'
down_revision = '3bf290a0af7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_borrowing', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genreId', sa.Uuid(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_book_borrowing_genreId_genre'), 'genre', ['genreId'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_borrowing', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_book_borrowing_genreId_genre'), type_='foreignkey')
        batch_op.drop_column('genreId')

    # ### end Alembic commands ###
