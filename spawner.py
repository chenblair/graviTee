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

class Spawner(actions.Move):
  
  # step() is called every frame.
  # dt is the number of seconds elapsed since the last call.
  def step(self, dt):
    
    super(Spawner, self).step(dt) # Run step function on the parent class.
    global reloadTime
    reloadTime+=dt
    print(reloadTime)
    global spawnRate
    if len(projectiles)<=spawnMax and reloadTime>=spawnRate:
    #if len(yous)<=10:
        
        projectile = sprite.Sprite('ball.jpg')
        player_layer.add(projectile)
  
        # Set initial position and velocity.
        projectile.position = (0, randint(0,600))
        projectile.velocity = (randint(500,2000), randint(-300,300))
        projectile.do(Projectile())
        projectiles.append(projectile)
        reloadTime-=spawnRate
        #print(len(yous));
        
    
# Main class
class Projectile(actions.Move):
    def step(self, dt):
    
        super(Projectile, self).step(dt) # Run step function on the parent class.
    
    # Determine velocity based on keyboard inputs.
        #velocity_x = randint(0,1000)
        #velocity_y = randint(-150,150)
    
    # Set the object's velocity.
        #self.target.velocity = (velocity_x, velocity_y)
    
def main():
  global keyboard,projectiles,spawnMax,reloadTime,spawnRate # Declare this as global so it can be accessed within class methods.
  # Initialize the window.
  projectiles=[]
  spawnMax=10
  reloadTime=1.0
  spawnRate=1.0
  director.init(width=1000, height=600, do_not_scale=True, resizable=True)
  
  # Create a layer and add a sprite to it.
  global player_layer
  player_layer = layer.Layer()
  spawner = sprite.Sprite('ball.jpg')
  player_layer.add(spawner)
  
  # Set initial position and velocity.
  spawner.position = (0, randint(0,600))
  spawner.velocity = (0, 0)
  spawner.visible=False
  # Set the sprite's movement class.
  spawner.do(Spawner())

  # Create a scene and set its initial layer.
  main_scene = scene.Scene(player_layer)

  # Attach a KeyStateHandler to the keyboard object.
  keyboard = key.KeyStateHandler()
  director.window.push_handlers(keyboard)

  # Play the scene in the window.
  director.run(main_scene)

if __name__ == '__main__':
    main()