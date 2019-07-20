from flask import Flask

from routes.funcx import funcx_api
from routes.automate import automate_api
from routes.auth import auth_api

from config import SECRET_KEY

application = Flask(__name__)

# Include the API blueprint
application.register_blueprint(funcx_api, url_prefix="/routes/v1")
application.register_blueprint(automate_api, url_prefix="/automate")
application.register_blueprint(auth_api)


@application.route("/")
def home():
    # TODO: Remove this once the GUI is deployed.
    application.logger.debug("FuncX")
    return "funcX"


application.secret_key = SECRET_KEY
application.config['SESSION_TYPE'] = 'filesystem'


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")