"""add new column

Revision ID: 38894067e8b0
Revises: 1cade85461a2
Create Date: 2024-02-11 04:15:20.238474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func



# revision identifiers, used by Alembic.
revision: str = '38894067e8b0'
down_revision: Union[str, None] = '1cade85461a2'
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
            sa.Column('updated_at', sa.DateTime())

        )


def downgrade() -> None:
    pass
