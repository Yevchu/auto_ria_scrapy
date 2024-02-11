"""add username

Revision ID: 1cade85461a2
Revises: 7b3dbb0c3ab0
Create Date: 2024-02-11 03:40:19.302605

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '1cade85461a2'
down_revision: Union[str, None] = '7b3dbb0c3ab0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
            'cars_info',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('url', sa.String(), nullable=False),
            sa.Column('title', sa.String(180), nullable=False),
            sa.Column('price_usd', sa.String(), nullable=False),
            sa.Column('username', sa.String(), nullable=False),
            sa.Column('odometer', sa.String(), nullable=False),
            sa.Column('phone_number', sa.String(), nullable=False),
            sa.Column('image_url', sa.String(), nullable=False),
            sa.Column('images_count', sa.String(), nullable=False),
            sa.Column('car_number', sa.String(), nullable=False),
            sa.Column('car_vin', sa.String(), nullable=False),
            sa.Column('created_at', sa.DateTime(), server_default=func.now()),
        )


def downgrade() -> None:
    pass
