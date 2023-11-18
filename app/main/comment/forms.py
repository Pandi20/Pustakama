# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length, DataRequired


class CommentForm(FlaskForm):
    comment = TextAreaField(u"Resensi buku anda",
                            validators=[DataRequired(message=u"Wajib diisi"), Length(1, 1024, message=u"Panjang resensi buku dibatasi hingga 1024 karakter")])
    submit = SubmitField(u"Melepaskan")
