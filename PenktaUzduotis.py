# Penkta
import traceback
class fifth:
    def get_input(self):
        try:
            number=int(input("Įveskite skaičių: "))
            self.dictionary(number)
        except Exception:
            traceback.print_exc()
    def dictionary(self, number):
        try:
            number_dictionary=dict()
            for i in range (number+1):
                number_dictionary[i] = i*2
            print(str(number_dictionary))
        except:
            print('Bandykite iš naujo!')
fif = fifth()
fif.get_input()