from bottle import get
from base_support import get_template

@get('/qfdate')
def qfdate():
    tpl = get_template('qfdate.html')
    return tpl.render()

