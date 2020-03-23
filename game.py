#run game



import map
import Engine

area = map.Map('intro')
game = Engine.Engine(area)
game.play()
