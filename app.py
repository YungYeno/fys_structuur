from flask import Blueprint, render_template, Flask
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', flightnumber=current_user.flightnumber, email=current_user.email,
                           seatnumber=current_user.seatnumber)


if __name__ == "__main__":
    main.run()
