class Warior:
	def set(self, n):
		self.name = n
		self.health = 100
	def hit(self, obj):
		obj.health -= 20
		print(self.name+" attacked "+obj.name+" which now has "+str(obj.health)+" health.")


