# Exercise 1
# Create a function called "devolver_distintos" who receive 3 integers as parameters
def devolver_distintos(num1, num2, num3):
    lista_numeros = [num1, num2, num3]
    lista_numeros.sort()
    suma = 0
    for n in lista_numeros:
        suma += n

    # if the sum of the 3 integers is greather than 15, it gonna return the major number
    if suma > 15:
        return lista_numeros[2]

    # if the sum of the 3 integers is minor than 10, it gonna return the minor number
    elif suma < 10:
        return lista_numeros[0]

    # if the sum of the 3 integers is between 10 and 15, it gonna return the medium value
    else:
        return lista_numeros[1]


print(devolver_distintos(3, 5, 1))


# Exercise 2
# Create a function that receive a word as parameter
def word_info(word):

    # It should return the uniques letters and in alphabetic order
    letters = set(word)
    letters = list(letters)
    letters.sort()
    letters = tuple(letters)
    return letters


print(word_info("bcffxydfhwbwfsdddaaeffghii"))


# Exercise 3
# Create a function who receive a undefined amount of arguments
def zero_check(*args):
    # It should return True if in a moment two zero was enter consecutively and False if not
    flag = 0
    for arg in args:
        if arg == 0:
            flag += 1
        else:
            flag = 0

        if flag == 2:
            return True
        else:
            pass
    return False


print(zero_check(1, 0, 3, 4, 5, 0, 2, 3))


# Exercise 4
# Create a function called contar_primos() who recive just one numeric argument
def contar_primos(numero):
    # This function gonna display every number that is primo in the range of 0 to your number and gonna return the amount of primo number that found. 0 and 1 are not primos
    numeros_primos = [2]
    for n in range(3, numero + 1):
        flag = True
        for number in range(2, n):
            if n % number == 0:
                flag = False
                break

        if flag == True:
            numeros_primos.append(n)
        else:
            pass

    print(numeros_primos)
    print(list(range(2, 2)))


contar_primos(2000)
