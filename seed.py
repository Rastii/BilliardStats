from BilliardStats import app, models

with app.app_context():
    models.db.drop_all()
    models.db.create_all()

    user1 = models.User('Bacon')
    user2 = models.User('Veggie')
    models.db.session.add(user1)
    models.db.session.add(user2)

    models.db.session.flush()

    game = models.Game(winning_user_id=user1.id, loser_user_id=user2.id)
    models.db.session.add(game)

    models.db.session.commit()

