from app import db, Users, Person

db.drop_all()
db.create_all()

test_user = Users(first_name='Groot', last_name='Toot')
db.session.add(test_user)
db.session.commit()
