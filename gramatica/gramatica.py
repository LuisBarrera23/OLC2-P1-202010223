import ply.yacc as yacc



from src.Expresion.Operaciones import Operacion,TIPO_OPERACION
from src.Abstract.RetornoType import TipoDato
from src.Expresion.Primitivo import Primitivo

from src.Instruccion.Print import Print


from src.Expresion.casteo import Casteo



reservadas = {
    'f64' : 'F64',
    'i64' : 'I64',
    'bool' : 'BOOL',
    'char' : 'CHAR',
    '&str' : 'STR',
    'string' : 'STRING',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'pow' : 'POW',
    'powf' : 'POWF',
    'println' : 'PRINTLN',
    'as' : 'AS',
    'to_string' : 'TOSTRING',
    'to_owned' : 'TOOWNED'
}

tokens = [
             'DOBLEPT',
             'PTCOMA',
             'COMA',
             'PUNTO',
             'PIZQ',
             'PDER',
             'CORIZQ',
             'CORDER',

             'AND',
             'OR',
             'NOT',

             'MAYORIGUAL',
             'MENOR',
             'MENORIGUAL',
             'MAYOR',
             'IGUALIGUAL',
             'DIFERENTE',
             'IGUAL',

             'MAS',
             'MENOS',
             'DIVISION',
             'MULTIPLICACION',
             'MODULO',
             'DECIMAL',
             'ENTERO',
             'ID',
             'CADENA'
         ] + list(reservadas.values())

# definir tokens
t_DOBLEPT = r'\:'
t_PTCOMA = r';'
t_COMA = r','
t_PUNTO = r'\.'
t_PIZQ = r'\('
t_PDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'

t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'

t_MENOR = r'\<'
t_MAYOR = r'\>'
t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_IGUALIGUAL = r'\=\='
t_DIFERENTE = r'\!\='
t_IGUAL = r'\='

t_MAS = r'\+'
t_MENOS = r'-'
t_DIVISION = r'/'
t_MULTIPLICACION = r'\*'
t_MODULO = r'\%'

def t_DECIMAL(t):
    r"""\d+\.\d+"""
    try:
        t.value = float(t.value)
    except ValueError:
        t.value = 0.0
    return t


def t_ENTERO(t):
    r"""\d+"""
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = 0
    return t


def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z0-9_]*"""
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t


def t_CADENA(t):
    """\".*?\""""
    t.value = t.value[1:-1]  # Eliminar las comillas dobles
    return t


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1


t_ignore = " \t\r"


def t_newLine(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print(f"Se encontro un error lexico {t.value[0]}")
    t.lexer.skip(1)

def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# creando el lexer
import ply.lex as lex

lexer = lex.lex()

# *************************** SECCION DE ANALIZADOR SINTACTICO  (parser) ************************** 
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'MAYOR', 'MENORIGUAL', 'MENOR', 'MAYORIGUAL', 'IGUALIGUAL', 'DIFERENTE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('right', 'NOT', 'UMENOS')
)

def p_init(t):
    """init : instrucciones"""
    t[0]=t[1]

def p_instrucciones(t):
    """instrucciones : instrucciones instruccion"""
    t[1].append(t[2])
    t[0]=t[1]

def p_instrucciones_instruccion(t):
    """instrucciones : instruccion"""
    t[0]=[t[1]]

def p_instruccion(t):
    """instruccion : print"""
    t[0]=t[1]

def p_print(t):
    """print : PRINTLN NOT PIZQ expresion PDER PTCOMA"""
    t[0]=Print(t[4],t.lexer.lineno,find_column(entrada,t.slice[1]))


def p_expresion_aritmetica(t):
    """expresion : MENOS expresion %prec UMENOS
                | expresion MAS expresion
                | expresion MENOS expresion
                | expresion MULTIPLICACION expresion
                | expresion DIVISION expresion
                | expresion MODULO expresion
                | I64 DOBLEPT DOBLEPT POW PIZQ expresion COMA expresion PDER 
                | F64 DOBLEPT DOBLEPT POWF PIZQ expresion COMA expresion PDER 
                | PIZQ expresion PDER"""
    
    if len(t) == 3:
        t[0] = Operacion(t[2], TIPO_OPERACION.RESTA, None, True,t.lexer.lineno,find_column(entrada,t.slice[1]))
    elif len(t)==10 and t[1]=="i64":
        t[0]=Operacion(t[6],TIPO_OPERACION.POTENCIA,t[8],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        t[0].tipo2=TipoDato.I64
    elif len(t)==10 and t[1]=="f64":
        t[0]=Operacion(t[6],TIPO_OPERACION.POTENCIA,t[8],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        t[0].tipo2=TipoDato.F64
    elif t[1] == '(':
        t[0] = t[2]
    else:
        if t[2] == '+':
            t[0] = Operacion(t[1], TIPO_OPERACION.SUMA, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        elif t[2] == '-':
            t[0] = Operacion(t[1], TIPO_OPERACION.RESTA, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        elif t[2] == '*':
            t[0] = Operacion(t[1], TIPO_OPERACION.MULTIPLICACION, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        elif t[2] == '/':
            t[0] = Operacion(t[1], TIPO_OPERACION.DIVISION, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        elif t[2] == '%':
            t[0] = Operacion(t[1], TIPO_OPERACION.MODULO, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))

def p_expresion_relacionalesLogicas(t):
    """expresion : expresion MAYOR expresion
                | expresion MENOR expresion
                | expresion MAYORIGUAL expresion
                | expresion MENORIGUAL expresion
                | expresion IGUALIGUAL expresion
                | expresion DIFERENTE expresion
                | expresion AND expresion
                | expresion OR expresion
                | NOT expresion"""
    
    if len(t) == 3:
        t[0] = Operacion(t[2], TIPO_OPERACION.NOT, None, True,t.lexer.lineno,find_column(entrada,t.slice[1]))
    else:
        if t[2] == '>':
            t[0] = Operacion(t[1], TIPO_OPERACION.MAYOR, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        elif t[2] == '<':
            t[0] = Operacion(t[1], TIPO_OPERACION.MENOR, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        elif t[2] == '>=':
            t[0] = Operacion(t[1], TIPO_OPERACION.MAYORIGUAL, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        elif t[2] == '<=':
            t[0] = Operacion(t[1], TIPO_OPERACION.MENORIGUAL, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        elif t[2] == '==':
            t[0] = Operacion(t[1], TIPO_OPERACION.IGUALIGUAL, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        elif t[2] == '!=':
            t[0] = Operacion(t[1], TIPO_OPERACION.DIFERENTE, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        elif t[2] == '&&':
            t[0] = Operacion(t[1], TIPO_OPERACION.AND, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))
        elif t[2] == '||':
            t[0] = Operacion(t[1], TIPO_OPERACION.OR, t[3],False,t.lexer.lineno,find_column(entrada,t.slice[2]))

def p_expresiones_variadas(t):
    """expresion : tostring
                | as"""
    t[0]=t[1]

def p_tostring(t):
    """tostring : expresion PUNTO TOSTRING PIZQ PDER
                | expresion PUNTO TOOWNED PIZQ PDER"""

    t[0]=Casteo(t[1],t.lexer.lineno,find_column(entrada,t.slice[2]))

def p_as(t):
    """as : expresion AS I64 
        | expresion AS F64 """
    
    if(t[3]=="i64"):
        t[0]=Casteo(t[1],t.lexer.lineno,find_column(entrada,t.slice[2]),TipoDato.I64)
    elif(t[3]=="f64"):
        t[0]=Casteo(t[1],t.lexer.lineno,find_column(entrada,t.slice[2]),TipoDato.F64)

    
def p_expresion_primitiva(t):
    """expresion : ENTERO
                    | DECIMAL
                    | ID
                    | CADENA
                    | TRUE
                    | FALSE"""

    if t.slice[1].type == 'ENTERO':
        t[0] = Primitivo(t[1],TipoDato.I64)
    elif t.slice[1].type == 'DECIMAL':
        t[0] = Primitivo(t[1], TipoDato.F64)
    elif t.slice[1].type == 'ID':
        print(t[1])
        #t[0] = Identificador(t[1])
    elif t.slice[1].type == 'CADENA':
        t[0] = Primitivo(t[1], TipoDato.STR)
    elif t.slice[1].type == 'TRUE':
        t[0] = Primitivo(True, TipoDato.BOOL)
    elif t.slice[1].type == 'FALSE':
        t[0] = Primitivo(False, TipoDato.BOOL)


def p_error(t):
    print(f"SE ENCONTRO UN ERROR {t} En linea {t.lexer.lineno} columna {find_column(entrada,t)}")

parser = yacc.yacc()
entrada=""


def parse(input):
    global lexer,entrada
    entrada=input
    lexer = lex.lex()
    return parser.parse(input)