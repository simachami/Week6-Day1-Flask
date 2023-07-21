from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, SignUpForm
from app.models import User

@app.route('/')
def home_page():
    recipe_posts = {
        'titles': {
            'pasta':['We are making a pasta'],
            'sauce': ['make a pasta sauce']
        },
        'foods':{ food:[f'as item {num}'] for num, food in enumerate(['tomato','basil','garlic','veggie'])}
    }
    print(recipe_posts['foods'])
    return render_template('index.jinja', titles=recipe_posts['titles'], foods=recipe_posts['foods'], title='Pinch of Yum')


@app.route('/recipes')
def recipe():
    recipe = {
        'title': 'Pasta Carbonara',
        'ingredients': ['pasta', 'bacon', 'eggs', 'cheese'],
        'instructions': [ 'Cook pasta','fry bacon', 'beat eggs', 'mix all together', 'add cheese', 'enjoy!']
    }
    return render_template('recipe.jinja', recipe=recipe)


@app.route('/signin', methods=['Get', 'POST'])
def sign_in():
    signin_form = LoginForm()
    if signin_form.validate_on_submit():
        email = signin_form.email.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(signin_form.password.data):
            flash(f'{signin_form.email.data} successfully logged in!' ,category='success')
            return redirect('/')
        else:
            flash(f'Invalid User Info, Please try again!', category='alert')
    return render_template('signin.jinja', form=signin_form)

@app.route('/signup', methods=['Get', 'POST'])
def sign_up():
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        first_name = signup_form.first_name.data
        last_name = signup_form.last_name.data
        username = signup_form.username.data
        email = signup_form.email.data
        try:
            user = User(first_name=first_name, last_name=last_name, username=username, email=email)
            user.hash_password(signup_form.password.data)
            user.commit()
            flash(f'{first_name if first_name else username} is registered', category='success')
            return redirect('/')
        except:
            flash(f'Username or Email is already taken. Please try again!', category='alert')
    return render_template('signup.jinja', form=signup_form)

