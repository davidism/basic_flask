"""user models

Revision ID: 35b593d48d6a
Revises: None
Create Date: 2013-06-25 10:10:53.866281
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression

# revision identifiers, used by Alembic.
revision = "35b593d48d6a"
down_revision = None


def upgrade():
    op.create_table("group",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False, unique=True, index=True)
    )
    op.create_table("user",
        sa.Column("id", sa.Integer),
        sa.Column("username", sa.String(254), nullable=False, unique=True, index=True),
        sa.Column("password", sa.String(60)),
        sa.Column("name", sa.String(254), nullable=False, server_default=""),
        sa.Column("email", sa.String(254), nullable=False, server_default=""),
        sa.Column("active", sa.Boolean, nullable=False, server_default=expression.true()),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_table("user_group",
        sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id"), primary_key=True),
        sa.Column("group_id", sa.Integer, sa.ForeignKey("group.id"), primary_key=True),
    )


def downgrade():
    op.drop_table("user_group")
    op.drop_table("user")
    op.drop_table("group")
