from sly import Parser
from .lexer import MyLexer

class MyParser(Parser):
    debugfile = 'parser.out'
    tokens = MyLexer.tokens

    # ordem: da menor para a maior precendencia
    precedence = (
        ('left', 'EQ'),
        ('left', '+', '-'),        
        ('left', '*', '/'),        
        ('right', 'UMINUS'), 
        # ('right', 'falso'), 
        # ('right', 'vdd'), 
        # ('right', '++'), 
        # ('right', '--'),
        # ('right', 'mod'), 
        # ('right', '!='),  
        )

    def __init__(self):
        self.names = { }

    # funcoes 'statement' não possuem retorno
    # funcoes 'expr' possuem retorno

    @_('ID "=" expr')
    def statement(self, p):
        self.names[p.ID] = p.expr
           
    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr "+" expr') # Soma
    def expr(self, p):
        return p[0] + p[2]

    @_('expr "-" expr') # Subtração
    def expr(self, p):
        return p[0] - p[2]

    @_('expr "*" expr') # Multiplicação
    def expr(self, p):
        return p[0] * p[2]

    @_('expr "/" expr') # Divisão
    def expr(self, p):
        return p[0] / p[2]

    @_('expr EQ expr') # Comparação
    def expr(self, p):
        return p[0] == p[2]

    @_('"-" expr %prec UMINUS') # caso especial, ex.: 5 * -5
    def expr(self, p):
        return -p.expr
    
    @_(' falso ')
    def expr(self, p):
        return False
    
    @_(' vdd ')
    def expr(self, p):
        return True
    
    @_(' expr mod expr ')
    def expr(self, p):
        return p[0] % p[2]
    
    @_(' expr SUM ')
    def expr(self, p):
        return p[0] + 1
    
    @_(' expr SUB ')
    def expr(self, p):
        return p[0] - 1
    
    @_(' expr DIFF expr ')
    def expr(self, p):
        return p[0] != p[2]

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER
        
    @_('ID')
    def expr(self, p):
        try:
            return self.names[p.ID]
        except LookupError:
            print('ID <{}> indefinido'.format(p.ID))
            return 0
        
        

    
