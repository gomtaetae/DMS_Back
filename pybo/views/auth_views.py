from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import Users

bp = Blueprint('auth', __name__, url_prefix='/auth')

# 회원가입 폼 입력받기
@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        users = Users.query.filter_by(users_name=form.users_name.data).first()
        if not users:
            users = Users(
                nickname=form.nickname.data,
                users_name=form.users_name.data,
                password=generate_password_hash(form.password1.data),
                email=form.email.data,
                users_birth=form.users_birth.data,
                users_phone=form.users_phone.data,
                address_main=form.address_main.data,
                address_sub=form.address_sub.data
                )
            db.session.add(users)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

# 로그인 폼
@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = Users.query.filter_by(email=form.email.data).first()
        if not user:
            error = "존재하지 않는 이메일입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['users_id'] = user.users_id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)

# 로그인 여부 확인
@bp.before_app_request
def load_logged_in_user():
    users_id = session.get('users_id')
    if users_id is None:
        g.user = None
    else:
        g.user = Users.query.get(users_id)

# 로그아웃 라우팅
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))