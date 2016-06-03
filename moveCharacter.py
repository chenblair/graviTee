# Python Cocos2d Game Development
# Part 1: Getting Started

# Tutorial: http://jpwright.net/writing/python-cocos2d-game-1/
# Github: http://github.com/jpwright/cocos2d-python-tutorials

# Jason Wright (jpwright0@gmail.com)


# Imports

import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director

# Player class

class Player1(actions.Move):
  
  # step() is called every frame.
  # dt is the number of seconds elapsed since the last call.
  def step(self, dt):
    
    super(Player1, self).step(dt) # Run step function on the parent class.
    
    # Determine velocity based on keyboard inputs.
    velocity_x = 100 * (keyboard[key.RIGHT] - keyboard[key.LEFT])
    velocity_y = 100 * (keyboard[key.UP] - keyboard[key.DOWN])
    
    # Set the object's velocity.
    self.target.velocity = (velocity_x, velocity_y)
    
class Player2(actions.Move):
  
  # step() is called every frame.
  # dt is the number of seconds elapsed since the last call.
  def step(self, dt):
    
    super(Player2, self).step(dt) # Run step function on the parent class.
    
    # Determine velocity based on keyboard inputs.
    velocity_x = 100 * (keyboard[key.D] - keyboard[key.A])
    velocity_y = 100 * (keyboard[key.W] - keyboard[key.S])
    
    # Set the object's velocity.
    self.target.velocity = (velocity_x, velocity_y)
    
# Main class

def main():
  global keyboard # Declare this as global so it can be accessed within class methods.
  
  # Initialize the window.
  director.init(width=500, height=300, do_not_scale=True, resizable=True)
  
  # Create a layer and add a sprite to it.
  player_layer = layer.Layer()
  player1 = sprite.Sprite('ball.jpg')
  player_layer.add(player1)
  
  player2 = sprite.Sprite('ball.jpg')
  player_layer.add(player2)
  
  # Set initial position and velocity.
  player1.position = (100, 100)
  player1.velocity = (0, 0)
  
  player2.position = (300, 100)
  player2.velocity = (0, 0)
  
  # Set the sprite's movement class.
  player1.do(Player1())
  player2.do(Player2())

  # Create a scene and set its initial layer.
  main_scene = scene.Scene(player_layer)

  # Attach a KeyStateHandler to the keyboard object.
  keyboard = key.KeyStateHandler()
  director.window.push_handlers(keyboard)

  # Play the scene in the window.
  director.run(main_scene)

if __name__ == '__main__':
    main()