# Python Cocos2d Game Development
# Part 1: Getting Started

# Tutorial: http://jpwright.net/writing/python-cocos2d-game-1/
# Github: http://github.com/jpwright/cocos2d-python-tutorials

# Jason Wright (jpwright0@gmail.com)


# Imports

import pyglet
from pyglet.window import key
from pyglet.window.key import KeyStateHandler

import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director

from math import sqrt

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
class Ball(actions.Move):
    G2 = 0
    prevVelocity_x = 0
    prevVelocity_y = 0
    
    def __init__(self):
        super( Ball, self ).__init__()
  
    # step() is called every frame.
    # dt is the number of seconds elapsed since the last call.
    def gravity (self,myX,myY,aX,aY,G):
        dist=sqrt((myX-aX)**2+(myY-aY)**2)
        graviX = G*-(myX-aX)/(dist**2)
        graviY = G*-(myY-aY)/(dist**2)
        return {'graviX':graviX, 'graviY':graviY }
    def step(self, dt):
    
        super(Ball, self).step(dt) # Run step function on the parent class.
        G=100.0
        G2 = self.G2
        G2 += 5*dt
        self.G2 = G2
        myX = ball.position[0]
        myY = ball.position[1]
        velocity_x = self.prevVelocity_x
        velocity_y = self.prevVelocity_y
        for anchor in anchors :
            result = self.gravity(myX,myY,anchor.position[0],anchor.position[1],G)
            # Determine velocity based on keyboard inputs.
            velocity_x += result['graviX']
            velocity_y += result['graviY']
        
        result = self.gravity(myX,myY,player1.position[0],player1.position[1],G2)
        velocity_x += result['graviX']
        velocity_y += result['graviY']
        result = self.gravity(myX,myY,player2.position[0],player2.position[1],G2)
        velocity_x += result['graviX']
        velocity_y += result['graviY']
        self.prevVelocity_x = velocity_x
        self.prevVelocity_y = velocity_y
    
        # Set the object's velocity.
        self.target.velocity = (velocity_x, velocity_y)
        # print(velocity_x,velocity_y)
        
class AnchorDrop(cocos.layer.Layer):

    # If you want that your layer receives director.window events
    # you must set this variable to 'True'
    is_event_handler = True

    def __init__(self):

        super( AnchorDrop, self ).__init__()
    def on_key_press (self, pressed, modifiers):
        if keyboard[key.SPACE]:
            anchors.append(sprite.Sprite('ball.jpg'))
            player_layer.add(anchors[-1])
            anchors[-1].position = (player1.position[0],player1.position[1])
        if keyboard[key.Z]:
            anchors.append(sprite.Sprite('ball.jpg'))
            player_layer.add(anchors[-1])
            anchors[-1].position = (player2.position[0],player2.position[1])
    
# Main class

def main():
  global keyboard,player1,player2,anchors,player_layer,ball # Declare this as global so it can be accessed within class methods.
  
  # Initialize the window.
  director.init(width=500, height=300, do_not_scale=True, resizable=True)
  
  anchors = []
  
  # Create a layer and add a sprite to it.
  player_layer = layer.Layer()
  player1 = sprite.Sprite('ball.jpg')
  player_layer.add(player1)
  
  ball = sprite.Sprite('earth-small.png')
  player_layer.add(ball)
  
  player2 = sprite.Sprite('ball.jpg')
  player_layer.add(player2)
  
  # Set initial position and velocity.
  ball.position = (250,150)
  ball.velocity = (0,0)
  
  player1.position = (400, 150)
  player1.velocity = (0, 0)
  
  player2.position = (100, 150)
  player2.velocity = (0, 0)
  
  # Set the sprite's movement class.
  ball.do(Ball());
  player1.do(Player1())
  player2.do(Player2())

  # Create a scene and set its initial layer.
  main_scene = scene.Scene(player_layer,AnchorDrop())

  # Attach a KeyStateHandler to the keyboard object.
  keyboard = key.KeyStateHandler()
  director.window.push_handlers(keyboard)

  # Play the scene in the window.
  director.run(main_scene)

if __name__ == '__main__':
    main()