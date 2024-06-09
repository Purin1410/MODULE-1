import numpy as np
def is_number(n):
	try:
		float(n)
	except ValueError:
		return False
	return True

def exercise_2():
	x = input()
	if not is_number(x):
		print('x must be a number')
		return False

	activation_fuction = input()
	activation_fuction = 'elu'
	supported_activations = ['sigmoid', 'relu', 'elu']
	if activation_fuction not in supported_activations:
		print(f'{activation_fuction} is not supported.')
		return False
	x = float(x)

	if activation_fuction == 'sigmoid':
		sigmoid = 1 / (1 + np.exp(-x))
		print(f'sigmoid: f({x}) = ',sigmoid)
	elif activation_fuction == 'relu':
		relu = (x if x>0 else 0)
		print(f'relu: f({x}) = ',relu)
	else:
		elu =  (x if x>0 else 0.01*(np.exp(x) - 1))
		print(f'elu: f({x}) = ',elu)


