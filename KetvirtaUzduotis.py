# Ketvirta

class fourth:
    def symbol_replacement(self):
        try:
            rules = {
                ".": " ",
                ",": ".",
                "!": "?",
                "a": "A"
            }
            line_for_replacement = "Sveiki, esu Dominykas! Tai yra testas."
            for key, value in rules.items():
                line_for_replacement=line_for_replacement.replace(key, value)
            print(line_for_replacement)
        except:
            print('Bandykite iš naujo!')

fo = fourth()
fo.symbol_replacement()