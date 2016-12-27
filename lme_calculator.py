import os
import re

def lme_eval(expr):
	if sum([1 for char in expr if char not in "1234567890.+-/* "]) == 0:
		nums = re.split('\*|/|\+|\-', expr, 1)
		try: numf, o = map(float, nums), expr[len(nums[0])]
		except Exception: return None
		if o == '+': return sum(numf)
		elif o == '-': return numf[0] - numf[1]
		elif o == '*': return numf[0]*numf[1]
		elif o == '/': return numf[0]/numf[1] if numf[1] != 0 else None
	else: return None

def calcul(expr):
	print lme_eval(expr)

while True:
	print 'Enter an exression to calculate'
	calcul(raw_input())
	os.system('pause')
	os.system('cls')
	break