"""insert roles, permissions

Revision ID: 4890345f468
Revises: 182b6f3f375
Create Date: 2015-07-29 14:12:15.888786

"""

# revision identifiers, used by Alembic.
revision = '4890345f468'
down_revision = '182b6f3f375'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index('ix_roles_default', 'roles', ['default'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_roles_default', 'roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    ### end Alembic commands ###
