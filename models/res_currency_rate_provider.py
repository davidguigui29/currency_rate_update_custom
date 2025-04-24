import logging
import requests
from odoo import models, fields, _
from odoo.exceptions import UserError
from odoo.addons.currency_rate_update_custom import const

_logger = logging.getLogger(__name__)

class ResCurrencyRateProviderAPILayer(models.Model):
    _inherit = 'res.currency.rate.provider'

    service = fields.Selection(
        selection_add=[('apilayer', 'APILayer Exchange Rates')],
        ondelete={'apilayer': 'set default'}
    )

    def _get_supported_currencies(self):
        self.ensure_one()
        if self.service == 'apilayer':
            # Minimal static list for testing; expand as needed
            return const.SUPPORTED_CURRENCIES
            
        return super()._get_supported_currencies()

    def _obtain_rates(self, base_currency, currencies, date_from, date_to):
        self.ensure_one()
        if self.service != 'apilayer':
            return super()._obtain_rates(base_currency, currencies, date_from, date_to)

        
        apikey = self.env['ir.config_parameter'].sudo().get_param('currency_rate_update_custom.apilayer_api_key')
        if not apikey:
            raise UserError(_("APILayer API key is not configured. Please set it in the settings."))

        # --------------------------------------

        try:
            # **FETCH BASE CURRENCY RECORD**
            base_currency = self.env['res.currency'].search([('name', '=', base_currency)], limit=1)
            if not base_currency:
                raise UserError(_("Base currency '%s' not found!") % base_currency)

            url = f"https://api.apilayer.com/exchangerates_data/latest?base={base_currency.name}"
            headers = {"apikey": apikey}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if not data.get('success', True):  # Some plans omit 'success'
                raise UserError(_("APILayer API error: %s") % data.get('error', 'Unknown error'))

            rates = {}
            api_rates = data.get('rates', {})

            # FETCH CURRENCY RECORD FOR EACH CURRENCY
            for currency_code in currencies: # previously: for currency in currencies
                currency = self.env['res.currency'].search([('name', '=', currency_code)], limit=1)
                if not currency:
                    _logger.warning("Currency %s not found in Odoo", currency_code)
                    continue # Skip if currency not found

                code = currency.name
                if code in api_rates:
                    rates[code] = str(api_rates[code])
                else:
                    _logger.warning("Currency %s not found in API response", code)

            return {date_from.isoformat(): rates}

        except Exception as e:
            _logger.error("APILayer connection error: %s", str(e))
            raise UserError(_("Error connecting to APILayer: %s") % str(e))




