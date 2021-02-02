#!/usr/bin/python3

from app import db, Users, Countries, Cities

db.drop_all()
db.create_all()

test_user = Users(first_name='Groot', last_name='Toot')
db.session.add(test_user)
db.session.commit()

UK = Countries(name='United Kingdom')
db.session.add(UK)
db.session.commit()

ldn = Cities(name='London', country=UK)
mcr = Cities(name='Manchester', country=Countries.query.filter_by(name='United Kingdom').first())

db.session.add(ldn)
db.session.add(mcr)
db.session.commit()
