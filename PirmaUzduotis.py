# Pirma

class first:
    def combine(self):
        try:
            x=[1, 2, 3, 4, 5, 100, 200, 300, 1000]
            y=[100, 1000, 250, 200, 2, 2]
            combined=x+y
            combined.sort()
            print('Sujungtas ir surūšiuotas sąrašas: ' + str(combined))
        except:
            print('Bandykite iš naujo!')

f = first()
f.combine()