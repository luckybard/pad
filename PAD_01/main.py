#     Ćwiczenie 1

def check_range(x, y, z):
    i = y
    while i <= z:
        if i == x:
            print(str(x) + " jest między " + str(y) + " a " + str(z))
            break
        elif i == z:
            print(str(x) + " nie jest między " + str(y) + " a " + str(z))
        i += 1

check_range(20, 9, 228)
check_range(7, 2, 5)

#     Ćwiczenie 2

def bool_range(x, y, z):
    i = y
    while i <= z:
        if i == x:
                return True
        elif i == z:
            return False
        i += 1

print("Czy podana wartość występuje w zbiorze? Wynik:" + str(bool_range(7, 5, 20)))
print("Czy podane wartość występuje w zbiorze? Wynik:" + str(bool_range(67, 22, 25)))

#     Ćwiczenie 3
def unique_list(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    print("Lista unikalnych elementów -> " + str(unique_elements))

unique_list([1,3,5,6,4,3,2,3,3,4,3,4,5,6,6,4,3,2,12,3,5,63,4,5,3,3,2])

#     Ćwiczenie 4

def objętość_kuli(promień):
        pi = 3.14
        objętość = (4/3) * pi * (promień**3)
        print("Objętość kuli wynosi" +str(round(objętość, 2)))

#     Ćwiczenie 5
def num_fact(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * num_fact(n-1)
print("Silnia dla 10 wynosi " + str(num_fact(10)))
