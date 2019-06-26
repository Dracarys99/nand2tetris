class parser:
    def __init__(self, tokens):
        self.tokens = tokens
        curr_tok = iter(tokens)
        self.parserOutput = []
    def consumetoken(self,spaces):
        self.parserOutput.append(spaces+self.curr_tok)
        self.curr_tok = next(self.curr_tok)
    def compile(self):
        if(self.curr_tok == "<tokens>"):
            self.curr_tok = next(self.curr_tok)
            if(self.curr_tok == "<keyword> class </keyword>"):
                self.parserOutput.append("<class>")
                self.compileClass("  ")
            else:
                print("Error-compile:Expected Class Keyword!!!")
                exit()
        else:
            print("Error-compile:Expected <tokens>!!!")
    def compileClass(self,spaces):
        if(self.curr_tok == "<keyword> class </keyword>"):
            self.consumetoken(spaces)
            if(str(self.curr_tok).startswith("<identifier>")):
                self.consumetoken(spaces)
                if(self.curr_tok == "<symbol> { </symbol>"):
                    self.consumetoken(spaces)
                    
        
