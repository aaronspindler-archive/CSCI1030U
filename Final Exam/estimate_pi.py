import numpy as np
import math

def rand():
    return np.random.rand()

def throwStars(numStars):
    inCircle = 0
    for Stars in xrange(1, numStars + 1):
        x = rand()
        y = rand()
        if (x*x + y*y)**0.5 <= 1.0:

   inCircle += 1

 return 4*(inCircle/float(numStars))


def getEstimate(numStars, numTrials):

 estimates = []

 for t in range(numTrials):

  piGuess = throwStars(numStars)

  estimates.append(piGuess)

 curEst = sum(estimates)/len(estimates)

 return curEst

def estimatePi(numIterations):

 numStars = 10000

 return getEstimate(numStars,numIterations)

print estimatePi(100)
