#!/usr/bin/env python3

from bottle import route, run,request

@route('/')
def index():
    name = request.query.name
    age = request.query.age
    if name and age:
        return f'{name} tiene {age} '
    else:
        return "Julian"


if __name__ == "__main__":
    run(host='35.237.215.97', port=80, debug=True,reloader=True)
