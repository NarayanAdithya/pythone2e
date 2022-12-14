from app.home import home


@home.route('/', methods=['GET'])
def home():
    return "Flask Website Running Successfully"
