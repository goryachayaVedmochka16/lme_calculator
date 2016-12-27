import os
import re

def lme_eval(expr):
	if sum([1 for char in expr if char not in "1234567890.+-/*()jJ "]) == 0:
		nums = re.split('\*|/|\+|\-', expr, 1)
		try: numf = map(float, nums)
		except Exception: return None
		if expr[len(nums[0])] == '+': return sum(numf)
		elif expr[len(nums[0])] == '-': return numf[0] - numf[1]
		elif expr[len(nums[0])] == '*': return numf[0]*numf[1]
		elif expr[len(nums[0])] == '/': return numf[0]/numf[1] if numf[1] != 0 else None
	else: return None

def calcul(expr):
	print lme_eval(expr)

while True:
	print 'Enter an exression to calculate'
	calcul(raw_input())
	os.system('pause')
	os.system('cls')
	break