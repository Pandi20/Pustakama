# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, URL
from flask_pagedown.fields import PageDownField
from flask_wtf.file import FileField, FileAllowed
from app import avatars


class EditProfileForm(FlaskForm):
    name = StringField(u'Nama', validators=[DataRequired(message=u"Lupa mengisi item ini!"), Length(1, 64, message=u"Panjangnya hingga 64 karakter")])
    major = StringField(u'Jurusan', validators=[Length(0, 128, message=u"Panjangnya hingga 128 karakter")])
    headline = StringField(u'judul', validators=[Length(0, 32, message=u"Panjangnya hingga 32 karakter")])
    about_me = PageDownField(u"Tentang Saya")
    submit = SubmitField(u"Simpan perubahan")


class AvatarEditForm(FlaskForm):
    avatar_url = StringField('', validators=[Length(1, 100, message=u"Batasi hingga 100 karakter"), URL(message=u"Silakan isi tautan dengan benar")])
    submit = SubmitField(u"Simpan")


class AvatarUploadForm(FlaskForm):
    avatar = FileField('', validators=[FileAllowed(avatars, message=u"Hanya diperbolehkan mengunggah gambar")])
