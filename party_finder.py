import sys

# companions will be a doulby nested list of the form
# [[name, dislikes1, dislikes2, skills], [name, dislikes1, dislikes2, skills], etc...]
companions = [
	['Alonso Incosa', 		'Patrick Gordon',		'Juba', 			'Lr'],
	['Bogdan',				'Chibchan',				'Father Gober', 	'pa'],							
	['Chibchan',			'Jose de Alba',			'Alonso Incosa',	'TPHS'],	
	['Father Gober',		'John Kirk',			'Bogdan',			'tpHSE'],
	['Francois', 	 		'Jose de Alba',			'Alonso Incosa',	'CBNler'],
	['Frogling',			'Lamore',				'Vanhouten',		'cBn'],
	['John Kirk',			'Patrick Gordon',		'Frogling',			'CBNa'],
	['Jose de Alba', 		'Juba',					'Chibchan',			'cAh'],
	['Juba', 				'Vanhouten',			'Jose de Alba',		'btPh'],							
	['Lamore',				'Francois',				'Father Gober',		'CnA'],
	['Patrick Gordon', 		'Frogling',				'Francois',			'ctAper'],
	['Vanhouten',			'John Kirk',			'Frogling',			'cPeR']
]

# teams will be a doubly nested list of the form
# [[team member 1, team member 2, etc], [team member 1, team member 2, etc], etc]]
teams = []

runTests = False

def main(args):
	if len(args) == 0:
		usage()
		filt = ''
	else:
		filt = args[0]
	if runTests:
		conflictTest()
		validateData()
		existsTest()
		passesFilterTest()
	for i in range(len(companions)):
		getNewMember([], i)

	for team in sorted(teams, key=len, reverse=True):
		if passesFilter(team, filt):
			print(team)

def passesFilter(team, filt):
	for c in filt:
		c2 = c
		if c.islower():
			c2 = c.upper()
		satisfied = False
		for name in team:
			companion = getCompanion(name)
			if (c in companion[3]) or (c2 in companion[3]):
				satisfied = True
		if satisfied == False:
			return False
	return True

def passesFilterTest():
	testTeams = [
		['Alonso Incosa', 'Bogdan', 'Frogling', 'Jose de Alba'],
		['Alonso Incosa', 'Bogdan', 'John Kirk', 'Jose de Alba', 'Lamore']
	]
	if passesFilter(testTeams[0], 'rb') == False:
		print('filter test 1 failed')
		sys.exit(1)
	if passesFilter(testTeams[0], 'LB') == False:
		print('filter test 2 failed')
		sys.exit(1)
	if passesFilter(testTeams[0], 'HSE') == True:
		print('filter test 3 failed')
		sys.exit(1)
	if passesFilter(testTeams[0], '') == False:
		print('filter test 4 failed')
		sys.exit(1)
	print('filter tests passed')

def getCompanion(name):
	for companion in companions:
		if companion[0] == name:
			return companion
	print('No companion found by the name: ' + name)
	sys.exit(1)

def getNewMember(teamSoFar, index):
	companion = companions[index][0]
	if not createsConflict(teamSoFar.copy(), companion):
		teamSoFar.append(companion)
		successes = 0
		for i in range(len(companions)):
			successes += getNewMember(teamSoFar.copy(), i)
		if successes == 0:
			# no new team members were added, add to teams
			if not exists(teamSoFar.copy(), teams):
				teams.append(teamSoFar.copy())
		return 1
	else:
		return 0	


def createsConflict(team, newCompanion):
	# if this companion is already on the team, return true
	if newCompanion in team:
		return True

	# otherwise, look for conflicts
	# add the new companion to this copy of the team
	team.append(newCompanion)

	for companion in companions:
		#print('checking companion: ' + str(companion))
		if companion[0] in team:
			if (companion[1] in team) or (companion[2] in team):
				return True

	return False

def validateData():
	names = []
	for c in companions:
		names.append(c[0])
	for c in companions:
		if c[1] not in names:
			print(c[1] + ' not recognized')
			sys.exit(1)
		if c[2] not in names:
			print(c[2] + ' not recognized')
			sys.exit(1)

	print('data validated')

def conflictTest():
	if createsConflict(["Alonso Incosa", "Frogling"], "Father Gober") == True:
		print('conflict test 1 failed')
		sys.exit(1)
	if createsConflict(["Alonso Incosa", "Frogling"], "Frogling") == False:
		print('conflict test 2 failed')
		sys.exit(1)
	if createsConflict(["Alonso Incosa", "Frogling"], "Patrick Gordon") == False:
		print('conflict test 3 failed')
		sys.exit(1)

	print('conflict tests passed')

def exists(newTeam, teams):
	for team in teams:
		if (len(team) != len(newTeam)):
			continue # only check teams of the same length
		matches = 0
		for companion in newTeam:
			if companion in team:
				matches += 1
		if matches == len(team):
			return True
	return False

def existsTest():
	testTeams = [
		['Alonso Incosa', 'Bogdan', 'Frogling', 'Jose de Alba'],
		['Alonso Incosa', 'Bogdan', 'John Kirk', 'Jose de Alba', 'Lamore']
	]
	if exists(['Alonso Incosa', 'Bogdan', 'Frogling', 'Jose de Alba'], testTeams) == False:
		print('exists test 1 failed')
		sys.exit(1)
	if exists(['Alonso Incosa', 'Frogling', 'Bogdan', 'Jose de Alba'], testTeams) == False:
		print('exists test 2 failed')
		sys.exit(1)
	if exists(['Alonso Incosa', 'Father Gober', 'Jose de Alba', 'Vanhouten'], testTeams) == True:
		print('exists test 3 failed')
		sys.exit(1)

	print('exists tests passed')

def usage():
	print("You may optionally provide a string argument specifying required attributes")
	print('B buccaneering')
	print('T Tracking')
	print('P Path-finding')
	print('N Navigation')
	print('H Herbalism')
	print('S Surgery')
	print('E Engineer')
	print('C captain (Fleetmaster, Naval Combat, Seafaring)')
	print('A tactics')
	print('R trade')
	print('You may use any of these as lowercase to specify that an attribute is allowed to be weak')
	print('example: EHSNPCl')
	print()

if __name__ == '__main__':
	main(sys.argv[1:])


