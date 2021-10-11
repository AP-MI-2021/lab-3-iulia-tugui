def citireLista():
    '''
    functie care citeste datele
    :return: o lista de numere ce au fost anterior introduse
    '''
    lista = []
    lista_string = []
    raw_data = input("Dati lista:")
    lista_string = raw_data.split()
    for i in lista_string:
        lista.append(int(i))
    return lista


def nr_prim(n):
    '''
    functie care verifica daca un numar este prim
    :param n: numarul pentru care se verifica proprietatea
    :return: True, daca numarul este prim sau False, in caz contrar
    '''
    if n<2:
        return False
    else:
        for i in range (2, n//2+1):
            if n%i==0:
                return False
        return True
def test_nr_prim():
    '''
    functie care testeaza daca functia "verificare_nr_prim" este corecta
    :return:
    '''
    assert(nr_prim(3)==True)
    assert(nr_prim(1)==False)
    assert(nr_prim(29)==True)
    assert(nr_prim(22)==False)
def toate_numerele_prime(lst):
    '''
    functie care determina daca toate numerele sunt prime
    :param lst: o lista de valori pentru care se verifica proprietatea
    :return: True, daca toate numerele sunt prime sau False, in caz contrar
    '''
    for i in lst:
        if nr_prim(i) == False:
            return False
    return True
def test_toate_numerele_prime():
    '''
    functie care testeaza daca functia "toate_numerele_prime" este corecta
    :return:
    '''
    assert (toate_numerele_prime([3,5,11,17])==True)
    assert (toate_numerele_prime([2,3,5,1])==False)
    assert (toate_numerele_prime([2,5,17,0])==False)
def get_longest_all_primes(lst):
    '''
    functie care determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt prime
    :param lst: lista de valori citita cu ajutorul functiei "citireLista"
    :return: cea mai lunga subsecventa cu proprietatea ceruta
    '''
    subsecventa_max1 =[]
    for i in range(len(lst)):
        for j in range(i,len(lst)+1):
            if (toate_numerele_prime(lst[i:j+1]) == True) and len(lst[i:j+1]) > len(subsecventa_max1):
                subsecventa_max1 = lst[i:j+1]
    return subsecventa_max1
def test_get_longest_all_primes():
    '''
    functie care testeaza daca functia "get_longest_all_primes" este corecta
    :return:
    '''
    assert (get_longest_all_primes([1,2,3,4,5,6])==[2,3])
    assert (get_longest_all_primes([1,2,3,5,7,11])==[2,3,5,7,11])
    assert (get_longest_all_primes([1,2,3])==[2,3])


def cifre_prime(n):
    '''
    functie care verifica daca numarul este format din cifre prime
    :param n: numarul pentru care se verifica daca are toate cifrele prime
    :return: True, daca numarul este format din cifre prime sau False, in caz contrar
    '''
    while n>0:
        ultima_cifra = n%10
        if nr_prim(ultima_cifra)==False:
            return False
        n = n//10
    return True
def test_cifre_prime():
    '''
    functie care testeaza daca functia "cifre_prime" este corecta
    :return:
    '''
    assert(cifre_prime(27)==True)
    assert(cifre_prime(243)==False)
    assert(cifre_prime(11)==False)
    assert(cifre_prime(50)==False)
    assert(cifre_prime(53)==True)
def toate_nr_cifre_prime(lst):
    '''
    functie daca determina daca toate numerele sunt formate din cifre prime
    :param lst: o lista de valori pentru care se verifica proprietatea
    :return: True, daca toate numerele sunt formate din cifre prime sau False, in caz contrar
    '''
    for i in lst:
        if cifre_prime(i) == False:
            return False
    return True
def test_toate_nr_cifre_prime():
    '''
    functie care testeaza daca functia "toate_nr_cifre_prime" este corecta
    :return:
    '''
    assert (toate_nr_cifre_prime([12, 33, 72, 57])==False)
    assert (toate_nr_cifre_prime([23, 57, 725])==True)
    assert (toate_nr_cifre_prime([23,25,27,20])==False)
def get_longest_prime_digits(lst):
    '''
    functie care determina cea mai lunga subsecventa care are proprietatea ca toate numerele sunt formate din cifre prime
    :param lst: lista de valori citita cu ajutorul functiei "citireLista"
    :return: cea mai lunga subsecventa cu proprietatea ceruta
    '''
    subsecventa_max2 = []
    for i in range(len(lst)):
        for j in range(i, len(lst) + 1):
            if (toate_nr_cifre_prime(lst[i:j + 1]) == True) and len(lst[i:j + 1]) > len(subsecventa_max2):
                subsecventa_max2 = lst[i:j + 1]
    return subsecventa_max2
def test_get_longest_prime_digits():
    '''
    functie care testeaza daca functia "get_longest_prime_digits" este corecta
    :return:
    '''
    assert (get_longest_prime_digits([121, 23, 533, 70])==[23, 533])
    assert (get_longest_prime_digits([23,7523,55])==[23,7523,55])
    assert (get_longest_prime_digits([12,42,30])==[])

def main():
    test_nr_prim()
    test_toate_numerele_prime()
    test_get_longest_all_primes()
    test_cifre_prime()
    test_toate_nr_cifre_prime()
    test_get_longest_prime_digits()
    lst = []
    shouldRun = True
    while shouldRun:
        print("1. Citire date")
        print("2. Determinare cea mai lunga subsecventa cu proprietatea ca numerele sunt prime")
        print("3. Determinare cea mai lunga subsecventa cu proprietatea ca numerele sunt formate din cifre prime")
        print("4. Iesire")
        option = input("Introduceti optiunea:")
        if option == "4":
            shouldRun = False
        elif option == "1":
            lst = citireLista()
        elif option == "2":
            secventa_nr_prime = get_longest_all_primes(lst)
            print(secventa_nr_prime)
        elif option == "3":
            secventa_nr_cu_cifre_prime = get_longest_prime_digits(lst)
            print(secventa_nr_cu_cifre_prime)
        else:
            print("Optiunea este gresita!")
if __name__ == "__main__":
    main()