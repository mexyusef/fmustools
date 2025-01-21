import os
import re
import datetime


def calculate_percentage_of_minute_and_hour(verbose=False):
	# Get current time
	current_time = datetime.datetime.now().time()

	# Extract current minute, hour, and total minutes in a day
	current_minute = current_time.minute
	current_hour = current_time.hour
	total_minutes_in_a_day = 24 * 60

	# Calculate total minutes passed in the day
	total_minutes_passed = current_hour * 60 + current_minute

	# Calculate percentage for the current minute
	minute_percentage = int((current_minute / 60) * 100)

	# Calculate percentage for the current hour
	hour_percentage = int((total_minutes_passed / total_minutes_in_a_day) * 100)

	# Print the results
	if verbose:
		print(f"The percentage of the current minute ({current_minute} minutes) in the current hour ({current_hour} hours) is: {minute_percentage}%")
		print(f"The percentage of the current hour ({current_hour} hours) in a day ({total_minutes_in_a_day} minutes) is: {hour_percentage}%")
	return hour_percentage, minute_percentage

def percent_day():
	current_time = datetime.datetime.now().time()
	current_minute = current_time.minute
	current_hour = current_time.hour
	total_minutes_in_a_day = 24 * 60
	total_minutes_passed = current_hour * 60 + current_minute
	hour_percentage = int((total_minutes_passed / total_minutes_in_a_day) * 100)
	return hour_percentage

def percent_hour():
	current_time = datetime.datetime.now().time()
	current_minute = current_time.minute
	# current_hour = current_time.hour
	# total_minutes_in_a_day = 24 * 60
	# total_minutes_passed = current_hour * 60 + current_minute
	minute_percentage = int((current_minute / 60) * 100)
	return minute_percentage

def test_calculate_percentage_of_minute_and_hour():
	calculate_percentage_of_minute_and_hour()

def is_only_dots(input_string):
	# Use a regular expression to check if the string has only dots
	return bool(re.match(r'^[.]+$', input_string))

def navigate_back(path, command):
	# Split the path into directories
	current_path = os.path.normpath(path)
	directories = current_path.split(os.sep)
	directories[0] = directories[0]+'\\'  # ternyata os.path.join c: dan hapus jadi c:hapus, bukan c:\hapus
	# print('current_path:',current_path)
	# print('directoriesir:',directories)

	# Handle command "cd ...main"
	if command.startswith("cd ..."):
		# Extract the target directory from the command
		target_directory = command.split("...")[1].strip()
		# Find the index of the current directory in the path
		current_index = directories.index(target_directory)
		# Navigate to the target directory
		new_path = os.path.join(*directories[:current_index+1])
		# print('new_path:',new_path)
		return new_path
	elif command.startswith('cd ..'):
		# nama direktori yg diminta, e.g. cd ..controller

		# jika cd ..\somedir maka kembalikan ..\somedir
		if command.startswith('cd ..' + os.path.sep):
			return command.strip('cd ')
		parent_directory = os.path.dirname(path)
		if command.strip() == 'cd ..':
			return parent_directory
		target_directory = command.split("..")[1].strip()
		new_path = os.path.join(parent_directory, target_directory)
		if os.path.isdir(new_path):
			return new_path

def test_navigate_back():
	current_path = r"c:\hapus\dec26\coba-springboot-gql\spring-boot-graphql\src\main\java\com\example\graphql\service"

	new_path = navigate_back(current_path, "cd ..repository")
	print('new_path ..:',new_path)

	new_path = navigate_back(current_path, "cd ...main")
	print('new_path:',new_path)

	new_path = navigate_back(current_path, "cd ...spring-boot-graphql")
	print('new_path:',new_path)

def navigate_back_multiple(path, command):
	# Split the path into directories
	current_path = os.path.normpath(path)
	directories = current_path.split(os.sep)
	directories[0] = directories[0]+'\\'
	# Count the number of dots in the command
	# num_dots = command.count('.')
	num_dots = command.count('.')-1
	if num_dots<=0: return current_path
	# Ensure the number of dots does not exceed the length of directories
	num_dots = min(num_dots, len(directories)-1)

	# Navigate backward based on the number of dots
	new_path = os.path.join(*directories[:-num_dots])

	return new_path

def test_navigate_back_multiple():
	current_path = r"c:\hapus\dec26\coba-springboot-gql\spring-boot-graphql\src\main\java\com\example\graphql\service"

	new_path = navigate_back_multiple(current_path, "cd .")
	print(new_path)

	new_path = navigate_back_multiple(current_path, "cd ..")
	print(new_path)

	new_path = navigate_back_multiple(current_path, "cd ...")
	print(new_path)

	new_path = navigate_back_multiple(current_path, "cd ....")
	print(new_path)

	new_path = navigate_back_multiple(current_path, "cd .....")
	print(new_path)


if __name__ == '__main__':
	test_navigate_back()
