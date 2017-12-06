import random

# List the committees in conference here
Committees = ['UNSC', 'DISEC', 'Futuristic', 'HRC', 'UNECLAC', 'WHO', 'UNEP', 'JCC', 'EU', 'WTO', 'IMF', 'IAEA', 'ASEAN', 'UNHCR', 'SPECPOL', 'ECOSOC']


# (Optional) List committees that should be small. This way the algorithm will assign 
# less delegates here at a time. If clause inside algorithm should be enabled as well
smallCommittees = ["UNSC","Historical"]

# List in the following dictionary the committee name and its capacity as the value 
Capacities = {"ASEAN":50,"DISEC":55,"JCC":50,"Futuristic":50,"SPECPOL":50,"EU":50,"WHO":50,"WTO":50,"IMF":50, \
			  "UNSC":40,"HRC":50,"ECOSOC":50,"UNECLAC":55,"IAEA":50,"UNEP":50,"UNHCR":50}



# START - DO NOT MODIFY 
capacity = 0
for committee in Committees:
	capacity += Capacities[committee]


slotsForConference = {}

for committee in Capacities:
	slotsForConference[committee] = {}
	for delegation in range(1, Capacities[committee]+1):
		slotsForConference[committee][delegation] = "Available"


print "Total capacity is",capacity


def getSpotsLeft():
	spotsleft =[]
	for committee in slotsForConference:
		for slot in slotsForConference[committee]:
			if slotsForConference[committee][slot] == "Available":
				spotsleft.append((committee,slot))

	return spotsleft

def getSmallestCommitteeSoFar(delegations):
	reps = {}
	for delegation in delegations:

		committee = delegation[0]
		slot = delegation[1]
		if committee in reps:
			reps[committee] +=1
		else:
			reps[committee] =1
	#print reps
	minCommittee = reps.keys()[0]
	#print "minCommittee before loop",minCommittee
	minReps = 400
	for committee in reps:
		if reps[committee] < minReps and not committee in ["UNSC","Historical"]:
			minCommittee =  committee
			minReps = reps[committee]
	#print "minCommittee",minCommittee
	return minCommittee


def getNextAvailableSlotInCommittee(committee):
	openSlots = []
	for slot in slotsForConference[committee]:
		if slotsForConference[committee][slot] == "Available":
			openSlots.append(slot)

	if len(openSlots) ==0:
		return None
	else:
		return openSlots[random.randrange(len(openSlots))]


def match_committees(delegation_size):
	delegations = []
	
	#print "need",delegation_size,"delegations for this delegations"

	for committee in Committees:
		if len(delegations) ==delegation_size:
			break		
		delegationsMatchedSoFarForThisCommittee = 0
		# (Optional) Enable this clause to assign less delegates
		# to small committees. smallCommittees variable should
		# also be enabled above
		# if committee in smallCommittees:
		# 	maxDelegationsForAschool = 1
		# else:
		# 	maxDelegationsForAschool = 2

		
		maxDelegationsForAschool =1
		for slot in slotsForConference[committee]:
			if slotsForConference[committee][slot] == "Available":
				delegations.append((committee,slot))
				slotsForConference[committee][slot] = "Occupied"
				delegationsMatchedSoFarForThisCommittee +=1
			if delegationsMatchedSoFarForThisCommittee == maxDelegationsForAschool:
				break

	lastCommittees = []
	i=0

	# For debugging:
	# print delegations
	while len(delegations) < delegation_size:
		spotsleft = getSpotsLeft()

		if len(spotsleft) == 0:
			print "RAN OUT OF DELEGATIONS"
			break


		smallestCommitteeSoFar = getSmallestCommitteeSoFar(delegations)
		availableSlot = getNextAvailableSlotInCommittee(smallestCommitteeSoFar)


		if availableSlot == None:
			lastResort = getSpotsLeft()[0]
			smallestCommitteeSoFar = lastResort[0]
			availableSlot = lastResort[1]

		delegations.append((smallestCommitteeSoFar,availableSlot))
		slotsForConference[smallestCommitteeSoFar][availableSlot] = "Occupied"


	return delegations
registeredSchools = {}

# END- DO NOT MODIFY CODE



# ENTER REGISTERED SCHOOLS AND THEIR DELEGATE COUNTS HERE
# 2017 Registered Schools
registeredSchools= {}




delegationsNeeded = 0
for school in registeredSchools:
	delegationsNeeded +=registeredSchools[school]

print "need",delegationsNeeded, "delegations"

schools = []

delegationsBySchool = {}

assignments = []
for school in registeredSchools:
	assignment = match_committees(registeredSchools[school])
	delegationsBySchool[school] = assignment



def anyRepetitions(inputted_list):
	reps = {}
	for test in inputted_list:
		for assignment in test:
			if assignment not in reps:
				reps[assignment] = True
			else:
				return True
	print "A total of", len(reps.keys()),'unique delegations'
	return False

for school in delegationsBySchool:
	#print "needed", len(test)
	print "\n",school
	print delegationsBySchool[school]
print len(assignments), "schools were assigned"


if not anyRepetitions(assignments):
	print "Verified: No delegations were repeated in matching"
else:
	print "Heads up: Delegations were repeated in this matching"



