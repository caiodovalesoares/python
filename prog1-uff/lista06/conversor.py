def strToInt(string):
    value = 0
    for i in range(len(string)):
        match i:
            case 0: exp = 100000
            case 1: exp = 10000
            case 2: exp = 1000
            case 3: exp = 100
            case 4: exp = 10
            case 5: exp = 1
        match string[i]:
            case '0': continue
            case '1': value += 1*exp
            case '2': value += 2*exp
            case '3': value += 3*exp
            case '4': value += 4*exp
            case '5': value += 5*exp
            case '6': value += 6*exp
            case '7': value += 7*exp
            case '8': value += 8*exp
            case '9': value += 9*exp
        
    return value

string = input('Digite um número de 6 algarismos: ')
print(strToInt(string))