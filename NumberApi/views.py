""" API Views"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import math



def is_prime(num):
    """ check if number is prime"""
    # numbers less than 2 are not prime
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # for i in range of 2 to the square root of the number
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    """ checks if the number is a perfect number"""
    # return the sum of the factors of the number
    return num == sum(i for i in range(1, num) if num % i == 0)

def is_armstrong(num):
    """ checks if the number is an armstrong number"""
    # make a list of the digits of the number
    digits = [int(digit) for digit in str(num)]
    # calaculate the power of the num based on the digits
    power = len(digits)
    # raise each digit to the power and sum them
    # if the sum is equal to the number, then it is an armstrong number
    return num == sum(digit ** power for digit in digits) == num

class NumberApi(APIView):
    """ APiView"""
    def get(self, request):
        """ Get Method to return the status and funfact"""
        # Get the number from the request
        number = request.query_params.get('number', None)
        
        # Check if the number is present
        try:
            number = int(number)
        except (ValueError, TypeError):
            return Response({
                "number": "alphabet",
                "error": True
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the number is negative
        if number < 0:
            return Response({
                "number": "negative",
                "error": True
            }, status=status.HTTP_400_BAD_REQUEST)
            
        # get the sum of number
        sum_of_digits = sum(int(digit) for digit in str(number))
        
        is_prime_number = is_prime(number)
        is_perfect_number = is_perfect(number)
        is_armstrong_number = is_armstrong(number)
        
        # combine the property list
        properties = []
        if is_armstrong_number:
            properties.append("armstrong")
        # use odd or even base on number
        properties.append("even" if number % 2 == 0 else "odd")
        
        # Get fun fact from the number api
        fun_fact_url = f'http://numbersapi.com/{number}/math'
        try:
            fun_fact = requests.get(fun_fact_url).text
        except requests.exceptions.RequestException:
            fun_fact = "No Fun Fact for this number"
        
        data = {
            "number": number,
            "is_prime": is_prime_number,
            "is_perfect": is_perfect_number,
            "properties": properties,
            "digit_sum": sum_of_digits,
            "fun_fact": fun_fact,
        }
        # return the data
        return Response(data, status=status.HTTP_200_OK)
        
        
        
        