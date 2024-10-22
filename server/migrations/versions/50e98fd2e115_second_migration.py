"""second migration.

Revision ID: 50e98fd2e115
Revises: 9caed55189b5
Create Date: 2024-08-08 12:06:11.748501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50e98fd2e115'
down_revision = '9caed55189b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.add_column(sa.Column('course_id', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('class_level', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('department', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=False))
        batch_op.drop_index('ix_course_course_desc')
        batch_op.create_index(batch_op.f('ix_course_description'), ['description'], unique=False)
        batch_op.drop_column('dept')
        batch_op.drop_column('level')
        batch_op.drop_column('course_desc')
        batch_op.drop_column('cid')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cid', sa.VARCHAR(), nullable=False))
        batch_op.add_column(sa.Column('course_desc', sa.TEXT(), nullable=False))
        batch_op.add_column(sa.Column('level', sa.VARCHAR(), nullable=False))
        batch_op.add_column(sa.Column('dept', sa.TEXT(), nullable=False))
        batch_op.drop_index(batch_op.f('ix_course_description'))
        batch_op.create_index('ix_course_course_desc', ['course_desc'], unique=False)
        batch_op.drop_column('description')
        batch_op.drop_column('department')
        batch_op.drop_column('class_level')
        batch_op.drop_column('course_id')

    # ### end Alembic commands ###
