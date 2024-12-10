string = str(input('Digite alguma coisa: '))

if string.isalpha() == True:
    print('A string possui apenas letras!')
elif string.isdigit() == True:
    print('A string possui apenas números!')
if string.isalpha() == False and string.isdigit() == False:
    print('A string possui letras e números combinados!')