@app.route('/', methods=["GET", "POST"])
def home():
    users = None
    if request.form:
        try:
            user = User(email=request.form.get(''))
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print("Failed to add book")
            print(e)
    books = User.query.all()
    return render_template("home.html", books=books)


@app.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = User.query.filter_by(email=oldtitle).first()
        book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get('email')
    book = User.query.filter_by(email=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
