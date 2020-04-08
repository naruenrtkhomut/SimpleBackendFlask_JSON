from os import environ
from SimpleBackendFlask_JSON import app

if __name__ == '__main__':
    HOST = environ.get('HOST', 'localhost')
    try:
        PORT = int(environ.get('PORT', 8080))
    except ValueError:
        PORT = 8080
    app.run(HOST, PORT)