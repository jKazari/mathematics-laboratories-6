""" My first module """

def Hello():
    print('Hello World from the cutiest Python module ever!')


def Sleep():
    print('Hrrrr...')

def arithmetic_sequence(a,r,stop):
    return [a*i+r for i in range(1,stop+1)]


# uncomment then import 
#def __dir__():
#return ['Hello','Sleep']   # pitfal

# uncomment then import 
#__all__ = ['Sleep']


# in this set of exercises we add a possibility to execute this file as a script

if __name__ == '__main__':
    print('Hello from WuPeA module!')
    print("I feel like a script")
    print('My name is ' + __name__)          
else:
    print('Hello from WuPeA module!')
    print("I feel like a module") 
    print('My name is ' + __name__)          


# EOF
