'''function that accepts variable func1( ) so that it can accept a variable length of
arguments and print all the argumnet values'''
def func1(*num):
     for i in num:
          print(i)

func1(20, 40, 60)
func1(80, 100)