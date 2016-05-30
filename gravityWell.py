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
from math import sqrt

# Player class
global prevVelocity_y,prevVelocity_x;

class Me(actions.Move):
    prevVelocity_x = 10
    prevVelocity_y = 0
  
  # step() is called every frame.
  # dt is the number of seconds elapsed since the last call.
    def step(self, dt):
    
        super(Me, self).step(dt) # Run step function on the parent class.
        G=100.0
        myX = me.position[0]
        myY = me.position[1]
        velocity_x = self.prevVelocity_x
        velocity_y = self.prevVelocity_y+500 * (keyboard[key.UP] - keyboard[key.DOWN])
        for i in range(numAnchors) :
            aX = anchors[i].position[0] 
            aY = anchors[i].position[1]
            dist=sqrt((myX-aX)**2+(myY-aY)**2)
            graviX = G*-(myX-aX)/(dist**2)
            graviY = G*-(myY-aY)/(dist**2)
    
            # Determine velocity based on keyboard inputs.
            velocity_x += graviX
            velocity_y += graviY
    
        self.prevVelocity_x = velocity_x
        self.prevVelocity_y = velocity_y
    
        # Set the object's velocity.
        self.target.velocity = (velocity_x, velocity_y)
        print(velocity_x,velocity_y)
    
# Main class

def main():
  global keyboard,myX,myY,aX,aY,me,anchors,numAnchors # Declare this as global so it can be accessed within class methods.
  
  # Initialize the window.
  director.init(width=500, height=300, do_not_scale=True, resizable=True)
  
  prevVelocity_x = 200
  prevVelocity_y = 0
  
  numAnchors=3
  # Create a layer and add a sprite to it.
  player_layer = layer.Layer()
  me = sprite.Sprite('ball.jpg')
  player_layer.add(me)
  anchors = []
  for i in range(numAnchors) :
      anchors.append(sprite.Sprite('ball.jpg'))
      player_layer.add(anchors[i])
      anchors[i].position = (randint(0,600),randint(0,600))
  
  
  # Set initial position and velocity.
  me.position = (200, 300)
  me.velocity = (0, 0)
  
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