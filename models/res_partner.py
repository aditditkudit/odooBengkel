from odoo import api, fields, models, _


class res_partner(models.Model):
    _inherit = "res.partner"

    montir = fields.Boolean(string="Montir")
    customer = fields.Boolean(string="Customer")
    kode = fields.Char(string="Kode", default="/")
    name = fields.Char(string="Nama")
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    pekerjaan = fields.Selection(string='Pekerjaan', selection=[('pelajar_mhs', 'Pelajar/Mahasiswa'), ('pegawai_negri', 'Pegawai Negri'),('swasta','Swasta'),('lain','Lain-Lain')],)
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('laki', 'Laki-Laki'), ('perempuan', 'Perempuan'),])

    _sql_constraint = [
        ('unique_kode', 'unique(kode,name)', 'Kombinasi Kode dan nama sudah ada, mohon di cek kembali'),
    ]

    
    
    
    
    
    
    
    
