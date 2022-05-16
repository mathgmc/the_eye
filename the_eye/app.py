from the_eye.model.partner import Partner
from the_eye.settings import app, db
from the_eye.views.event import event_blueprint


@app.route("/", methods=["GET"])
def index() -> str:
    try:
        db.session.query("SELECT version()")
        return f"<h1>Every thing works fine! {a.name}</h1>"
    except Exception as e:
        return f"<h1>Could not connect with database {e}</h1>"


app.register_blueprint(event_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
