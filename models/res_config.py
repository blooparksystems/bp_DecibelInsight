# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, an open source suite of business apps
# This module copyright (C) 2015 bloopark systems (<http://bloopark.de>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.models import TransientModel
from openerp import fields


class WebsiteConfigSettings(TransientModel):

    """Adds the fields for DecibelInsight."""

    _inherit = 'website.config.settings'

    decibelinsight = fields.Boolean(
        string='Use DecibelInsight',
        related='website_id.decibelinsight',
        help=('if activated DecibelInsight tracking is active')
    )
    decibelinsight_script = fields.Text(
        string='DecibelInsight Script',
        related='website_id.decibelinsight_script'
    )
