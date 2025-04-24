from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    apilayer_api_key = fields.Char(
        string="APILayer API Key",
        config_parameter='currency_rate_update_custom.apilayer_api_key'
    )




# # models/res_config_settings.py
# from odoo import models, fields

# class ResConfigSettings(models.TransientModel):
#     _inherit = 'res.config.settings'

#     apilayer_api_key = fields.Char(
#         string='APILayer API Key',
#         config_parameter='currency_rate_update.apilayer_api_key'
#     )
