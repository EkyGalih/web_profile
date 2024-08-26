"""ondelete pada tabel mahasiswa

Revision ID: 5e2951037093
Revises: 0fd8c611a17e
Create Date: 2024-08-26 15:18:47.594798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e2951037093'
down_revision = '0fd8c611a17e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint('mahasiswa_ibfk_1', type_='foreignkey')
        batch_op.drop_constraint('mahasiswa_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_dua'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_satu'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('mahasiswa_ibfk_2', 'dosen', ['dosen_satu'], ['id'])
        batch_op.create_foreign_key('mahasiswa_ibfk_1', 'dosen', ['dosen_dua'], ['id'])

    # ### end Alembic commands ###
