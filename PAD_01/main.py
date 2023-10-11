
def check_range(valueToFind,start,end):
    i = start
    while i <= end:
        if i == valueToFind:
            print(str(valueToFind) + " jest między " + str(start) + " a " + str(end))
            break
        elif i == end:
            print(str(valueToFind) + " nie jest między " + str(start) + " a " + str(end))
        i += 1

check_range(20, 9, 228)
check_range(7, 2, 5)
def bool_range(valueToFind,start,end):
    i = start
    while i <= end:
        if i == valueToFind:
                return True
        elif i == end:
            return False
        i += 1

print("Czy podana wartość występuje w zbiorze? Wynik:" + str(bool_range(7, 5, 20)))
print("Czy podane wartość występuje w zbiorze? Wynik:" + str(bool_range(67, 22, 25)))

def unique_list(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    print("Lista unikalnych elementów -> " + str(unique_elements))

unique_list([1,3,5,6,4,3,2,3,3,4,3,4,5,6,6,4,3,2,12,3,5,63,4,5,3,3,2])

def objętość_kuli(promień):
        pi = 3.14
        objętość = (4/3) * pi * (promień**3)
        print("Objętość kuli wynosi" +str(round(objętość, 2)))
def num_fact(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * num_fact(n-1)
print("Silnia dla 10 wynosi " + str(num_fact(10)))
