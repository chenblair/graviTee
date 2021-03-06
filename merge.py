from random import randint

import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director
from math import sqrt

#global prevVelocity_y,prevVelocity_x

"""class Me(actions.Move):
    prevVelocity_x = 10
    prevVelocity_y = 0
    
    def __init__(self):
        super( Me, self ).__init__()
  
  # step() is called every frame.
  # dt is the number of seconds elapsed since the last call.
    def step(self, dt):
    
        super(Me, self).step(dt) # Run step function on the parent class.
        G=100.0
        myX = me.position[0]
        myY = me.position[1]
        velocity_x = self.prevVelocity_x
        velocity_y = self.prevVelocity_y+500 * (keyboard[key.UP] - keyboard[key.DOWN])
        for anchor in anchors :
            aX = anchor.position[0] 
            aY = anchor.position[1]
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
        print(velocity_x,velocity_y)"""
    
class Mouse(cocos.layer.Layer):

    is_event_handler = True     #: enable director.window events

    def __init__(self):
        super( Mouse, self ).__init__()

    def on_mouse_press (self, x, y, buttons, modifiers):
        """This function is called when any mouse button is pressed

        (x, y) are the physical coordinates of the mouse
        'buttons' is a bitwise or of pyglet.window.mouse constants LEFT, MIDDLE, RIGHT
        'modifiers' is a bitwise or of pyglet.window.key modifier constants
        (values like 'SHIFT', 'OPTION', 'ALT')
        """
        anchors.append(sprite.Sprite('Sun_Glasses.png'))
        player_layer.add(anchors[-1])
        anchors[-1].position = (x,y)
# Main class
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
        
        projectile = sprite.Sprite('earth-small.png')
        player_layer.add(projectile)
  
        # Set initial position and velocity.
        projectile.position = (0, randint(0,600))
        projectile.velocity = (randint(50,200), randint(-30,30))
        projectile.do(Projectile())
        projectiles.append(projectile)
        reloadTime-=spawnRate
        #print(len(yous));
        
    
# Main class
class Projectile(actions.Move):
    def step(self, dt):
        
        super(Projectile, self).step(dt)
        G=100.0
        myX = self.target.position[0]
        myY = self.target.position[1]
        velocity_x = self.target.velocity[0]
        velocity_y = self.target.velocity[1]+500 * (keyboard[key.UP] - keyboard[key.DOWN])
        for anchor in anchors :
            aX = anchor.position[0] 
            aY = anchor.position[1]
            dist=sqrt((myX-aX)**2+(myY-aY)**2)
            graviX=0
            graviY=0
            if dist<200 :
                graviX = G*-(myX-aX)/(dist**2)
                graviY = G*-(myY-aY)/(dist**2)
    
            # Determine velocity based on keyboard inputs.
            velocity_x += graviX
            velocity_y += graviY
    
        self.prevVelocity_x = velocity_x
        self.prevVelocity_y = velocity_y
    
        # Set the object's velocity.
        self.target.velocity = (velocity_x, velocity_y) # Run step function on the parent class.
        #print(self.target.velocity)
    # Determine velocity based on keyboard inputs.
        #velocity_x = randint(0,1000)
        #velocity_y = randint(-150,150)
    
    # Set the object's velocity.
        #self.target.velocity = (velocity_x, velocity_y)

def main():
  global keyboard,myX,myY,aX,aY,me,anchors,player_layer,projectiles,spawnMax,reloadTime,spawnRate # Declare this as global so it can be accessed within class methods.
  
  # Initialize the window.
  projectiles=[]
  spawnMax=10
  reloadTime=1.0
  spawnRate=1.0
  director.init(width=1000, height=600, do_not_scale=True, resizable=True)
  
  #prevVelocity_x = 200
  #prevVelocity_y = 0
  
  # Create a layer and add a sprite to it.
  player_layer = layer.Layer()
  #me = sprite.Sprite('ball.jpg')
  #player_layer.add(me)
  anchors = []
  for i in range(len(anchors)) :
      anchors.append(sprite.Sprite('Sun_Glasses.png'))
      player_layer.add(anchors[i])
      anchors[i].position = (randint(0,600),randint(0,600))
  
  
  # Set initial position and velocity.
  #me.position = (200, 300)
  #me.velocity = (0, 0)
  
  # Set the sprite's movement class.
  #me.do(Me())
  
  spawner = sprite.Sprite('earth-small.png')
  player_layer.add(spawner)
  
  # Set initial position and velocity.
  spawner.position = (0, randint(0,600))
  spawner.velocity = (0, 0)
  spawner.visible=False
  # Set the sprite's movement class.
  spawner.do(Spawner())

  # Create a scene and set its initial layer.
  main_scene = scene.Scene(player_layer,Mouse())

  # Attach a KeyStateHandler to the keyboard object.
  keyboard = key.KeyStateHandler()
  director.window.push_handlers(keyboard)
  #director.run( cocos.scene.Scene( Mouse() ) )
  # Play the scene in the window.
  director.run(main_scene)


if __name__ == '__main__':
    main()