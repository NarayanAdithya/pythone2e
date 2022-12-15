from app.home import home


@home.route('/', methods=['GET'])
def homepage():
    return "Flask Website Running Successfully"


@home.route('/<string:name>', methods=['GET'])
def printname(name):
    return f"Hey {name}"
