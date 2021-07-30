# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Sponsor model

Revision ID: d0c22553b338
Revises: 69b928240b2f
Create Date: 2021-05-26 18:23:27.021443
"""

import sqlalchemy as sa
import sqlalchemy_utils

from alembic import op
from sqlalchemy.dialects import postgresql

revision = "d0c22553b338"
down_revision = "69b928240b2f"

# Note: It is VERY important to ensure that a migration does not lock for a
#       long period of time and to ensure that each individual migration does
#       not break compatibility with the *previous* version of the code base.
#       This is because the migrations will be ran automatically as part of the
#       deployment process, but while the previous version of the code is still
#       up and running. Thus backwards incompatible changes must be broken up
#       over multiple migrations inside of multiple pull requests in order to
#       phase them in over multiple deploys.


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "sponsors",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("service", sa.String(), nullable=True),
        sa.Column("activity_markdown", sa.Text(), nullable=True),
        sa.Column("link_url", sqlalchemy_utils.types.url.URLType(), nullable=False),
        sa.Column(
            "color_logo_url", sqlalchemy_utils.types.url.URLType(), nullable=False
        ),
        sa.Column(
            "white_logo_url", sqlalchemy_utils.types.url.URLType(), nullable=True
        ),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("footer", sa.Boolean(), nullable=False),
        sa.Column("psf_sponsor", sa.Boolean(), nullable=False),
        sa.Column("infra_sponsor", sa.Boolean(), nullable=False),
        sa.Column("one_time", sa.Boolean(), nullable=False),
        sa.Column("sidebar", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("sponsors")
    # ### end Alembic commands ###
