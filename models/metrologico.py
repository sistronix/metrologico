# Copyright 2019 Sistronix
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class Metrologico(models.Model):

    _name = 'metrologico'
    _description = 'Metrologico'  # TODO

    name = fields.Char()
