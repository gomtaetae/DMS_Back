from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

# 회원가입 폼
class UserCreateForm(FlaskForm):
    nickname = StringField(
        '아이디',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    users_name = StringField(
        '사용자 이름',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    password1 = PasswordField(
        '비밀번호',
        validators=[
            DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')]
    )
    password2 = PasswordField(
        '비밀번호확인',
        validators=[DataRequired()]
    )
    email = EmailField(
        '이메일',
        validators=[DataRequired(), Email()]
    )
    users_birth = StringField(
        '생년월일',
        validators=[DataRequired(), Length(min=8, max=8, message='생년월일은 8자리여야 합니다. ex)19961020')]
    )
    users_phone = StringField(
        '전화번호',
        validators=[DataRequired(), Length(min=10, max=15)]  # 전화번호 형식에 맞춰 길이를 조정하세요.
    )
    address_main = StringField(
        '주소',
        validators=[DataRequired()]
    )
    address_sub = StringField(
        '상세주소',
        validators=[DataRequired()]
    )

# 로그인폼
class UserLoginForm(FlaskForm):
    email = StringField('사용자 이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])