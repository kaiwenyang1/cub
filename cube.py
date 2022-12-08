from PIL import Image, ImageDraw
import random
import drawing
myDrawing = drawing.drawing()

class cube:
	U = [['W']*3 for i in range(3)]
	L = [['O']*3 for i in range(3)]
	F = [['G']*3 for i in range(3)]
	R = [['R']*3 for i in range(3)]
	B = [['B']*3 for i in range(3)]
	D = [['Y']*3 for i in range(3)]
	moves = []
	Tperm = ["R","U","R\'","U\'","R\'","F","R2","U\'","R\'","U\'","R","U","R\'","F\'"]
	Jbperm = ["R","U","R\'","F\'","R","U","R\'","U\'","R\'","F","R2","U\'","R\'","U\'"]
	OPcorner = ["R","U\'","R\'","U\'","R","U","R\'","F\'","R","U","R\'","U\'","R\'","F","R"]
	Raperm = ["R","U\'","R\'","U\'","R","U","R","D","R\'","U\'","R","D\'","R\'","U2","R\'","U\'"]
	OPedgeSetups = [
		#A
		["M2","D\'","L2"],
		#B (buffer)
		[],
		#C
		["M2","D","L2"],
		#D (no setup)
		[],
		#E
		["L\'","E","L\'"],
		#F
		["E\'","L"],
		#G
		["L\'","E\'","L"],
		#H
		["E","L\'"],
		#I
		["M","D\'","L2"],
		#J
		["E2","L"],
		#K
		["M","D","L2"],
		#L
		["L'"],
		#M (buffer)
		[],
		#N
		["E","L"],
		#O
		["D2","L\'","E","L"],
		#P
		["E\'","L\'"],
		#Q
		["M\'","D","L2"],
		#R
		["L"],
		#S
		["M\'","D\'","L2"],
		#T
		["E2","L\'"],
		#U
		["D\'","L2"],
		#V
		["D2","L2"],
		#W
		["D","L2"],
		#X
		["L2"],
		#Y (doesn't exist)
		[],
		#Z (doesn't exist)
		[]
	]
	OPcornerSetups = [
		#A (buffer)
		[],
		#B
		["R2"],
		#C
		["R2","D\'"],
		#D
		["F2"],
		#E (buffer)
		[],
		#F
		["F\'","D"],
		#G
		["F\'"],
		#H
		["D\'","R"],
		#I
		["F","R\'"],
		#J
		["R\'"],
		#K
		["F\'","R\'"],
		#L
		["F2","R\'"],
		#M
		["F"],
		#N
		["R\'","F"],
		#O
		["R2","F"],
		#P
		["R","F"],
		#Q
		["R","D\'"],
		#R (buffer)
		[],
		#S
		["D","F\'"],
		#T
		["R"],
		#U
		["D"],
		#V (no setup)
		[],
		#W
		["D\'"],
		#X
		["D2"],
		#Y (doesn't exist)
		[],
		#Z (doesn't exist)
		[]
	]


	def __init__(self):
		for ch in "UFRBLDXYZMES":
			self.moves.append(ch)
			self.moves.append(ch+"2")
			self.moves.append(ch+"\'")

	def move_U(self):
		for i in range(3):
			temp = self.R[0][i]
			self.R[0][i] = self.B[0][i]
			self.B[0][i] = self.L[0][i]
			self.L[0][i] = self.F[0][i]
			self.F[0][i] = temp
		temp = self.U[1][2]
		self.U[1][2] = self.U[0][1]
		self.U[0][1] = self.U[1][0]
		self.U[1][0] = self.U[2][1]
		self.U[2][1] = temp
		temp = self.U[0][2]
		self.U[0][2] = self.U[0][0]
		self.U[0][0] = self.U[2][0]
		self.U[2][0] = self.U[2][2]
		self.U[2][2] = temp
	def move_U2(self):
		self.move_U()
		self.move_U()
	def move_Uprime(self):
		self.move_U()
		self.move_U()
		self.move_U()

	def move_X(self):
		temp = [['W']*3 for i in range(3)]
		for i in range(3):
			for j in range(3):
				temp[i][j] = self.F[i][j]
				self.F[i][j] = self.D[i][j]
		for i in range(3):
			for j in range(3):
				self.D[i][j] = self.B[2-i][2-j]
		for i in range(3):
			for j in range(3):
				self.B[i][j] = self.U[2-i][2-j]
		for i in range(3):
			for j in range(3):
				self.U[i][j] = temp[i][j]
		temp2 = self.L[0][2]
		self.L[0][2] = self.L[2][2]
		self.L[2][2] = self.L[2][0]
		self.L[2][0] = self.L[0][0]
		self.L[0][0] = temp2
		temp2 = self.R[0][2]
		self.R[0][2] = self.R[0][0]
		self.R[0][0] = self.R[2][0]
		self.R[2][0] = self.R[2][2]
		self.R[2][2] = temp2
		temp2 = self.L[0][1]
		self.L[0][1] = self.L[1][2]
		self.L[1][2] = self.L[2][1]
		self.L[2][1] = self.L[1][0]
		self.L[1][0] = temp2
		temp2 = self.R[0][1]
		self.R[0][1] = self.R[1][0]
		self.R[1][0] = self.R[2][1]
		self.R[2][1] = self.R[1][2]
		self.R[1][2] = temp2
	def move_X2(self):
		self.move_X()
		self.move_X()
	def move_Xprime(self):
		self.move_X()
		self.move_X()
		self.move_X()

	def move_Y(self):
		for i in range(3):
			for j in range(3):
				temp = self.F[i][j]
				self.F[i][j] = self.R[i][j]
				self.R[i][j] = self.B[i][j]
				self.B[i][j] = self.L[i][j]
				self.L[i][j] = temp
		temp = self.U[1][2]
		self.U[1][2] = self.U[0][1]
		self.U[0][1] = self.U[1][0]
		self.U[1][0] = self.U[2][1]
		self.U[2][1] = temp
		temp = self.U[0][2]
		self.U[0][2] = self.U[0][0]
		self.U[0][0] = self.U[2][0]
		self.U[2][0] = self.U[2][2]
		self.U[2][2] = temp
		temp = self.D[1][2]
		self.D[1][2] = self.D[2][1]
		self.D[2][1] = self.D[1][0]
		self.D[1][0] = self.D[0][1]
		self.D[0][1] = temp
		temp = self.D[0][2]
		self.D[0][2] = self.D[2][2]
		self.D[2][2] = self.D[2][0]
		self.D[2][0] = self.D[0][0]
		self.D[0][0] = temp
	def move_Y2(self):
		self.move_Y()
		self.move_Y()
	def move_Yprime(self):
		self.move_Y()
		self.move_Y()
		self.move_Y()

	def move_Z(self):
		self.move_X()
		self.move_Y()
		self.move_Xprime()
	def move_Z2(self):
		self.move_Z()
		self.move_Z()
	def move_Zprime(self):
		self.move_Z()
		self.move_Z()
		self.move_Z()

	def move_D(self):
		self.move_X2()
		self.move_U()
		self.move_X2()
	def move_D2(self):
		self.move_D()
		self.move_D()
	def move_Dprime(self):
		self.move_D()
		self.move_D()
		self.move_D()

	def move_F(self):
		self.move_X()
		self.move_U()
		self.move_Xprime()
	def move_F2(self):
		self.move_F()
		self.move_F()
	def move_Fprime(self):
		self.move_F()
		self.move_F()
		self.move_F()

	def move_R(self):
		self.move_Y()
		self.move_F()
		self.move_Yprime()
	def move_R2(self):
		self.move_R();
		self.move_R()
	def move_Rprime(self):
		self.move_R()
		self.move_R()
		self.move_R()

	def move_L(self):
		self.move_Yprime()
		self.move_F()
		self.move_Y()
	def move_L2(self):
		self.move_L()
		self.move_L()
	def move_Lprime(self):
		self.move_L()
		self.move_L()
		self.move_L()

	def move_B(self):
		self.move_Y2()
		self.move_F()
		self.move_Y2()
	def move_B2(self):
		self.move_B()
		self.move_B()
	def move_Bprime(self):
		self.move_B()
		self.move_B()
		self.move_B()

	def move_M(self):
		self.move_R()
		self.move_Lprime()
		self.move_Xprime()
	def move_M2(self):
		self.move_M()
		self.move_M()
	def move_Mprime(self):
		self.move_M()
		self.move_M()
		self.move_M()

	def move_E(self):
		self.move_U()
		self.move_Dprime()
		self.move_Yprime()
	def move_E2(self):
		self.move_E()
		self.move_E()
	def move_Eprime(self):
		self.move_E()
		self.move_E()
		self.move_E()

	def move_S(self):
		self.move_B()
		self.move_Fprime()
		self.move_Z()
	def move_S2(self):
		self.move_S()
		self.move_S()
	def move_Sprime(self):
		self.move_S()
		self.move_S()
		self.move_S()

	def apply_move(self, move):
		if move == "U":
			self.move_U()
		if move == "U2":
			self.move_U2()
		if move == "U'":
			self.move_Uprime()
		if move == "F":
			self.move_F()
		if move == "F2":
			self.move_F2()
		if move == "F'":
			self.move_Fprime()
		if move == "R":
			self.move_R()
		if move == "R2":
			self.move_R2()
		if move == "R'":
			self.move_Rprime()
		if move == "B":
			self.move_B()
		if move == "B2":
			self.move_B2()
		if move == "B'":
			self.move_Bprime()
		if move == "L":
			self.move_L()
		if move == "L2":
			self.move_L2()
		if move == "L'":
			self.move_Lprime()
		if move == "D":
			self.move_D()
		if move == "D2":
			self.move_D2()
		if move == "D'":
			self.move_Dprime()
		if move == "X":
			self.move_X()
		if move == "X2":
			self.move_X2()
		if move == "X'":
			self.move_Xprime()
		if move == "Y":
			self.move_Y()
		if move == "Y2":
			self.move_Y2()
		if move == "Y'":
			self.move_Yprime()
		if move == "Z":
			self.move_Z()
		if move == "Z2":
			self.move_Z2()
		if move == "Z'":
			self.move_Zprime()
		if move == "M":
			self.move_M()
		if move == "M2":
			self.move_M2()
		if move == "M'":
			self.move_Mprime()
		if move == "E":
			self.move_E()
		if move == "E2":
			self.move_E2()
		if move == "E'":
			self.move_Eprime()
		if move == "S":
			self.move_S()
		if move == "S2":
			self.move_S2()
		if move == "S'":
			self.move_Sprime()
			
	def apply_alg(self, alg):
		for move in alg:
			self.apply_move(move)

	def reverse_move(self, move):
		s = move[0]
		if len(move) == 1:
			s+="\'"
		elif move[1] == "2":
			s+="2"
		return s

	def undo_move(self, move):
		self.apply_move(self.reverse_move(move))

	def undo_alg(self, alg):
		for i in range(len(alg)-1,-1,-1):
			self.undo_move(alg[i])

	def generate_move(self):
		move = random.randint(0,5)
		direction = random.randint(0,3)
		s = "UFRBLD"[move]
		if direction == 0:
			s+="2"
		if direction == 1:
			s+="\'"
		return s

	def make_image_from_scramble(self):
		myDrawing.draw_face("U",self.U)
		myDrawing.draw_face("L",self.L)
		myDrawing.draw_face("R",self.R)
		myDrawing.draw_face("B",self.B)
		myDrawing.draw_face("F",self.F)
		myDrawing.draw_face("D",self.D)
		myDrawing.im.save('3bld.jpg', quality=100)

	def generate_scramble(self):
		scrambleLength = random.randint(18,20)
		prev = "A"
		scramble = []
		for i in range(scrambleLength):
			cur = prev
			while cur[0]==prev[0]:
				cur = self.generate_move()
			scramble.append(cur)
			prev = cur
		return scramble

	def get_scramble(self):
		scramble = self.generate_scramble()
		self.apply_alg(scramble)
		s = "```"
		for move in scramble:
			s+=move
			s+=" "
		s+="\n```"
		self.make_image_from_scramble()
		return s

	def apply_OPcornerswap(self, ch):
		self.apply_alg(self.OPcornerSetups[ord(ch)-ord("a")])
		self.apply_alg(self.OPcorner)
		self.undo_alg(self.OPcornerSetups[ord(ch)-ord("a")])

	def apply_OPedgeswap(self, ch):
		self.apply_alg(self.OPedgeSetups[ord(ch)-ord("A")])
		self.apply_alg(self.Tperm)
		self.undo_alg(self.OPedgeSetups[ord(ch)-ord("A")])

	def apply_blind_algs(self, s):
		for ch in s:
			if ch == "+":
				self.apply_alg(self.Raperm)
			elif ord(ch) >= ord("a") and ord(ch) <= ord("x"):
				self.apply_OPcornerswap(ch)
			elif ord(ch) >= ord("A") and ord(ch) <= ord("X"):
				self.apply_OPedgeswap(ch)

	def solve(self):
		self.U = [['W']*3 for i in range(3)]
		self.L = [['O']*3 for i in range(3)]
		self.F = [['G']*3 for i in range(3)]
		self.R = [['R']*3 for i in range(3)]
		self.B = [['B']*3 for i in range(3)]
		self.D = [['Y']*3 for i in range(3)]

	def to_string(self):		
		s = "```"
		for i in range(3):
			s+="   "
			for j in range(3):
				s+=self.U[i][j]
			s+="\n"
		for i in range(3):
			for j in range(3):
				s+=self.L[i][j]
			for j in range(3):
				s+=self.F[i][j]
			for j in range(3):
				s+=self.R[i][j]
			for j in range(3):
				s+=self.B[i][j]
			s+="\n"
		for i in range(3):
			s+="   "
			for j in range(3):
				s+=self.D[i][j]
			s+="\n"
		s+="```"
		return s

