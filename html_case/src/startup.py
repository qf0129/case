
from bottle import Bottle,debug
app = Bottle()

with app:
	# import route.file_route
	# import route.index_route
	from route.routes import *


debug(True)
# app.run(reloader=True,host='192.168.1.9', port=8080)
# app.run(host='0.0.0.0', port=9000)