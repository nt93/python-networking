class ClassTest :
	def __init__ (self, name, roll) :
		self.name = name
		self.roll = roll

	def PrintStudentsList(self) :
		print('Student info',self.name,self.roll, sep=" : ")

l = []
for i in range(0,9):
	l.append(ClassTest('Kuchbhi',200))
for item in l:
	print(item.PrintStudentsList())

print (l)