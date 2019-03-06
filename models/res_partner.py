from odoo import api, fields, models, _


class res_partner(models.Model):
    _inherit = "res.partner"

    montir = fields.Boolean(string="Montir")
    kustomer = fields.Boolean(string="Customer")
    kode = fields.Char(string="Kode", default="/")
    name = fields.Char(string="Nama")
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    nama_pekerjaan = fields.Char(string='Nama Pekerjaan')
    pekerjaan = fields.Selection([
        ('pelajar_mhs','Pelajar/Mahasiswa'),
        ('pegawai_negeri','Pegawai Negeri'),
        ('swasta','Swasta'),
        ('lain','Lain-Lain'),
    ], string='Pekerjaan')
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('laki', 'Laki-Laki'), ('perempuan', 'Perempuan'),])

    _sql_constraints = [
        ('unique_kode', 'unique(kode,name)', 'Kombinasi Kode dan nama sudah ada, mohon di cek kembali'),
    ]

    @api.model
    def create(self, values):
        # Add code here
        if values.get('kustomer', False):
            values['kode'] = self.env['ir.sequence'].get_sequence('Kode Customer','res.partner','CSTR')
        elif values.get('montir', False) and ('kode' not in values or values.get('kode', False) == '/'):
            values['kode'] = self.env['ir.sequence'].get_sequence('Kode Montir','res.partner', 'MNTR')
        return super(res_partner, self).create(values)
    
    