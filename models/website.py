 # -*- coding: utf-8 -*-
from openerp.models import Model
from openerp import fields

class Website(Model):
    _inherit = 'website'

    decibelinsight = fields.Boolean(
        string='Use DecibelInsight',
        default=False,
        help=('if activated DecibelInsight tracking is active'),
        translate=True
    )
    decibelinsight_script = fields.Text(
        string='DecibelInsight Script'
    )
