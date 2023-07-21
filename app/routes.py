from flask import render_template
from app import app
from app.forms import LoginForm, SignUpForm

@app.route('/')
def home_page():
    recipe_posts = {
        'titles': {
            'pasta':['We are making a pasta'],
            'sauce': ['make a pasta sauce']
        },
        'foods':{ food:[f'as item {num}'] for num, food in enumerate(['pasta','chicken','tomato','veggies'])}
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


@app.route('/signin')
def sign_in():
    signin_form = LoginForm()
    return render_template('signin.jinja', form=signin_form)

@app.route('/signup')
def sign_up():
    signup_form = SignUpForm()
    return render_template('signup.jinja', form=signup_form)

