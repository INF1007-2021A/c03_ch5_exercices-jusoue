#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1
    else: 
        number *= 1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    result = []
    for letter in prefixes:
        letter += suffixe
        result.append(letter)
    return result


def prime_integer_summation() -> int:
    prime_numbers = []
    
    return print(prime_numbers)


def factorial(number: int) -> int:
    result = 1
    for number1 in range(1, number + 1):
        result *= number1
    return result


def use_continue() -> None:
    for number in range(1, 11):
        if(number != 5):
            print(number)
            continue
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    verif = True
    verifications = []
    for group in groups:
        if 3 >= len(group) > 10:
            verif = False
            verifications.append(verif)
        else:
            for number in group:
                if number == 25:
                    verif = True
                    break
                if number < 18:
                    verif = False
                    continue
                if number > 70:
                    for group in groups:
                        if number == 50:
                            verif = False
                else:
                    verif = True
        verifications.append(verif)
    return verifications


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
