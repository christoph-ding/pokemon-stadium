# pokemon needs stats
import random

types = ['normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting',
 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost',
 'dragon', 'dark', 'steel', 'fairy']


# Parent class Pokemon generates stats
class Pokemon:
	# automatically call stat generating methods
	def __init__(self, name = 'None'):
			self.name = name
			self.hp = self.generate_hp()
			self.attack = self.generate_attack()
			self.defense = self.generate_defense()
			self.sp_attack = self.generate_sp_attack()
			self.sp_defense = self.generate_sp_defense()
			self.speed = self.generate_speed()
			self.type = self.generate_type()

	#summary - do I need this?
			self.info ={'Name': self.name,
						'HP': self.hp,
						'Atk': self.attack,
						'Def': self.defense,
						'SpA': self.sp_attack,
						'SpD': self.sp_defense,
						'Spe': self.speed,
						'Type': self.type
						}

	# generates statistics:
	def generate_hp(self):
			return random.randint(20,35)
	def generate_attack(self):
			return random.randint(3,11)
	def generate_defense(self):
			return random.randint(3,11)
	def generate_sp_attack(self):
			return random.randint(3,11)
	def generate_sp_defense(self):
			return random.randint(3,11)
	def generate_speed(self):
			return random.randint(3,11)
	def generate_type(self):
			return random.choice(types)

	# prints out statistics

	# def __repr__(self):
	# 	msgs = ['Name: %s' % self.name,
	# 			'HP: %s' % self.hp,
	# 			'Atk: %s' % self.attack,
	# 			'Def: %s' % self.defense,
	# 			'SpA: %s' % self.sp_attack,
	# 			'SpD: %s' % self.sp_defense,
	# 			'Spe: %s' % self.speed]
	# 	return '\n'.join(msgs)

	def __str__(self):
		msgs = ['Name: %s' % self.name,
                'Type: %s' % self.type,
				'HP: %s' % self.hp,
				'Atk: %s' % self.attack,
				'Def: %s' % self.defense,
				'SpA: %s' % self.sp_attack,
				'SpD: %s' % self.sp_defense,
				'Spe: %s' % self.speed]
		return '\n'.join(msgs)

# Role
class Physical_Attacker(Pokemon):
	def generate_attack(self):
		Pokemon.generate_attack(self) + random.randint(2,4)

class Physical_Wall(Pokemon):
	def generage_defense(self):
		Pokemon.generate_defense(self) + random.randint(2,4)

class Special_Attacker(Pokemon):
	def generate_sp_attack(self):
		Pokemon.generate_sp_attack(self) + random.randint(2,4)

class Special_Wall(Pokemon):
	def generate_sp_defense(self):
		Pokemon.generate_sp_defense(self) + random.randint(2,4)
