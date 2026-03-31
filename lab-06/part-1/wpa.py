""" My first module """

def Hello():
    print('Hello World from the cutiest Python module ever :3')

def Sleep():
    print('Hrrrr...')

def arithmetic_sequence(a,r,stop):
    return [a*i+r for i in range(1,stop+1)]

# def __dir__():
#     return ['Hello','Sleep']

# __all__ = ['Sleep']

if __name__ == '__main__':
    Hello()
    print("I think I will go to sleep")
    for i in arithmetic_sequence(1, 0, 10):
        print(f'{i} owieczka')
    Sleep()
else:
    Hello()
