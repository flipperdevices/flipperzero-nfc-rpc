import readline

class Completer(dict):
    def __init__(self, dict):
        self.dict = dict
        readline.set_completer(self.complete)
        readline.parse_and_bind("tab: complete")

    
    def complete(self, text, state):
        options = [c for c in self.dict.keys() if c.startswith(text)]
        try:
            return options[state]
        except IndexError:
            return None