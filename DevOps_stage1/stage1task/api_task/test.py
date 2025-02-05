from sympy import isprime, is_perfect, simplify

class mathser():

    def is_armstrong(self, number):
        nod = len(str(number))

        sum = 0

        for digit in str(number):
            sum += int(digit) ** nod
        if sum == number:
            return True
        else:
            return False


    def get_properties(self, number):

        properties = [] #initialize an empty properties list

        if self.is_armstrong(number):
            properties.append("armstrong")
        else: pass

        if simplify(number).is_even:
            properties.append("even")
        else:
            properties.append("odd")
        
        return properties

calc = mathser()

print(calc.get_properties(371))