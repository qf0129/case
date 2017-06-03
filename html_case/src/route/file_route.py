from bottle import route,static_file


@route('/css/<filename:re:.*\.css>')
def css_file(filename):
    return static_file(filename, root='../res/css/')

@route('/js/<filename:re:.*\.js>')
def js_file(filename):
    return static_file(filename, root='../res/js/')

@route('/img/<filename:re:.*\.png|.*\.jpg|.*\.gif>')
def img_file(filename):
    return static_file(filename, root='../res/img/')