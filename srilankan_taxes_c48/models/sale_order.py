from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    vat_type = fields.Selection([("non_vat", "Non VAT"), ("vat", "VAT"), ("svat", "SVAT")], string="VAT Types")
    is_qr_code = fields.Boolean("QR Code")

    @api.onchange("vat_type")
    def onchange_on_vat_type(self):
        if self.vat_type == "non_vat":
            [setattr(line, 'tax_id', False) for line in self.order_line]
