cd src
gunicorn -w 1 -k gevent -b 127.0.0.1:3000 startup:app
