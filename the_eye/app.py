from the_eye.settings import app, db

@app.route('/', methods=['GET'])
def index() -> str:
    try:
        db.session.query('SELECT version()')
        return '<h1>Every thing works fine!</h1>'
    except:
        return '<h1>Could not connect with database</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
