from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def progress_tracker():
    return render_template('index.html')


@app.get('/sign-up/')
def get_signup():
    return render_template('signup.html')


@app.post('/sign-up/')
def post_signup():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    terms = request.form.get('terms')

    return redirect(url_for('get_login'))


@app.get('/sign-in/')
def get_login():
    return render_template('signin.html')


@app.post('/sign-in/')
def post_login():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    return redirect(url_for('profile'))


@app.route('/profile/')
def profile():
    return render_template('profile.html')


@app.route('/profile-settings/')
def profile_settings():
    return render_template('profile-settings.html')


@app.route('/update-username/')
def profile_username():
    return render_template('profile-username.html')


@app.route('/update-avatar/')
def profile_avatar():
    return render_template('profile-avatar.html')


@app.post('/update-username/')
def update_username():
    username = request.form.get('username')
    password = request.form.get('password')

    return redirect(url_for('profile_settings'))


@app.post('/update-avatar/')
def update_avatar():
    avatar = request.form.get('avatar')
    return redirect(url_for('profile_settings'))

@app.route('/verification/')
def verification():
    return render_template('verification.html')


@app.route('/terms/')
def get_terms():
    return render_template('terms.html')


@app.get('/authors/')
def authors():
    return render_template('authors.html')


if __name__ == '__main__':
    app.run(debug=True)