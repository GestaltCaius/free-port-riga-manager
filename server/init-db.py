from app import app, models


users = [
    {
        'email': 'toto.titi@example.com',
        'first_name': 'Toto',
        'last_name': 'Titi',
        'phone': '+331',
        'is_forwarder': False,
        'password': 'hello'
    },
    {
        'email': 'tata.tutu@example.com',
        'first_name': 'Tata',
        'last_name': 'Tutu',
        'phone': '+332',
        'is_forwarder': True,
        'password': 'world'
    }
]


with app.app_context():
    for user in users:
        obj = models.User(**user)
        try:
            obj.add()
        except Exception as e:
            print('Error:', e)
