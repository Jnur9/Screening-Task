{
    'name': 'Task Module', 
    'summary': 'test Odoo 18 module for odoo specialist job opportunity ',
    'description': '''
        Testing Purpuses.
    ''',
    'version': '18.0.1.0.0',
    'category': 'Productivity',
    'license': 'LGPL-3', 
    'author': 'Jamila',
    'website': 'https://www.linkedin.com/in/jnur9/',
    'depends': [
        'base',
    ],
    'data': [
        
        'security/ir.model.access.csv',
        'views/task_module_views.xml',
        
    ],
    
    'installable': True,
    'application': True,

}