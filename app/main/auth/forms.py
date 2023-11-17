# -*- coding:utf-8 -*-
from app import db
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import Email, Length, DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"Lupa mengisi item ini!"), Length(1, 64), Email(message=u"Apakah anda yakin ini email yang benar?")])
    password = PasswordField(u'Kata Sandi', validators=[DataRequired(message=u"Lupa mengisi item ini!"), Length(6, 32)])
    remember_me = BooleanField(u"Jangan lupakan saya", default=True)
    submit = SubmitField(u'Masuk')


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"Lupa mengisi item ini!"), Length(1, 64), Email(message=u"Apakah anda yakin ini email yang benar?")])
    name = StringField(u'Nama Lengkap', validators=[DataRequired(message=u"Lupa mengisi item ini!"), Length(1, 64)])
    password = PasswordField(u'Kata Sandi',
                             validators=[DataRequired(message=u"Lupa mengisi item ini!"), EqualTo('password2', message=u'kata sandi harus cocok'),
                                         Length(6, 32)])
    password2 = PasswordField(u'Ulangi Kata Sandi', validators=[DataRequired(message=u"Lupa mengisi item ini!")])
    submit = SubmitField(u'Daftar')

    def validate_email(self, filed):
        if User.query.filter(db.func.lower(User.email) == db.func.lower(filed.data)).first():
            raise ValidationError(u'Email ini telah didaftarkan')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'Kata sandi lama', validators=[DataRequired(message=u"Lupa mengisi item ini!")])
    new_password = PasswordField(u'Kata sandi baru', validators=[DataRequired(message=u"Lupa mengisi item ini!"),
                                                     EqualTo('confirm_password', message=u'kata sandi harus cocok'),
                                                     Length(6, 32)])
    confirm_password = PasswordField(u'Ulangi kata sandi baru', validators=[DataRequired(message=u"Lupa mengisi item ini!")])
    submit = SubmitField(u"Simpan kata sandi")

    def validate_old_password(self, filed):
        from flask_login import current_user
        if not current_user.verify_password(filed.data):
            raise ValidationError(u'Kata sandi lama salah')
