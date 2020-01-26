# For quantum computing, this is a simple way to determine how much to rotate around a Bloch sphere.

# For the blog article explanation, please visit https://agentanakinai.wordpress.com/2020/01/23/finding-theta/
 
import math
ground = .4 # probability of measuring 0
adjacent = abs((ground - .5) * 2)
theta = math.acos(adjacent)
if (ground < .5):
    theta = math.pi - theta
print(theta)

# If using Qiskit, use circ.ry(theta, 0) to rotate around the Y axis.

# You could also use this with phi and use circ.rz(phi, 0) to rotate around the Z axis.
