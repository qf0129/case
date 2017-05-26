from bottle import get, request
from base_support import get_template

@get('/qfdate')
def qfdate():
    tpl = get_template('qfdate.html')
    return tpl.render()


@get('/ip')
def qfdate():
    ip1 = request.remote_addr
    ip2 = request.headers['Host']
    ip3 = request.headers['X-Real-IP']
    ip4 = request.headers['X-Forwarded-For']
    print ip1
    print ip2
    print ip3
    print ip4

    return ip1,ip2,ip3,ip4

