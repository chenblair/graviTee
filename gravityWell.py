# Python Cocos2d Game Development
# Part 1: Getting Started

# Tutorial: http://jpwright.net/writing/python-cocos2d-game-1/
# Github: http://github.com/jpwright/cocos2d-python-tutorials

# Jason Wright (jpwright0@gmail.com)


# Imports

from random import randint

import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director

# Player class
global prevVelocity_y,prevVelocity_x;

class Me(actions.Move):
    prevVelocity_x = 0
    prevVelocity_y = 0
  
  # step() is called every frame.
  # dt is the number of seconds elapsed since the last call.
    def step(self, dt):
    
        super(Me, self).step(dt) # Run step function on the parent class.
        myX = me.position[0]
        myY = me.position[1]
        aX = anchor.position[0] 
        aY = anchor.position[1]
    
        graviX = 10000/((-myX+aX)*abs(myX-aX))
        graviY = 10000/((-myY+aY)*abs(myY-aY))
    
        # Determine velocity based on keyboard inputs.
        velocity_x = self.prevVelocity_x+graviX
        velocity_y = self.prevVelocity_y+500 * (keyboard[key.UP] - keyboard[key.DOWN])+graviY
    
        self.prevVelocity_x = velocity_x
        self.prevVelocity_y = velocity_y
    
        # Set the object's velocity.
        self.target.velocity = (velocity_x, velocity_y)
    
# Main class

def main():
  global keyboard,myX,myY,aX,aY,me,anchor # Declare this as global so it can be accessed within class methods.
  
  # Initialize the window.
  director.init(width=500, height=300, do_not_scale=True, resizable=True)
  
  prevVelocity_x = 200
  prevVelocity_y = 0
  
  # Create a layer and add a sprite to it.
  player_layer = layer.Layer()
  me = sprite.Sprite('ball.jpg')
  player_layer.add(me)
  
  anchor = sprite.Sprite('ball.jpg')
  player_layer.add(anchor)
  
  # Set initial position and velocity.
  me.position = (0, randint(0,200))
  me.velocity = (0, 0)
  
  anchor.position = (100,100)
  
  # Set the sprite's movement class.
  me.do(Me())

  # Create a scene and set its initial layer.
  main_scene = scene.Scene(player_layer)

  # Attach a KeyStateHandler to the keyboard object.
  keyboard = key.KeyStateHandler()
  director.window.push_handlers(keyboard)

  # Play the scene in the window.
  director.run(main_scene)

if __name__ == '__main__':
    main()