from BillardStats import app, models

with app.app_context():
    models.db.drop_all()
    models.db.create_all()

    user1 = models.User('Bacon')
    user2 = models.User('Veggie')

    game1 = models.Game(user1, user2)

    models.db.session.add(user1)
    models.db.session.add(user2)
    models.db.session.add(game1)

    models.db.session.commit()
