from flask import Blueprint, render_template, request, redirect, url_for
from app.services.book_author_service import BookAuthorService
from app.services.book_service import BookService
from app.services.author_service import AuthorService
from app.services.population_service import PopulationService

# services
book_service = BookService()
author_service = AuthorService()
library_service = BookAuthorService()
population_service = PopulationService()

routes = Blueprint("routes", __name__, url_prefix="/", template_folder="templates")

@routes.route('/')
def index():
    return render_template("index.html")
#########################
# ----- Book routes -----
#########################
@routes.route('/books/create', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        title = request.form['title']
        published_year = request.form.get('published_year', None)
        isbn = request.form.get('isbn', None)
        pages = request.form.get('pages', None)
        language = request.form.get('language', None)
        created_book = book_service.create_book(title, published_year, isbn, pages, language)
        return redirect(url_for('routes.view_book', book_id=created_book.id))
    else:
        return render_template("create_book.html")
    
@routes.route('/books/<int:book_id>')
def view_book(book_id):
    book = book_service.get_book_by_id(book_id)
    if not book:
        return "Book not found", 404
    book.authors = library_service.get_authors_for_book(book.id)
    all_authors = author_service.get_all_authors()
    return render_template("view_book.html", book=book, all_authors=all_authors)

@routes.route('/books')
def book_list():
    books = book_service.get_all_books()
    for book in books:
        book.authors = library_service.get_authors_for_book(book.id)
    return render_template("book_list.html", books=books)

@routes.route('/books/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book_service.delete_book(book_id)
    return redirect(url_for('routes.book_list'))

@routes.route('/books/<int:book_id>/edit', methods=['GET', 'POST'])
def edit_book(book_id):
    book = book_service.get_book_by_id(book_id)
    if not book:
        return "Book not found", 404
    if request.method == 'POST':
        book.title = request.form['title']
        book.published_year = request.form.get('published_year', None)
        book.isbn = request.form.get('isbn', None)
        book.pages = request.form.get('pages', None)
        book.language = request.form.get('language', None)
        book_service.update_book(book)
        return redirect(url_for('routes.view_book', book_id=book.id))
    else:
        return render_template("edit_book.html", book=book)
    
##########################
# ---- Author routes -----
##########################
@routes.route('/author/create', methods=['GET', 'POST'])
def create_author():
    if request.method == 'POST':
        name = request.form['name']
        birth_year = request.form.get('birth_year', None)
        created_author = author_service.create_author(name, birth_year)
        return redirect(url_for('routes.view_author', author_id=created_author.id))
    else:
        return render_template("create_author.html")
    
@routes.route('/authors/<int:author_id>')
def view_author(author_id):
    author = author_service.get_author_by_id(author_id)
    if not author:
        return "Author not found", 404
    author.books = library_service.get_books_for_author(author.id)
    all_books = book_service.get_all_books()
    return render_template("view_author.html", author=author, all_books=all_books)

@routes.route('/authors')
def author_list():
    authors = author_service.get_all_authors()
    for author in authors:
        author.books = library_service.get_books_for_author(author.id)
    return render_template("author_list.html", authors=authors)

@routes.route('/authors/<int:author_id>/delete', methods=['POST'])
def delete_author(author_id):
    author_service.delete_author(author_id)
    return redirect(url_for('routes.author_list'))

@routes.route('/authors/<int:author_id>/edit', methods=['GET', 'POST'])
def edit_author(author_id):
    author = author_service.get_author_by_id(author_id)
    if not author:
        return "Author not found", 404
    if request.method == 'POST':
        author.name = request.form['name']
        author.birth_year = request.form.get('birth_year', None)
        author_service.update_author(author)
        return redirect(url_for('routes.view_author', author_id=author.id))
    else:
        return render_template("edit_author.html", author=author)
    
###########################
# -- Book-Author routes -----
###########################

# attach books to authors
@routes.route('/authors/link', methods=['GET', 'POST'])
def link_author_book():
    if request.method == 'POST':
        book_id = int(request.form['book_id'])
        author_id = int(request.form['author_id'])
        library_service.add_author_to_book(book_id, author_id)
        return redirect(url_for('routes.book_list'))
    else:
        # quesionable routesroach with a larger database
        books = book_service.get_all_books()
        authors = author_service.get_all_authors()
        return render_template("link_author_book.html", books=books, authors=authors)
# remove author from book

@routes.route('/authors/remove', methods=['GET', 'POST'])
def remove_author_book():
    if request.method == 'POST':
        book_id = int(request.form['book_id'])
        author_id = int(request.form['author_id'])
        library_service.remove_author_from_book(book_id, author_id)
        return redirect(url_for('routes.book_list'))
    else:
        books = book_service.get_all_books()
        authors = author_service.get_all_authors()
        return render_template("remove_author_book.html", books=books, authors=authors)