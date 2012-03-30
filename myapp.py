from flask import Flask, request
from flask.ext.celery import Celery


def create_app():
    return Flask("myapp")

app = create_app()
app.config.from_pyfile('settings_run.py')
celery = Celery(app)


@celery.task(name="myapp.add")
def add(x, y):
    return x + y


@app.route("/")
def hello_world(x=16, y=16):
    x = int(request.args.get("x", x))
    y = int(request.args.get("y", y))
    res = add.apply_async((x, y))
    context = {"id": res.task_id, "x": x, "y": y}
    return """Hello world: \
                add(%(x)s, %(y)s) = \
                <a href="/result/%(id)s">%(id)s</a>""" % context


@app.route("/result/<task_id>")
def show_result(task_id):
    retval = add.AsyncResult(task_id).get(timeout=1.0)
    return repr(retval)


if __name__ == "__main__":
  app.run(host="127.0.0,1", port=3000,debug=True)
