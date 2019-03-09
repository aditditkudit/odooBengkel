from odoo import api, fields, models, _
from odoo.exceptions import Warning
import unicodedata

class cb_pendaftaran(models.Model):
    _name = 'cb.pendaftaran'

    name = fields.Char(string='Pendaftaran', default='/')
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('confirm', 'Confirmed'),('cancel','Cancelled')], default='draft')
    kustomer_id = fields.Many2one(comodel_name='res.partner', string='Customer', domain=[('kustomer','=',True)] )
    lining_id = fields.Many2one(comodel_name='cb.lining', string='Lining yang Dipakai')
    tanggal = fields.Datetime(string='Tanggal', default=fields.Datetime.now())
    note = fields.Html(string='Note')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].get_sequence('Pendaftaran','cb.pendaftaran','DFT/%(y)s/',5)
        return super(cb_pendaftaran, self).create(vals)
    
    @api.multi
    def name_get(self):
        result = []
        for me_id in self:
            result.append((me_id.id, '%s - %s' % (me_id.name, me_id.kustomer_id.name)))
        return result
    
    @api.model
    def name_search(self, name, args=None, operator='ilike',limit=100):
        args = args or []
        if name :
            recs = self.search([
                '|',
                ('kustomer_id.name', operator, name),
                ('name', operator, name),
            ] + args, limit=limit)
        else:
            recs = self.search([] + args, limit=limit)
        return recs.name_get()

    
    

    
    
    
