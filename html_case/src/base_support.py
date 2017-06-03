from bottle import request
from jinja2 import Environment,FileSystemLoader
env = Environment(loader = FileSystemLoader('../tpl'))

def get_template(file):
	return env.get_template(file)