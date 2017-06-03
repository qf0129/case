cd src
gunicorn -w 1 -k gevent -b 127.0.0.1:5000 startup:app
