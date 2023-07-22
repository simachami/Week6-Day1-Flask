from flask import render_template, redirect, flash, url_for, g 
from flask_login import current_user
from app import app
from app.forms import RecipeForm, RecipeSearchForm
from app.models import User, Recipe
from . import bp


@app.before_request
def before_request():
    g.recipe_search_form = RecipeSearchForm()
    g.recipe_form = RecipeForm()


@bp.post('/post')
def post():
    if g.recipe_form.validate_on_submit():
        post = Recipe(body=g.recipe_form.body.data, user_id = current_user.user_id)
        post.commit()
        flash('Recipe posted!', category='success')
    return redirect(url_for('social.profile', username = current_user.username))

@bp.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user:
        recipes = user.recipes
        return render_template('profile.jinja', username=username, recipes=recipes)
    else:
        flash(f'User: {username} is not valid!', category='warning')
        return redirect(url_for('main.home'))
    
@bp.post('user-search')
def user_search():
    return redirect(url_for('social.profile', username=g.recipe_search_form.username.data))

