import random
import math

def excercise3():
	num_samples = input("Enter the number of samples: ")
	loss_name = input("Enter the loss name (MAE, MSE, RMSE): ")
	if not num_samples.isnumeric():
		print('Number of samples must be an integer number')
		return False

	num_samples = int(num_samples)
	predicts = []
	targets = []
	for i in range(num_samples):
		predict = random.uniform(0, 10)
		target = random.uniform(0, 10)
		predicts.append(predict)
		targets.append(target)
	if loss_name == 'MAE':
		loss = sum(abs(y - y_hat) for y, y_hat in zip(targets, predicts)) / num_samples
	elif loss_name == 'MSE':
		loss = sum((y - y_hat) ** 2 for y, y_hat in zip(targets, predicts)) / num_samples
	elif loss_name == 'RMSE':
		mse = sum((y - y_hat) ** 2 for y, y_hat in zip(targets, predicts)) / num_samples
		loss = math.sqrt(mse)
	else:
		print(f'{loss_name} is not supported')
		return
	print(f'Input loss name: {loss_name}')
	for i in range(num_samples):
		print(f'Load name: {loss_name}, Sample-{i}, Predict = {predicts[i]:.4f}, Target = {targets[i]:.4f}')
		print(f'Loss: {loss:.4f}')
	print(f'Final {loss_name}: {loss:.4f}')


