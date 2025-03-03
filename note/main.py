
def check_input(user_txt):
	return not any(char.isdigit() for char in user_txt)


def hello(name):
		if check_input(name):
			print("Hello")
		else:
			print("enter")
			user = input("Name")
			hello(user)
user = input("What is your name?:")
			

def fun1():
    msg = "This is thr outer function"

    def fun2():
	    print(msg)
	
    fun2()
	
fun1        ()



def  fun(a):

#outer function rembers the vuale of a 

    def adder(b):
        return a+b
    return adder # return the closure

val = fun(10)#cakk outer function and set a

print(val(5)) #call inner function set b



def end(income):
	
    def calc(cost, type):
        percent = cost/income
        print(f"your {type} is ${cost:.2f} and that is {percent:.0f}")
    return calc

def user_input(type):
    return int(input(f"What is your nonthtly?{type}:$"))
income = user_input("Incone")
rent = user_input("rent")
utilites = user_input("utilities")
transportation = user_input("transportation")

ready = end(income)
ready(rent,"rent")
ready(utilites,"Utillites")
ready(transportation,"transportation")