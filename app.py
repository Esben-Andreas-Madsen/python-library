from flask import Flask, render_template, request, redirect, url_for

from services.book_author_service import BookAuthorService
from services.book_service import BookService
from services.author_service import AuthorService
from services.population_service import PopulationService

app = Flask(__name__)

# services
book_service = BookService()
author_service = AuthorService()
library_service = BookAuthorService()
population_service = PopulationService()

# add dummy data if db is empty
if not book_service.get_all_books():
    population_service.populate_sample_data()

@app.route('/')
def index():
    return render_template("index.html")

#########################
# ----- Book routes -----
#########################

@app.route('/books/create', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        title = request.form['title']
        published_year = request.form.get('published_year', None)
        isbn = request.form.get('isbn', None)
        pages = request.form.get('pages', None)
        language = request.form.get('language', None)
        created_book = book_service.create_book(title, published_year, isbn, pages, language)
        return redirect(url_for('view_book', book_id=created_book.id))
    else:
        return render_template("create_book.html")
    
@app.route('/books/<int:book_id>')
def view_book(book_id):
    book = book_service.get_book_by_id(book_id)
    if not book:
        return "Book not found", 404
    book.authors = library_service.get_authors_for_book(book.id)
    all_authors = author_service.get_all_authors()
    return render_template("view_book.html", book=book, all_authors=all_authors)

@app.route('/books')
def book_list():
    books = book_service.get_all_books()
    for book in books:
        book.authors = library_service.get_authors_for_book(book.id)
    return render_template("book_list.html", books=books)

@app.route('/books/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book_service.delete_book(book_id)
    return redirect(url_for('book_list'))

@app.route('/books/<int:book_id>/edit', methods=['GET', 'POST'])
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
        return redirect(url_for('view_book', book_id=book.id))
    else:
        return render_template("edit_book.html", book=book)
    
##########################
# ---- Author routes -----
##########################

@app.route('/author/create', methods=['GET', 'POST'])
def create_author():
    if request.method == 'POST':
        name = request.form['name']
        birth_year = request.form.get('birth_year', None)
        created_author = author_service.create_author(name, birth_year)
        return redirect(url_for('view_author', author_id=created_author.id))
    else:
        return render_template("create_author.html")
    
@app.route('/authors/<int:author_id>')
def view_author(author_id):
    author = author_service.get_author_by_id(author_id)
    if not author:
        return "Author not found", 404
    author.books = library_service.get_books_for_author(author.id)
    all_books = book_service.get_all_books()
    return render_template("view_author.html", author=author, all_books=all_books)

@app.route('/authors')
def author_list():
    authors = author_service.get_all_authors()
    for author in authors:
        author.books = library_service.get_books_for_author(author.id)
    return render_template("author_list.html", authors=authors)

@app.route('/authors/<int:author_id>/delete', methods=['POST'])
def delete_author(author_id):
    author_service.delete_author(author_id)
    return redirect(url_for('author_list'))

@app.route('/authors/<int:author_id>/edit', methods=['GET', 'POST'])
def edit_author(author_id):
    author = author_service.get_author_by_id(author_id)
    if not author:
        return "Author not found", 404
    if request.method == 'POST':
        author.name = request.form['name']
        author.birth_year = request.form.get('birth_year', None)
        author_service.update_author(author)
        return redirect(url_for('view_author', author_id=author.id))
    else:
        return render_template("edit_author.html", author=author)

###########################
# -- Book-Author routes -----
###########################

# attach books to authors
@app.route('/authors/link', methods=['GET', 'POST'])
def link_author_book():
    if request.method == 'POST':
        book_id = int(request.form['book_id'])
        author_id = int(request.form['author_id'])
        library_service.add_author_to_book(book_id, author_id)
        return redirect(url_for('book_list'))
    else:
        # quesionable approach with a larger database
        books = book_service.get_all_books()
        authors = author_service.get_all_authors()
        return render_template("link_author_book.html", books=books, authors=authors)

# remove author from book
@app.route('/authors/remove', methods=['GET', 'POST'])
def remove_author_book():
    if request.method == 'POST':
        book_id = int(request.form['book_id'])
        author_id = int(request.form['author_id'])
        library_service.remove_author_from_book(book_id, author_id)
        return redirect(url_for('book_list'))
    else:
        books = book_service.get_all_books()
        authors = author_service.get_all_authors()
        return render_template("remove_author_book.html", books=books, authors=authors)

if __name__ == '__main__':
    app.run(debug=True)
