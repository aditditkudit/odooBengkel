from odoo import api, fields, models


class cb_lining(models.Model):
    _name = 'cb.lining'
    _description = 'Lining'

    name = fields.Char(string='Name', required=True)
    kode = fields.Char(string='Kode Lining', required=True, copy=False)

    _sql_constraints = [
        ('unique_kode', 'unique(kode)', 'Kode Lining Sudah Ada')
    ]
    
    @api.multi
    def name_get(self):
        result=[]
        for me in self:
            result.append((me.id, "%s - %s" % (me.kode, me.name)))
        return result
    
    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            recs = self.search([
                '|',
                ('kode', operator, name),
                ('name', operator, name),
            ] + args, limit=limit)
        else:
            recs = self.search([] + args, limit=limit)
        return recs.name_get()
