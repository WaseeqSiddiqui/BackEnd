"""create column to posts table

Revision ID: 5bcb476c4d5f
Revises: 86e70e58580c
Create Date: 2024-07-27 09:54:50.376781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bcb476c4d5f'
down_revision: Union[str, None] = '86e70e58580c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column("posts","content")
    pass
