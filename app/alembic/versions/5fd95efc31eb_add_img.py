"""add img

Revision ID: 5fd95efc31eb
Revises: 8bc06c47c69a
Create Date: 2021-04-05 21:26:35.798300

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "5fd95efc31eb"
down_revision = "8bc06c47c69a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("pecha", sa.Column("img", sa.String(), nullable=True))
    op.create_index(op.f("ix_pecha_img"), "pecha", ["img"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_pecha_img"), table_name="pecha")
    op.drop_column("pecha", "img")
    # ### end Alembic commands ###
