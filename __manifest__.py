{
    'name': 'Custom Currency Rate Update',
    'version': '1.0',
    'summary': 'Updates currency rates from custom sources',
    'description': """
        Updates currency rates for GHS, NGN, XAF, etc.
    """,
    'author': 'GUIGUI David',
    'website': 'http://www.guidasworld.com',
    'license': 'AGPL-3',
    'depends': ['currency_rate_update'],
    'external_dependencies': {
        'python': ['requests', 'urllib3'],
    },
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    
}
