 # -*- coding: utf-8 -*-
from openerp.models import TransientModel
from openerp import fields

class WebsiteConfigSettings(TransientModel):
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
