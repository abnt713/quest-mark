__author__ = 'alisonbnt'

#!venv/bin/python
__author__ = 'alisonbento'

from app import api, manager
from conf.routes import Routes

Routes.load_routes(api)

if __name__ == '__main__':
    manager.run()
    # app.run(host='0.0.0.0', port=config.APP_PORT, debug=config.APP_DEBUG)
