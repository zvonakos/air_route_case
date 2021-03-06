import flask

from flask import Flask, request


app = Flask(__name__)

examples = [
    "01-create-route",
    "02-get-route",
    "03-update-route",
    "04-delete-route",
    "05-retrieve-routes",
]


@app.route("/")
def show_list():  # just a list of endpoints on home page
    """
    The list of available functions
    """
    body = ""
    for example in examples:
        body += f'<a href="/{example}">{example}</a><br>'
    return body


@app.route("/<example>", methods=["GET", "POST"])
def run_example(example=None):
    """
    The function responsible to launch main function of python files
    whose names are in the list examples mentioned above
    """

    data = request.args if not request.get_json() else request.get_json()
    # I know I could validate between types of requests POST or GET
    # when executing function but I think it is also legit and convenient

    if example not in examples:
        flask.abort(404, "Example does not exist")
    return __import__(example).main(data)  # did in such way cause I didn't want to make additional view functions


if __name__ == "__main__":
    app.debug = True
    app.run()
