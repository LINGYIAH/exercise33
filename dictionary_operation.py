student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}


# First, display the complete record using for loop, printing and some string formatting only
print("Complete record:")
for key, value in student.items():
    print(key + ": " + str(value))
print()


# Check if there's a key called 'email'. If not, ask the user to enter an email
if 'email' not in student:
    email = input("Enter email: ")
    student['email'] = email


# Ask the user to enter a new city, and update the existing city with this new one
# Make sure the new city is not an empty string
new_city = input("Enter new city: ")
if new_city != "":
    student['city'] = new_city


# Check if there's 'phone' key in the dictionary. If not, print a message saying "Phone number not found."
# Use the get() method
phone = student.get('phone')
if phone is None:
    print("Phone number not found.")
    phone = input("Enter phone number: ")
    student['phone'] = phone


# Add a new key called 'contact' to the dictionary, which is itself a dictionary containing two keys: 'phone' and 'email'.
student['contact'] = {
    'phone': student['phone'],
    'email': student['email']
}


# Add another key called 'courses' to the dictionary, which is itself a dictionary containing three keys: 'Python', 'Databases', and 'Software Engineering', with 88, 91, and 84 as their corresponding scores
student['courses'] = {
    'Python': 88,
    'Databases': 91,
    'Software Engineering': 84
}

# Calculate the average score for the student without built-in functions like sum(). Use a for loop instead. 
total = 0
count = 0
for course, score in student['courses'].items():
    total += score
    count += 1
average = total / count

# Add a new key called 'academic_status' to the dictionary
# It should be a string that indicates the student's academic status based on the average score. 
# If the score is >= 90, the status should be "Excellent".
# If the score is >= 75, the status should be "Good".
# If the score is >= 60, the status should be "Pass".
# If the score is < 60, the status should be "At Risk".
if average >= 90:
    status = "Excellent"
elif average >= 75:
    status = "Good"
elif average >= 60:
    status = "Pass"
else:
    status = "At Risk"
student['academic_status'] = status



# Add the logic to search for a course. 
# If the course is found, print the course name and score. If not, print "Course not found".
search_course = input("Enter course name to search: ")
if search_course in student['courses']:
    print(search_course + ": " + str(student['courses'][search_course]))
else:
    print("Course not found")



# Add the logic to update a course score. 
# Ask the user to enter the course name and the new score. 
# If the course is found, then update the score and print a message indicating the change.
# While adding the new course, make sure the new score is a number between 0 and 100
update_course = input("Enter course name to update: ")
if update_course in student['courses']:
    new_score_str = input("Enter new score (0-100): ")
    is_number = True
    for ch in new_score_str:
        if not (ch.isdigit() or ch == '.'):
            is_number = False
            break
    if is_number:
        new_score = float(new_score_str)
        if 0 <= new_score <= 100:
            student['courses'][update_course] = new_score
            print("Score updated for " + update_course + " to " + str(new_score))
        else:
            print("Score must be between 0 and 100.")
    else:
        print("Score must be a number.")
else:
    print("Course not found")


# Recaclculate the average score and update the academic status after the course score has been updated.
total = 0
count = 0
for course, score in student['courses'].items():
    total += score
    count += 1
average = total / count
if average >= 90:
    status = "Excellent"
elif average >= 75:
    status = "Good"
elif average >= 60:
    status = "Pass"
else:
    status = "At Risk"
student['academic_status'] = status



# Display the final formatted student record with all the updated information, including the average score and academic status.

print("=====================================")
print("        STUDENT RECORD")
print("=====================================")
print()
print("Name: " + student['name'])
print("Student ID: " + student['student_id'])
print("Age: " + str(student['age']))
print("Program: " + student['program'])
print("City: " + student['city'])
print("GPA: " + str(student['gpa']))
print()
print("CONTACT")
print("Phone: " + student['contact']['phone'])
print("Email: " + student['contact']['email'])
print()
print("COURSE RESULTS")
for course, score in student['courses'].items():
    print(course + ": " + str(score))
print()
print("Average Score: " + str(round(average, 1)))
print("Academic Status: " + student['academic_status'])
print()
print("=====================================")