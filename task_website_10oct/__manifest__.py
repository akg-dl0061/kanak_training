{
    'name': 'Task Website',
    'description': 'Website Task onclick all product and customer name on web page.',
    'category': '',
    'version': '1.1',
    'author': 'Kanak Infosystems LLP.',
    'website': 'http://www.kanakinfosystems.com',
    'depends': ['website','website_sale'],
    'data': [
            # 'security/ir.model.access.csv',
            'views/website.xml',
            
    ],
    'assets': {
        'web.assets_frontend': [
            'task_website_10oct/static/src/css/style.css',
            # 'website_kanak/static/src/css/owl.carousel.min.css',
            # 'website_kanak/static/src/js/custom_website_kanak.js',
            'task_website_10oct/static/src/js/show_result.js',
        ],
    },
    'bootstrap': True,
    'application': True,
    'installable': True,
}
