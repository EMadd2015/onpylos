from vpython import *
import math

class Space:
	def __init__(self):
		self.isOccupied = False
		self.NEchild = None
		self.NWchild = None
		self.SWchild = None
		self.SEchild = None
		self.x = None
		self.y = None
		self.z = None

class Board:
	def __init__(self):
		# pile of 2d layers of spaces, such that each successive layer is 1 smaller than the layer below. The base layer is 4x4.
		layers = [[[Space() for a in range(4)] for b in range(4)], [[Space() for i in range(3)] for j in range(3)], [[Space() for m in range(2)] for n in range(2)], [[Space() for u in range(1)] for v in range(1)]]
		# link every space in each layer to its "children," the spaces in the layer below that support its place in the pile
		for z in range(len(layers) - 1): # -1 because base (4x4) layer doesn't need to be linked
			for y in range(len(layers[z+1])):
				for x in range(len(layers[z+1][y])):
					layers[z+1][y][x].NEchild = layers[z][y][x+1]
					layers[z+1][y][x].NWchild = layers[z][y][x]
					layers[z+1][y][x].SWchild = layers[z][y+1][x]
					layers[z+1][y][x].SEchild = layers[z][y+1][x+1]
		# render the pile
		offset = math.cos(math.pi/3)
		for l in range(len(layers)):
			for m in range(len(layers[l])):
				for n in range(len(layers[l][m])):
					space = layers[l][m][n]
					space.x = n + (l * offset)
					space.y = m + (l * offset)
					space.z = l * offset
					sphere(pos=vector(space.x, space.y, space.z),radius=0.5)

Board()
