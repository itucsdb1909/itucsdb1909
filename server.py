# Anthology app
# Developed by Mehmet Gencay Ertürk

from flask import Flask, render_template, request, url_for,redirect
from flask_bootstrap import Bootstrap
from flask_login import login_user,LoginManager
from forms import *
from config import Config
from db_table_operations import *
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
login = LoginManager(app)
from models import User, Book, Poem
@app.route("/")
def home_page():
    initialize()
    return render_template("homepage.html")


@app.route('/mylists', methods=['GET', 'POST'])
def mylists_page():
    user_poems = userlist_get_poems()
    user_books = userlist_get_book()

    if request.method == 'POST':
        poem_id = request.form['poem_id']
        user_id = request.form['user_id']
        book_id = request.form['book_id']

        if poem_id != "0":  # request to delete poem
            userlist_delete_book(user_id, poem_id)
            print("delete poem with id " + poem_id)
            return redirect('/mylists')

        elif book_id != "0":  # request to delete book
            userlist_delete_book(user_id, book_id)
            return redirect('/mylists')

    return render_template("mylists.html",
                           user_poems=user_poems,
                           user_books=user_books)


@app.route('/mylists/books', methods=['GET', 'POST'])
def books_page():
    books = get_books()

    if request.method == 'POST':
        book_id = request.form['book_id']
        user_id = request.form['user_id']
        userlist_add_book(user_id, book_id)
        return redirect(url_for('/mylists')))

    return render_template("books.html", books=sorted(books))


@app.route('/mylists/books/add', methods=['GET', 'POST'])
def books_add_page():
    form = bookAddForm(request.form)
    if request.method == 'POST' and form.validate():
        book = book(form.name.data, form.author.data, form.number_of_pages.data,
                      form.publisher.data, form.category.data)
        insert_book(book)
        return redirect('/mylists/books')

    return render_template("add_books.html", form=form)


@app.route('/mylists/books/update', methods=['GET', 'POST'])
def books_update_page():
    form = bookUpdateForm(request.form)
    if request.method == 'POST' and form.validate():
        book = book(form.name.data, form.author.data, form.number_of_pages.data,
                      form.publisher.data, form.category.data)
        book_id = form.id.data  # which book to update
        update_book(book_id, book)
        return redirect('/mylists/books')
    return render_template("update_books.html", form=form)
#
#
@app.route('/mylists/books/delete', methods=['GET', 'POST'])
def books_delete_page():
    form = bookDeleteForm(request.form)
    id = form.book_id.data
    if id.__len__() > 0:
        delete_book(id)
        return redirect('/mylists/books')
    return render_template("delete_books.html", form=form)


@app.route('/mylists/poems', methods=['GET', 'POST'])
def poems_page():
    poems = get_poems()

    if request.method == 'POST':
        poem_id = request.form['poem_id']
        user_id = request.form['user_id']
        userlist_add_poem(user_id, poem_id)
        return redirect('/mylists')

    return render_template("poems.html", poems=sorted(poems))

@app.route('/mylists/poems/add', methods=['GET', 'POST'])
def poems_add_page():
    form = poemAddForm(request.form)
    if request.method == 'POST' and form.validate():
        poem = poem(form.title.data, form.year.data, form.content.data,
                      form.author.data, form.category.data)
        insert_poem(poem)
        return redirect('/mylists/poems')
    return render_template("add_poems.html", form=form)


@app.route('/mylists/poems/update', methods=['GET', 'POST'])
def poems_update_page():
    form = poemUpdateForm(request.form)
    if request.method == 'POST' and form.validate():
        poem = poem(form.title.data, form.year.data, form.content.data,
                      form.author.data, form.category.data)
        poem_id = form.id.data  # which poem to update
        update_poem(poem_id, poem)
        return redirect('/mylists/poems')

    return render_template("update_poems.html", form=form)


@app.route('/mylists/poems/delete', methods=['GET', 'POST'])
def poems_delete_page():
    form = poemDeleteForm(request.form)
    id = form.poem_id.data
    if id.__len__() > 0:
        delete_poem(id)
        return redirect('/mylists/poems')
    return render_template("delete_poems.html", form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin_page():
    form = LoginForm()
    if form.validate_on_submit():
        found_user = find_user_by_username(form.username.data)
        user = User(found_user[1], found_user[2], found_user[3], found_user[4],
                    found_user[5], found_user[6], found_user[7])
        user.set_id(found_user[0]) # to load user id
        if user is None or not check_password(user.password, form.password.data):
            print("User signing failed")
            return redirect('/signin')
        login_user(user, remember=form.remember_me.data)
        print("User signed successfully")
        return redirect(url_for('/mylists')))
    return render_template("signin.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.name.data, form.surname.data, form.email.data,
                    form.password.data, form.age.data, form.gender.data)
        insert_user(user)
        return redirect(url_for('/mylists')))

    return render_template("signup.html", form=form)


if __name__ == "__main__":
    app.run()
