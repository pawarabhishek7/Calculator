def add(n1,n2):
	return (n1+n2)

def sub(n1,n2):
	return (n1-n2)

def mlt(n1,n2):
	return (n1*n2)

def div(n1,n2):
	return (n1/n2)

def mdivision(n1,n2):
	return (n1%n2)
print( 'Enter your choice \n 1:add \n 2:sub \n  3: mlt \n 4:div \n 5:mdivision')
while True:

	choice = input('Enter choice:\t')

	if choice in ('1','2','3','4','5'):
		n1 = float(input("n1 value here\t"))
		n2 = float(input("n2 value here\t"))

		if choice == '1':
			print('the sum is:',add(n1,n2))
		elif choice == '2':
			print('the diff is:',sub(n1,n2))
		elif choice == '3':
			print('the mult is :',mlt(n1,n2))
		elif choice == '4':
			print('the div is :',div(n1,n2))
		elif choice == '5':
			print("the md is :",mdivision(n1,n2))
		break
	else:
		print("Invalid input")



