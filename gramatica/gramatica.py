import ply.yacc as yacc

reservadas = {
    'f64': 'F64',
    'i64':'I64',
    'bool':'BOOL',
    'char':'CHAR',
    '&str':'STR',
    'string':'STRING',
    'println!': 'PRINTLN',
    'true': 'TRUE',
    'false': 'FALSE',
}

tokens = [
             'DOBLEPT',
             'PTCOMA',
             'COMA',
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
             'DECIMAL',
             'ENTERO',
             'ID',
             'STRING'
         ] + list(reservadas.values())

# definir tokens
t_DOBLEPT = r'\:'
t_PTCOMA = r';'
t_COMA = r','
t_PIZQ = r'\('
t_PDER = r'\)'
t_CORIZQ = r'\{'
t_CORDER = r'\}'

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


def t_STRING(t):
    """\".*?\""""
    t.value = t.value[1:-1]  # Eliminar las comillas dobles
    return  t

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

# creando el lexer
import ply.lex as lex

lexer = lex.lex()

# *************************** SECCION DE ANALIZADOR SINTACTICO  (parser) ************************** 
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'MAYOR', 'MENORIGUAL', 'MENOR', 'MAYORIGUAL', 'IGUALIGUAL', 'DIFERENTE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('right', 'NOT', 'UMENOS')
)