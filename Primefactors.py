# A function to find the prime factors of a number
def get_prime_factors(number):
    factors = list()
    divisor = 2
    while (divisor <= number):
        if (number % divisor) == 0:
          factors.append(divisor)
          number = number/divisor
        else:
          divisor += 1
    return factors
  
# call the function with print 
print(get_prime_factors(77))


