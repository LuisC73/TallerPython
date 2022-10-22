print()

getLargest = lambda numberOne, numberTwo: 1 if numberOne > numberTwo else -1
showMessage = lambda result : print('The first number is largest') if result == 1 else print('The second number is largest')

numberOne = float(input('Enter the first number: '))
numberTwo = float(input('Enter the second number: '))

showMessage( getLargest( numberOne, numberTwo ) )

print()