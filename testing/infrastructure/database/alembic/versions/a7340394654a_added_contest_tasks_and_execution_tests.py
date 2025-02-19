"""Added contest_tasks and execution_tests

Revision ID: a7340394654a
Revises: 
Create Date: 2025-02-19 23:07:00.891249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a7340394654a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    sa.Enum('TARGET_LANGUAGE', 'INPUT_OUTPUT', 'MAKE_FILE', name='executiontesttypeenum').create(op.get_bind())
    op.create_table('contest_tasks',
    sa.Column('task_info_id', sa.Uuid(), nullable=False),
    sa.Column('time_limit', sa.Integer(), nullable=False),
    sa.Column('memory_limit', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('task_info_id', name=op.f('pk_contest_tasks'))
    )
    op.create_table('executions_tests',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('task_info_id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('type', postgresql.ENUM('TARGET_LANGUAGE', 'INPUT_OUTPUT', 'MAKE_FILE', name='executiontesttypeenum', create_type=False), nullable=False),
    sa.Column('archive', sa.String(), nullable=True),
    sa.Column('input_files', postgresql.ARRAY(sa.String()), server_default='{}', nullable=False),
    sa.Column('output_files', postgresql.ARRAY(sa.String()), server_default='{}', nullable=False),
    sa.Column('test_file', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['task_info_id'], ['contest_tasks.task_info_id'], name=op.f('fk_executions_tests_task_info_id_contest_tasks'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_executions_tests'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('executions_tests')
    op.drop_table('contest_tasks')
    sa.Enum('TARGET_LANGUAGE', 'INPUT_OUTPUT', 'MAKE_FILE', name='executiontesttypeenum').drop(op.get_bind())
    # ### end Alembic commands ###
