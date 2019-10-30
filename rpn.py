#!/usr/bin/env python3

import operator

operators = {
	'+': operator.add,
	'-': operator.sub,
}

def calculate(string):
	stack = list()
	for token in string.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError: # this must be an operator
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1,arg2)
			stack.append(result)
		
	if len(stack) != 1:
		raise TypeError("malformed input: "+ string)

	return stack.pop()

def main():
	while True:
		calculate(input('rpn calc> '))

if __name__ == '__main__':
	main()
