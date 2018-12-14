import random

# to do
# only need to write committees with capacities






# List the committees in conference here
Committees = ['ASEAN','IMF', 'UNECLAC','EU', 'ECOSOC','IAEA','SPECPOL','JCC - USSR','JCC - USA','UNEP','UNHCR','WHO','DISEC','HRC','UNSC']
print(len(Committees))


# (Optional) List committees that should be small. This way the algorithm will assign 
# less delegates here at a time. If clause inside algorithm should be enabled as well
smallCommittees = ["UNSC","Historical"]

# List in the following dictionary the committee name and its capacity as the value 
Capacities = {'ASEAN':26,'IMF':50, 'UNECLAC':30,'EU':30, 'ECOSOC':50,'IAEA':50,'SPECPOL':50,'JCC - USSR':20,'JCC - USA':21,\
			'UNEP':50,'UNHCR':50,'WHO':50,'DISEC':50,'HRC':38,'UNSC':36}



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
		if reps[committee] < minReps and not committee in smallCommittees:
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

# END- DO NOT MODIFY CODE


# ENTER REGISTERED SCHOOLS AND THEIR DELEGATE COUNTS HERE
# 2018 Registered Schools
registeredSchools= {'Commonwealth School': 30, 'The High School Attached to Tsinghua University': 7, "La Scuola d'Italia": 10, 'Beverly High School': 12, 'Hamilton Wenham Regional High School': 20, 'Pioneer Charter School of Science II': 21, 'Hanover High School': 14, 'Revere High School': 16, 'Brookline High School': 20, 'ASDAN China (Educational Organization)': 50, 'Winthrop High School': 7, 'The Winsor School': 15, 'International School of Boston': 16, 'Williston Northampton School': 12, 'Santa Marta Bilingual School': 1, 'Ealing Independent College': 4, 'Pancyprian Gymnasium': 1, 'Jiangsu Education Services for International Exchanges': 30, 'Bishop Verot MUN': 19, 'Tabor Academy': 10, 'Jiangsu College for International Education': 30, 'Jiangsu Cambridge International Education': 30, 'League of Creative Minds': 26, 'Jiangsu International Education Consulting Center': 30, 'Milton High School Model U.N.': 12, 'Tesseract Education': 10, 'CATS Academy Boston': 8, 'Kennebunk High School': 30, 'Middlesex School': 1, 'Cantonment English School and College': 1, 'Universidad Tecmilenio': 1, 'Westwood High School Model UN Club': 16, 'Ramsey High School': 1, 'Belmont Model UN': 20, 'Buckingham Browne & Nichols School': 20, 'Menaul School Qingdao': 6, 'Al-Noor Academy': 10, 'The Putney School': 6, 'Shenzhen Overseas Chinese town middle school': 1, 'Milestone Institute': 3, 'Excel Academy Charter High School': 4, 'Wando High School': 1, 'The Calhoun School': 15, 'Lahore School of Economics': 4}




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
	assignments.append(assignment)



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


import csv
import pandas as pd
# read country mappings 

countryMappings = {}


df  = pd.read_csv('countryMappings.csv')


#print(list(df.columns.values))
for committee in Capacities:
	for i in range(Capacities[committee]):
		print('i',i)
		print('committee',committee)
		country = df.loc[i][committee]
		delegationID = committee + str(i+1)
		countryMappings[delegationID] = country
print(countryMappings)


# write the csv
nameOfCSVFile = 'MITMUNCXIAssignments.csv'

with open(nameOfCSVFile, mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['School', 'Committee', 'DelegationID','Country'])
    for school in delegationsBySchool:
    	for assignment in delegationsBySchool[school]:
    		commitee = assignment[0]
    		delegationID = commitee+str(assignment[1])
    		country = countryMappings[delegationID]
        	employee_writer.writerow([school, commitee, delegationID,country])



