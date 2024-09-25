"""init

Revision ID: 59f5414e7497
Revises: 
Create Date: 2024-09-25 16:48:39.208473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '59f5414e7497'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.add_column('workflow', sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.alter_column('workflow', 'status',
               existing_type=postgresql.ENUM('DRAFT', 'PUBLISHED', name='workflowstatusenum'),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('workflow', 'status',
               existing_type=postgresql.ENUM('DRAFT', 'PUBLISHED', name='workflowstatusenum'),
               nullable=False)
    op.drop_column('workflow', 'description')
    op.create_table('user',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    # ### end Alembic commands ###
