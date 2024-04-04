"""add content column to post table

Revision ID: 55c0dbc0de8e
Revises: dcf826c0fdb2
Create Date: 2024-04-02 10:47:22.087694

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55c0dbc0de8e'
down_revision: Union[str, None] = 'dcf826c0fdb2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
