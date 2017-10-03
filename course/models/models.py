# -*- coding: utf-8 -*-

from odoo import models, fields, api

class course(models.Model):
    _name = 'course.course'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    reference_ids = fields.One2many('student.reference.course', 'reference_id',
                                    'References')

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
        
        
class StudentReference(models.Model):
    ''' Defining a student reference information '''
    _name = "student.reference.course"
    _description = "Student Reference"

    reference_id = fields.Many2one('course.course', 'Student')
    description = fields.Many2one('res.partner', 'user')
    name = fields.Char('First Name', required=True)
    middle = fields.Char('Middle Name', required=True)
    last = fields.Char('Surname', required=True)
    designation = fields.Char('Designation', required=True)
    phone = fields.Char('Phone', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              'Gender')