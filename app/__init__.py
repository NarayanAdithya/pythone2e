from flask import Flask
import config
import os

app: Flask = Flask(__name__)
app.config.from_object(
                        config.Development
                        if
                        os.environ.get('ENVIRONMENT') == 'Development'
                        else
                        config.Production
                        )

# Blueprint Registrations
from app.home import home


app.register_blueprint(home, url_prefix='')
