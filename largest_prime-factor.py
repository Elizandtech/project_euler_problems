#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
    ## Create list of all factors, create list of primes, then find the largest factor from the list.

def is_prime(inp):
    isprime = True
    for div in range(2, int(math.sqrt(inp)+1)):
        if inp % div== 0:
            isprime=False
            break
    return isprime


def print_prime_numbers(inp):
    for testnumber in range(2, inp+1):
        if is_prime(testnumber):
            print(testnumber)
