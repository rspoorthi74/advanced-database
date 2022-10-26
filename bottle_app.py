from bottle import default_app, route,template
import sqlite3

connection= sqlite3.connect("Travel_list.db")


@route('/')
def hello_world():
    return 'Hello from Spoorthi!'

@route('/hi')
def hi_world():
    return 'Hi from Spoorthi!'

@route('/bye')
def bye_world():
    return 'Bye from Spoorthi!'

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from list")
    rows = list(rows)
    rows = [ {'id':row[0] , 'desc':row[1]} for row in rows]
    return template("Travel_list.tpl",name="Spoorthi",Travel_list=rows)



application =  default_app()