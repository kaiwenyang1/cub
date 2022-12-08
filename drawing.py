from PIL import Image, ImageDraw
class drawing:
	delta = 12
	smallDelta = 5
	length = 50
	faceLength = length*3+smallDelta*2+delta
	RED = (255,0,0)
	ORANGE = (255,128,0)
	YELLOW = (255,255,0)
	GREEN = (0,255,0)
	BLUE = (0,0,255)
	WHITE = (255,255,255)
	im = Image.new('RGB', (1000, 600), (169, 169, 169))
	draw = ImageDraw.Draw(im)
	

	def __init__(self):
		pass

	def draw_square(self, face, x, y, colour):
		print("test")
		originx = 200
		originy = 200
		if face == "F":
			pass
		elif face == "L":
			originx-=self.faceLength
		elif face == "R":
			originx+= self.faceLength
		elif face == "B":
			originx += 2*self.faceLength
		elif face == "U":
			originy-=self.faceLength
		elif face == "D":
			originy+=self.faceLength
		else:
			print("no face")
		originx += y*(self.smallDelta+self.length)
		originy += x*(self.smallDelta+self.length)
		if colour == "R":
			self.draw.rectangle((originx, originy, originx+self.length, originy+self.length), fill=self.RED)
		elif colour == "O":
			self.draw.rectangle((originx, originy, originx+self.length, originy+self.length), fill=self.ORANGE)
		elif colour == "B":
			self.draw.rectangle((originx, originy, originx+self.length, originy+self.length), fill=self.BLUE)
		elif colour == "W":
			self.draw.rectangle((originx, originy, originx+self.length, originy+self.length), fill=self.WHITE)
		elif colour == "Y":
			self.draw.rectangle((originx, originy, originx+self.length, originy+self.length), fill=self.YELLOW)
		elif colour == "G":
			self.draw.rectangle((originx, originy, originx+self.length, originy+self.length), fill=self.GREEN)
		print(str(originx) + " " + str(originy))

	def draw_face(self, face, arr):
		for i in range(3):
			for j in range(3):
				self.draw_square(face, i, j, arr[i][j])


		

