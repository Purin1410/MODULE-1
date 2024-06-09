
def exercise_1(tp, fp, fn):
	if type(tp) != int:
		print('tp must be int')
	elif type(fp) != int:
		print('fp must be int')
	elif type(fn) != int:
		print('fn must be int')
	elif num <=0:
		print('tp and fp and fn must be greater than zero')
	else:
		precision = tp/ (tp+fp)
		recall = tp/ (tp+fn)
		F1_score = 2*(precision*recall)/ (precision+ recall)
		print('Precision is: ',precision)
		print('Recall is: ',recall)
		print('F1_score is: ',F1_score)

exercise_1(tp = 2,fp = 3, fn=4)
