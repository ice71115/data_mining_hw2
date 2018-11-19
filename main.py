from svmutil import *	
y, x = svm_read_problem('training.txt')
yt, xt = svm_read_problem('test.txt')
model = svm_train(y, x,'-t 0')
a,linear_accuracy,b=svm_predict(y, x, model)


