from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = "account.move"

    sale_order = fields.Boolean(string="Sale Order", compute="compute_sale_order", default=False)
    vat_type = fields.Selection([("non_vat", "Non VAT"), ("vat", "VAT"), ("svat", "SVAT")], string="VAT Types")
    is_qr_code = fields.Boolean("QR Code")

    def compute_sale_order(self):
        for move_id in self:
            move_id.sale_order = any(move_id.invoice_line_ids.mapped("sale_line_ids").mapped("order_id"))

    @api.onchange("vat_type")
    def onchange_on_vat_type(self):
        if self.vat_type == "non_vat":
            for line in self.line_ids:
                line.tax_ids = False
