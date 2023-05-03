c=40

def abc():
    print('Good message')

#dunder
if __name__=='__main__':
    print('main se call')
    a=int(input('Enter the first value:'))
    b=int(input('Enter second value:'))
    print(c*(a+b))


#the dunder part will execute only when this myfile.py runs not when this myfile is imported in another file