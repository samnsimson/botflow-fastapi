"""revised

Revision ID: c499e0ea5e38
Revises: 0286784dfefb
Create Date: 2024-10-02 22:25:59.918163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c499e0ea5e38'
down_revision: Union[str, None] = '0286784dfefb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('workflow', 'status',
               existing_type=postgresql.ENUM('DRAFT', 'PUBLISHED', name='workflowstatusenum'),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('workflow', 'status',
               existing_type=postgresql.ENUM('DRAFT', 'PUBLISHED', name='workflowstatusenum'),
               nullable=True)
    # ### end Alembic commands ###
