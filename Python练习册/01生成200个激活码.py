import random
import string



def cdkey(num):
	s = set()
	while len(s) < num:
		code = random.sample(string.ascii_uppercase+string.digits,6)
		s.add(''.join(code))
	return s

