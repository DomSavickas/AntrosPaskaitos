# Antra

class second:
    def find_numbers(self):
        try:
            lower_range=2000
            upper_range=4000
            for number in range (lower_range,upper_range +1):
                if (number%7==0) and (number%5!=0):
                    print(number)
        except:
            print('Bandykite iš naujo!')

s = second()
s.find_numbers()