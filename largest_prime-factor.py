#The prime factors of 13195 are 5, 7, 13 and 29. (Use as check for code)
    ## Create list of prime factors and then find the largest factor from the list.

import math

def is_prime(inp):
    isprime = True
    for div in range(2, int(math.sqrt(inp)+1)):
        if inp % div== 0:
            isprime=False
            break
    return isprime


def return_prime_numbers_in_a_list(lst):
    return [testnumber for testnumber in lst if is_prime(testnumber)]


def return_largest_element_in_list(lst):
    largest_element = 0
    for elem in lst:
        if elem > largest_element:
            largest_element = elem
    return largest_element


def main():
    number_to_factor = int(input("Enter a number: "))
    factors = [factor for factor in range(2, number_to_factor+1) if number_to_factor % factor ==0]
    print(return_largest_element_in_list(return_prime_numbers_in_a_list(factors)))

if __name__=="__main__":
    main()

