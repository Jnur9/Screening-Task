from odoo import models, fields, api

class TaskModel(models.Model):
    _name = 'task.model'
    _description = 'Task Model'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Role")
    is_active = fields.Boolean(string="Is Active", default=True)
    state = fields.Selection([('draft' , 'Draft'), ('done' , 'Done')], default="draft", string="status")


    def toggle_active(self):
        self.state= "done"
