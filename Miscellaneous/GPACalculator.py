def calculate_gpa():
	"""int(num_courses) + str(mark) + float(weight) --> float(total)
        Given the course marks, the weight of each course, calculates the GPA of a student."""
	dict = {'A+': 4.0, 'A': 4.0,'A-': 3.7,'B+': 3.3,'B': 3.0,'B-': 2.7,'C+': 2.3,'C': 2.0,'C-': 1.7,'D+': 1.3,'D': 1.0,'D-': 0.7,'F': 0.0}

	total = 0
	mark = 0
	total_weight = 0
	course = 1
	num_courses = a = int(input("Enter the number of courses: ")) #'a' is kept constant and not used in the while loop so that it can be used to calculate average later on.
	while num_courses>0:
		mark = input("Enter your mark in course #"+ str(course) +": ")
		mark = dict[mark] #Converts the inputted mark from letter grades in 
		weight = float(input("Enter the weight of this course: "))	
		total = total + mark*weight
		total_weight = total_weight + weight
		num_courses = num_courses - 1
		course = course + 1
	total = total/total_weight
	return total

print(calculate_gpa())

