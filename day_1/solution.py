'''
name:	solution.py
desc:	Advent of Code day 1

author:	Chris Vantine
'''
def solve(input_string):
	'''
	solve calculates the captcha from the given input string

	PARAMETERS
	input_string:	(str) string to calculate from

	RETURNS
	int:			captcha sum

	PRE-CONDITIONS
	input_string is a string of integers only
	'''
	first_char = '9000'
	last_char = '9000'
	captcha_sum = 0
	position = 0

	for char in input_string:
		if first_char == '9000':
			first_char = char

		if char == last_char:
			captcha_sum = captcha_sum + int(char)

		last_char = char

	if first_char == last_char:
		captcha_sum = captcha_sum + int(first_char)

	return captcha_sum


def main():
	'''
	main is the main function of the program
	'''
	file = open('input')
	line = file.readline().strip()
	print("length: ", len(line))

	captcha_sum = solve(line)

	print(captcha_sum)


if __name__ == '__main__':
	main()