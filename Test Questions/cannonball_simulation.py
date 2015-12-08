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

cannonball1 = Cannonball(0.10,20.0,10.0,0.1)
cannonball2 = Cannonball(10.0,16.0,10.0,0.1)

cannonBall1_x = []
cannonBall1_y = []
cannonBall1_time = []

cannonBall2_x = []
cannonBall2_y = []
cannonBall2_time = []

while(cannonball1.impactOnLastTimeStep() == False):
    cannonBall1_x.append(cannonball1.x)
    cannonBall1_y.append(cannonball1.y)
    cannonBall1_time.append(cannonball1.time)

    cannonball1.advanceTimeStep()

while(cannonball2.impactOnLastTimeStep() == False):
    cannonBall2_x.append(cannonball2.x)
    cannonBall2_y.append(cannonball2.y)
    cannonBall2_time.append(cannonball2.time)

    cannonball2.advanceTimeStep()

#print("c1_time:",cannonBall1_time[len(cannonBall1_time) - 1])
#print("c2_time:",cannonBall2_time[len(cannonBall2_time) - 1])

#print("c1_x:",cannonBall1_x[len(cannonBall1_x) - 1])
#print("c2_x:",cannonBall2_x[len(cannonBall2_x) - 1])

if(cannonBall1_time[len(cannonBall1_time) - 1] > cannonBall2_time[len(cannonBall2_time) - 1]):
    print("Cannonball2 hit the ground before Cannonball1")
else:
    print("Cannonball1 hit the ground before Cannonball2")

if(cannonBall1_x[len(cannonBall1_x) - 1] < cannonBall2_x[len(cannonBall2_x) - 1]):
    print("Cannonball2 went farther than Cannonball1")
else:
    print("Cannonball1 went farther than Cannonball2")
