np.array(object, dtype=None, ndmin=0)// khởi tạo ma trận
Matrix_name[row_index, column_index]
# khời tạo một vector
	import numpy as np #import numpy and uses shorter keyword
	_a = [ 1, 2, 3, 4 ] #array-like object  
	a = np.array(_a) #create a 1-dimension array (vector) from _a 
	print(‘Vector 4 chiều:’, a) #print vector a

# cộng trừ hai ma trận có kích thước giống nhau
	import numpy as np
	_a = [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
	_b = [ [ 2, 3, 5], [7, 9, 21] ]
	a = np.array(_a) #create 2 * 3 matrix: a
	b = np.array(_b) #create 2 * 3 matrix: b
	print(‘a + b:’, a + b) #print out a + b
	print(‘a – b:’, a – b) #print out a - b

# Nhân chia ma trận với một số
	import numpy as np
	_a = [ [ 3, 2, 1 ], [ 2, 4, 6 ] ]
	a = np.array(_a)
	print(‘a / 2:’, a / 2) #print out a / 2
	print(‘a * 2:’, a * 2) #print out a * 2

# Nhân ma trận với một vector
	Matrix_name.dot(vector)
	vd:
		import numpy as np
		_a = [ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ] ]
		a = np.array(_a) #Create a 3 * 2 matrix
		_b = [ 1, 2 ]
		b = np.array(_b) #Create a 2-dimension vector
		print(a)
		print(b)
		print(‘a * b:’, a.dot(b)) #print out a * b using narray.dot()
		print(‘a * b:’, a @ b) #print out a * b using @ operation

#Nhân ma trận với ma trận
	Matrix1.dot(matrix2)
	np.dot(Matrix1,Matrix2)
	vd: 
		import numpy as np
	_a = [ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ] ]
	a = np.array(_a) #Create a 3 * 2 matrix
	_b = [ [1, 3], [2, 1] ]
	b = np.array(_b) #Create a 2 * 2 matrix
	print(a)
	print(b)
	print(‘a * b:’, a.dot(b)) #print out a * b using narray.dot()
	print(‘a * b:’, a @ b) #print out a * b using @ operation

# khởi tạo một ma trận đơn vị
	np.eye(x)

# Ma trận khả nghịch 
	np.linalg.pinv(matrix)
	vd: 
		import numpy as np
		_a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
		a = np.array(_a)
		 #Create inverse of a
		print(a_i)
		print(a @ a_i)

#Ma trận chuyển vị
	np.transpose(a)

# Hàm sum và max/min với ma trận
	np.sum(matrix,axis)

	np.max(matrix,axis)

	np.min(matrix,axis)

    axix: chiều , nếu là 0 thì sẽ tính theo cột, nếu là 1 thì sẽ tính theo hàng

# thêm phần tử vào cuổi mảng array- python sẽ tạo ra một mảng mới chứ ko thay d
#đổi giá trị của mảng ban đầu
	vd: 
		a = np.array([1,2,3,4])
		b = np.append(a,[5])
		-> b = [1,2,3,4,5]

# Nối hai ma trận 
	np.concatenate((matrix1, matrix2),axis = 0/1)
	axis == 0: nối theo hàng
	axis == 1: nối theo cột

	vd: a = np.array([[1, 2], [3, 4]])
	b = np.array([[5, 6]])
	np.concatenate((a, b), axis=0)
	array([[1, 2],
	       [3, 4],
	       [5, 6]])
	np.concatenate((a, b.T), axis=1)
	array([[1, 2, 5],
	       [3, 4, 6]])
	np.concatenate((a, b), axis=None)
	array([1, 2, 3, 4, 5, 6])