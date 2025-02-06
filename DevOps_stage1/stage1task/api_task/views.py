import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from bs4 import BeautifulSoup

from sympy import isprime, is_perfect, simplify


class ClassifyNumber(APIView):
    
    def get(self, request, format=None):

        """
        returns json object containing details about the number specified in the GET request
        """

        #Get number in the request's query parameter from the request object, ensuring it is a valid integer
        try:
            query_param = request.GET.get("number", "")
            number = int(query_param.lstrip('-'))  #using lstrip ensures negative integers are accepted but "cleaned"

        except ValueError:
            return Response({
                "number": "alphabet",
                "error": True,
            }, status=status.HTTP_400_BAD_REQUEST)

        else:
            #use requests, beautifulsoup to retrieve the corresponding html fun fact page for the number's math type
            html_doc = requests.get(f"http://numbersapi.com/{number}/math").text

            soup = BeautifulSoup(html_doc, "lxml")

            #create a python dictionary to hold the facts about the number
            number_details = {
                "number": number,
                "is_prime": isprime(number),
                "is_perfect": is_perfect(number),
                "properties": self.get_properties(number),
                "digit_sum": self.get_digits_sum(number),
                "funfact": soup.get_text()
            }

            #return the facts serialized as a JSON resonse 
            return Response(number_details)


    #function that returns the sum of digits of a number
    def get_digits_sum(self, number):

        sum = 0

        for digit in str(number):
            sum+= int(digit)

        return sum


    #function that checks the armstrong property of a number
    def is_armstrong(self, number):
        nod = len(str(number))

        sum = 0

        for digit in str(number):
            sum += int(digit) ** nod

        if sum == number:
            return True
        else:
            return False


    #function that returns a list of properties of a number (armstrong and/or even/odd)
    def get_properties(self, number):

        properties = []

        if self.is_armstrong(number):
            properties.append("armstrong")
        else: pass

        if simplify(number).is_even:
            properties.append("even")
        else:
            properties.append("odd")
        
        return properties

