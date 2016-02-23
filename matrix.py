import string
class matrix:
	__permanent = 0 #start filling
	def mmax(self):
		return max(max(self.table))
	def mmin(self):
		return min(min(self.table))
	def __init__(self, n, m):
		self.table = [[self.__permanent]*m]*n
		self.n = n
		self.m = m
		self.index = 1
		self.max = self.mmax()
		self.min = self.mmin()
	def fill(self, func):#table[i][j]=func(i,j)
		self.table = [[func(i+1, j+1) for j in range(self.m)] for i in range(self.n)]
		self.max = self.mmax()
		self.min = self.mmin()
	def keyboard_fill(self):
		print 'Enter your matrix (%dx%d), please:\n' % (self.n, self.m)
		height = self.n
		for i in range(height):
			tmp = map(lambda x: int(x), raw_input("").split(' '))
			if len(tmp) != self.m:
					print 'string is incorrect retype, please'
					height += 1
			else: self.table[i] = tmp
	def __iter__(self):
		self.index = 0
		return self
	def next(self):
		if self.index == self.n:
			self.index = 1
			raise StopIteration
		self.index += 1
		return self.table[self.index-1]
	def __str__(self):
		matr = ''
		max_len = max(len(str(self.max)),len(str(self.min)))		
		#print '%d !! %d !! %d' % (max_len, self.max, self.min)
		for line in self:
			matr += '||'+' '.join(strar(map(lambda x: format(x, max_len), line)))+'||\n'
		return matr
	def __getitem__(self, x):
		return self.table[x]
	def T(self):
		new = matrix(self.n, self.m)
		new.table = self.table
		new.index = self.index
		new.max = self.max
		new.min = self.min
		new.table = [[new.table[i][j] for i in range(new.n)] for j in range(new.m)]
		(new.n, new.m)=(new.m, new.n)
		return new	
	def __add__(self, other):
		n = self.n
		m = self.m
		new = matrix(n, m)
		new.table = [[self.table[i][j]+other.table[i][j] for j in range(m)] for i in range(n)]
		new.max = new.mmax()
		new.min = new.mmin()
		return new
	def __sub__(self, other):
		n = self.n
		m = self.m
		new = matrix(n, m)
		new.table = [[self.table[i][j]-other.table[i][j] for j in range(m)] for i in range(n)]
		new.max = new.mmax()
		new.min = new.mmin()
	def __mul__(self, other):
		new = matrix(self.n, other.m)
		oT = other.T()
        	new.table = [[sum(map(lambda x, y: x*y, self.table[i], oT.table[j])) for i in range(self.n)] for j in range(other.m)]
        	new.max = new.mmax()
		new.min = new.mmin()
		return new
	def __pow__(self, k):		
		n = self.n
		m = self.m
		new = matrix(n, m)
		new.fill(delta_ij)
		for i in range(k):
			print new
			new = new * self
		return new
###############################################################################################################
def identity_func(x, y):
		if x==y: return 1
def strar(ar):
	return map(lambda x: str(x), ar)
def format(x, n):
	ans = str(x)
	if len(ans) < n:
		ans+=' '*(n-len(ans))
	return ans
def f(i,j):
	return i**j
def g(i,j):
	return -i*j
def Kronecker(i,j):
	if i == j: return 1
	else: return 0
def delta_ij(i,j): return Kronecker(i,j)
###############################################################################################################
M = matrix(3,3)
N = matrix(1,5)
M.fill(delta_ij)
N.fill(g)
#print N*M
print M*M*M
print M**2
