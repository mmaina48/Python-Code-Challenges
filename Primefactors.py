import re

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
# print(get_prime_factors(77))


# Write a function to determine if a given string is palindrome
def is_palindrome(string):
  
  '''This function input is a string
     Output: Boolean value
     Only consider letter(A-Z)
     ingore case(A == a) '''
     
  lowercase_string = string.lower()
  char_only_string = ''.join(char for char in lowercase_string if char.isalpha())
  return True if char_only_string == char_only_string[::-1] else False
  
# Alternative funtion
def is_palindrome2(phrase):
  forword = ''.join(re.findall(r'[a-z]+', phrase.lower()))
  backwards = forword[::-1]
  return forword == backwards

print(is_palindrome('GO hang a alami - Im a lasagna hog.'))
     
