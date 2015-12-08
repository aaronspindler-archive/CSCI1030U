class Cannonball:
   def __init__(self,y,velocityX,velocityY,timeStepSize):
       self.velocityX = velocityX
       self.velocityY = velocityY
       self.acceleration = -9.81
       self.timeStepSize = timeStepSize
       self.time = 0.0
       self.x = 0.0
       self.y = y
   def advanceTimeStep(self):
        self.velocityY += (self.acceleration * self.timeStepSize)
        self.x += (self.velocityX * self.timeStepSize)
        self.y += (self.velocityY * self.timeStepSize)
        self.time += self.timeStepSize
   def impactOnLastTimeStep(self):
        if(self.y <= 0):
            return True
        return False