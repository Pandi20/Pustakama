# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, URL
from flask_pagedown.fields import PageDownField
from flask_wtf.file import FileField, FileAllowed
from app import avatars


class EditProfileForm(FlaskForm):
    name = StringField(u'Nama Lengkap', validators=[DataRequired(message=u"Lupa mengisi item ini!"), Length(1, 64, message=u"Panjangnya 1 hingga 64 karakter")])
    major = StringField(u'主修专业', validators=[Length(0, 128, message=u"长度为0到128个字符")])
    headline = StringField(u'一句话介绍自己', validators=[Length(0, 32, message=u"长度为32个字符以内")])
    about_me = PageDownField(u"个人简介")
    submit = SubmitField(u"Simpan perubahan")


class AvatarEditForm(FlaskForm):
    avatar_url = StringField('', validators=[Length(1, 100, message=u"
Panjangnya dibatasi hingga 100 karakter"), URL(message=u"Silakan isi URL dengan benar")])
    submit = SubmitField(u"Simpan")


class AvatarUploadForm(FlaskForm):
    avatar = FileField('', validators=[FileAllowed(avatars, message=u"Hanya diperbolehkan mengunggah gambar")])
