from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from libs.db import db
from libs import config
from user.views import user_bp

# 初始化app
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# 初始化DB迁移模块
migrate = Migrate(app,db)
migrate.init_app(app)

#初始化命令行管理工具
manager = Manager(app)
manager.add_command('db',MigrateCommand)

app.register_blueprint(user_bp)

if __name__ == '__main__':
    manager.run()
