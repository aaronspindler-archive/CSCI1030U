#Description: Simulate the fall of a bungee jumper using physics and forces

#Import the libraries needed to draw the simulation
from visual import *

#Definition of the function animateBungeeJumper
def animateBungeeJumper(mass, deltaT, simulationTime, surfaceArea, unstretchedBungeeLength):

    #Initializing the animation screen
    scene = display(title='Bungee Jumper',
                x=0, y=0, width=600, height=600,
                center=(0,0,0), range=(100,100,100),
                autoscale=False, exit=False)
    initialPos = vector(0,40,0)
    jumper = sphere(pos=initialPos, radius=2, color=(1,1,0))
    bungee = cylinder(pos=initialPos, axis=initialPos, radius=0.5, color=(0,0,1))

    #Declaring variables
    d = 0
    k = 21.7
    gravity = -9.80
    currentTime = 0.0
    velocity = 0.0

    #While loop set to run until the current time is greater than or equal to
    # the simulation time
    while(currentTime <= simulationTime):
        #Calculate the force weight
        forceWeight = mass * gravity
        #Calculate the force friction
        forceFriction = -0.65 * surfaceArea * velocity * abs(velocity)
        #Calculate the force spring
        forceSpring = -k * d
        #Calculate the force total
        forceTotal = forceWeight + forceFriction + forceSpring

        #Calculate the acceleration
        acceleration = forceTotal / mass
        #Calculate the velocity
        velocity += acceleration * deltaT
        #Calculate the displacement
        d += velocity * deltaT

        #Increment the current time
        currentTime += deltaT

        #Set the refresh rate of the animation
        rate(60)

        #Set the animation locations
        jumper.pos.y = d
        bungee.axis.y = -bungee.pos.y + jumper.pos.y

#Test the function
animateBungeeJumper(60,0.1,90,0.2,30)
