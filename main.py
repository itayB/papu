from bottle import abort, request, response, Bottle, static_file, redirect
import logging

logger = logging.getLogger(__name__)


def post_first():
    logger.info("got first message")
    
    logger.info(str(request.forms))
    return request.forms


def setup_routing(app):
    app.route('/api/v1/first', 'POST', post_first)


app = Bottle()
setup_routing(app)


def main():
    app.run(host='0.0.0.0', port=80, debug=False)


if __name__ == "__main__":
    main()

