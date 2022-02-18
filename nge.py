<<<<<<< HEAD
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, x):
    stack.append(x)

def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()

def printNGE(arr):
    s = createStack()
    element = 0
    next = 0


    push(s,arr[0])

    for i in range(1,len(arr),1):
        next = arr[i]

        if isEmpty(s) == False:
            element = pop(s)


            while element < next:
                print(str(element) + "--" + str(next))
                if isEmpty(s) == True:
                    break
                element = pop(s)


            if element > next:
                push(s,element)

        push(s,next)


    while isEmpty(s) == False:
        element = pop(s)
        next = -1
        print(str(element) + "--" + str(next))


val = []
n = int(input("Enter the number of elements"))

for i in range(0,n):
    ele = int(input())
    val.append(ele)

for i in range(0,n):
    print(int(val[i])+"ok")

printNGE(val)

        
        
         
=======
# Python program to print next greater element using stack



def createStack():
	stack = []
	return stack


def isEmpty(stack):
	return len(stack) == 0


def push(stack, x):
	stack.append(x)


def pop(stack):
	if isEmpty(stack):
		print("Error : stack underflow")
	else:
		return stack.pop()




def printNGE(arr):
	s = createStack()
	element = 0
	next = 0


	push(s, arr[0])

	for i in range(1, len(arr), 1):
		next = arr[i]

		if isEmpty(s) == False:


			element = pop(s)

			
			while element < next:
				print(str(element) + " -- " + str(next))
				if isEmpty(s) == True:
					break
				element = pop(s)

			
			if element > next:
				push(s, element)
				
		push(s, next)

	while isEmpty(s) == False:
		element = pop(s)
		next = -1
		print(str(element) + " -- " + str(next))


arr = [11, 13, 21, 3]

val = []
n = int(input("Enter the number of elements"))

for i in range(0, n):
	ele = int(input())
	val.append(ele)


#print(val)
for i in range(0, n):
	print(str(val[i])+"ok")


printNGE(val)



>>>>>>> f6c02ee2da16cea06b9c8e7abf8dbaf29ee0e79f
