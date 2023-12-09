#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer).
    """

    veryunique_integers = set()

     for num in my_list:
        veryunique_integers.add(num)

         sum_veryunique = sum(veryunique_integers)

         return sum_veryunique

