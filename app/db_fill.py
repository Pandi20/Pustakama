# -*- coding: utf-8 -*-

from app import app, db
from app.models import User, Book, Log, Role

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'root', email='root@gmail.com', password='password', major='administrator',
             headline=u"Pustakawan", about_me=u"Akulah sang penjaga pengetahuan.")
user1 = User(name=u'Hadi Sopandi', email='202151038@student.unsil.ac.id', password='123456', major='Pendidikan Matematika', headline=u"Kusuka buku")
user2 = User(name=u'test', email='test@test.com', password='123456')
user3 = User(name=u'Cantika', email='xiaoming@163.com', password='123456')
user4 = User(name=u'Putri', email='lihua@yahoo.com', password='123456')

book1 = Book(title=u"Flask Web", subtitle=u"PythonWeb", author=u"Miguel Grinberg", isbn='9787115373991',
             tags_string=u",Web", image='http://img3.douban.com/lpic/s27906700.jpg',
             summary=u"""Kitu we""")
book2 = Book(title=u"STL", subtitle=u"Standar", author=u"Nakama", isbn='9787560926995',
             tags_string=u"Gurita,Antropologi,C++", image='https://m.media-amazon.com/images/I/71XnOuGlPnL._SY466_.jpg',
             summary=u"""apa hayo""")
book3 = Book(title=u"Aku cinta keduanya", subtitle=u"meraih cinta",
             author="Alfred V. Aho / Monica S.Lam / Ravi Sethi / Jeffrey D. Ullman ", isbn="9787111251217",
             tags_string=u"Cinta,berdua", image='http://img3.douban.com/lpic/s3392161.jpg',
             summary=u"""* apa ya""")
book4 = Book(title=u"Vandaloriema", author="Randal E.Bryant / David O'Hallaron", isbn="9787111321330",
             tags_string=u"raki,vandelor", image='http://img3.douban.com/lpic/s4510534.jpg',
             summary=u"""* Yuk makan dulu""")
book5 = Book(title=u"Algoritma dasar", subtitle=u"cara mudah", author=u"Joseph Albahari/ Ben Albahari",
             isbn="9787517010845", tags_string=u"problem,algoritma,C#", image='http://img3.douban.com/lpic/s28152290.jpg',
             summary=u"""cek satu kan""")
book6 = Book(title=u"Matematika Murni",
             author="Thomas H.Cormen / Charles E.Leiserson / Ronald L.Rivest / Clifford Stein",
             isbn="9787111187776", tags_string=u"Matematika,dasar", image='http://img3.doubanio.com/lpic/s1959967.jpg',
             summary=u"matematika untuk anda saja")
logs = [Log(user1, book2), Log(user1, book3), Log(user1, book4), Log(user1, book6),
        Log(user2, book1), Log(user2, book3), Log(user2, book5),
        Log(user3, book2), Log(user3, book5)]

db.session.add_all([admin, user1, user2, user3, user4, book1, book2, book3, book4, book5, book6] + logs)
db.session.commit()

app_ctx.pop()
