from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = "res.company"

    qr_img = fields.Binary("Payment QR")
