from flask import Flask
from flask_mail import Mail
from config import Config
from libs.database import init_db

def create_app():
    """App factory function"""

    app = Flask(__name__)
    app.config_class = Config

    Mail(app)
    init_db(app)

    from apps.account import account as account_app
    app.register_blueprint(account_app, url_prefix='/account')

    from apps.admin import admin as admin_app
    app.register_blueprint(admin_app, url_prefix='/admin')

    from apps.model import model as model_app
    app.register_blueprint(model_app, url_prefix='/model')

    from apps.portfolio import portfolio as portfolio_app
    app.register_blueprint(portfolio_app, url_prefix='/portfolio')

    from apps.trade import trade as trade_app
    app.register_blueprint(trade_app, url_prefix='/trade')

    return app

app = Flask(__name__)
# app = create_app()