"""add few column to posts table

Revision ID: eccc4986e74d
Revises: f8565135d85d
Create Date: 2024-07-27 10:51:06.586512

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eccc4986e74d'
down_revision: Union[str, None] = 'f8565135d85d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts",sa.Column("published",sa.Boolean(),nullable=False,server_default="TRUE"))
    op.add_column("posts",sa.Column("created_at",sa.TIMESTAMP(timezone=True),
                                    server_default=sa.text("now()"),nullable=False))
    pass


def downgrade():
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
