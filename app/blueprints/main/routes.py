from flask import render_template, g
from . import bp as main


@main.route('/')
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

@main.route('/recipes')
def recipe():
    recipe = {
        'title': 'Pasta Carbonara',
        'ingredients': ['pasta', 'bacon', 'eggs', 'cheese'],
        'instructions': [ 'Cook pasta','fry bacon', 'beat eggs', 'mix all together', 'add cheese', 'enjoy!']
    }
    return render_template('recipe.jinja', recipe=recipe)