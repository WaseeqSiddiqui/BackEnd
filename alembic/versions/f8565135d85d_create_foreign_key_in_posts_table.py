"""create foreign key in posts table

Revision ID: f8565135d85d
Revises: 06ff41bce0d8
Create Date: 2024-07-27 10:26:00.342460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8565135d85d'
down_revision: Union[str, None] = '06ff41bce0d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts",sa.Column("owner_id",sa.Integer(),nullable=False))
    op.create_foreign_key("posts_users_fk",source_table="posts",referent_table="users",
                          local_cols=["owner_id"],remote_cols=["id"],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("posts_users_fk","posts")
    op.drop_column("posts","owner_id")
    pass
