"""adding content table

Revision ID: e59afef84129
Revises: c62ac2f27dff
Create Date: 2024-03-05 22:27:15.256128

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e59afef84129'
down_revision: Union[str, None] = 'c62ac2f27dff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
