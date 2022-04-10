from bottle import route, run, template, static_file, request
from game import Game
from renderer import Renderer

game = Game(11)
renderer = Renderer(game.world)

@route('/state')
def state():
    return static_file("./world.svg", root = "./")

@route('/insert')
def insert():
    x = int(request.query.x)
    y = int(request.query.y)
    game.placeCurrentTileAt((x,y))
    return "OK"



run(host='localhost', port=8000)