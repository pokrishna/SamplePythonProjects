class Player():
    total_obj=2
    curr_obj=0
    
    def __new__(cls,*args,**kwargs):
	print("double fuck you")
        if Player.curr_obj >= Player.total_obj:
            raise ValueError("More than 2 obj")
        Player.curr_obj +=1
	print(cls.curr_obj)
	return super().__new__(cls)

    def __init__(self,name,health):
	print("fuck you")
	self.name=name
	self.health=health

    def __del__(self):
	Player.curr_obj -=1
	print("One object got redused")
    
    def __add__(self,other):
	return self.health+other.health
	
    def __str__(self):
	return str(self.helth)+" "+str(self.name)

class Text1():
    def __init__(self,fname):
	self.fname=fname
	self.f=None
    def __enter__(self):
	print("enters into enter")
	self.f=open(self.fname)
	return self.f
    def __exit__(self):
	print("__exit__")
	self.f.close()

    def __call__(self):
	return self.fname



class Iter_Demo():
	def __init__(self,odd):
		self.odd=odd
		self.s_odd=0
	def __iter__(self):
		return self
	def __next__(self):
		if self.odd < self.s_odd:
			raise ValueError("odd number is greater than")
		self.s_odd +=1
		return self.s_odd




















