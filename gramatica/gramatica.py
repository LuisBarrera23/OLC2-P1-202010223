import ply.yacc as yacc



from src.Expresion.Operaciones import Operacion,TIPO_OPERACION
from src.Abstract.RetornoType import TipoDato
from src.Expresion.Primitivo import Primitivo

from src.Instruccion.Print import Print
from src.Instruccion.Declaracion import Declaracion
from src.Instruccion.Asignacion import Asignacion
from src.Instruccion.If_i import If_i
from src.Instruccion.Funcion import Funcion
from src.Instruccion.Llamada import Llamada
from src.Instruccion.Return import Return
from src.Instruccion.Break import Break
from src.Instruccion.Loop import Loop
from src.Instruccion.While import While
from src.Instruccion.Continue import Continue
from src.Instruccion.For import For


from src.Expresion.casteo import Casteo
from src.Expresion.AccesoSimbolo import AccesoSimbolo
from src.Expresion.If_e import If_e

from src.Symbol.Parametro import Parametro



reservadas = {
    'f64' : 'F64',
    'i64' : 'I64',
    'bool' : 'BOOL',
    'char' : 'CHAR',
    'str' : 'STR',
    'String' : 'STRING',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'pow' : 'POW',
    'powf' : 'POWF',
    'println' : 'PRINTLN',
    'as' : 'AS',
    'to_string' : 'TOSTRING',
    'to_owned' : 'TOOWNED',
    'let' : 'LET',
    'mut' : 'MUT',
    'if' : 'IF',
    'else' : 'ELSE',
    'fn' : 'FN',
    'return' : 'RETURN',
    'break' : 'BREAK',
    'loop' : 'LOOP',
    'while' : 'WHILE',
    'continue' : 'CONTINUE',
    'for' : 'FOR',
    'in' : 'IN',
    'chars' : 'CHARS'
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
             'LLAVEIZQ',
             'LLAVEDER',

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
             'CADENA',
             'CARACTER',
             'FLECHA',
             'Y'
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
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'

t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'

t_Y = r'\&'

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
t_FLECHA = r'->'

def t_DECIMAL(t):
    r"""\d+\.\d+"""
    try:
        t.value = float(t.value)
    except ValueError:
        t.value = 0.0
    return t

def t_CARACTER(t):
    r'(\'([a-zA-Z]|\\\'|\\"|\\t|\\n|\\\\|.)\')' # expresion regualar

    t.value = t.value[1:-1]
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
    t.type = reservadas.get(t.value, 'ID')
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
    """init : funciones_structs"""
    t[0]=t[1]

def p_funciones_structs(t):
    """funciones_structs : funciones_structs funcion_struct"""
    t[1].append(t[2])
    t[0]=t[1]

def p_funciones_structs_corte(t):
    """funciones_structs : funcion_struct """
    t[0] = [t[1]]

def p_funcion_struct(t):
    """funcion_struct : funcion"""
    t[0]=t[1]

def p_funcion(t):
    """funcion : FN ID PIZQ PDER bloque
                | FN ID PIZQ PDER FLECHA tipo_dato bloque
                | FN ID PIZQ parametros PDER bloque
                | FN ID PIZQ parametros PDER FLECHA tipo_dato bloque """
    if len(t)==6:
        t[0] = Funcion(t[2],TipoDato.ERROR,t[5],[],t.lexer.lineno,find_column(entrada,t.slice[1]))
    elif len(t)==8:
        t[0] = Funcion(t[2],t[6],t[7],[],t.lexer.lineno,find_column(entrada,t.slice[1]))
    elif len(t)==7:
        t[0] = Funcion(t[2],TipoDato.ERROR,t[6],t[4],t.lexer.lineno,find_column(entrada,t.slice[1]))
    elif len(t)==9:
        t[0] = Funcion(t[2],t[7],t[8],t[4],t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_lista_parametros(t):
    """ parametros : parametros COMA parametro"""
    t[1].append(t[3])
    t[0] = t[1]


def p_lista_parametros_corte(t):
    """ parametros : parametro"""
    t[0] = [t[1]]


def p_parametro(t):
    """ parametro : ID DOBLEPT tipo_dato """
    t[0] = Parametro(t[1],t[3],t.lexer.lineno,find_column(entrada,t.slice[2]))

def p_llamada(t):
    """llamadaF : ID PIZQ PDER
                | ID PIZQ lista_expresiones PDER """
    if len(t)==4:
        t[0]=Llamada(t[1],[],t.lexer.lineno,find_column(entrada,t.slice[1]))
    if len(t)==5:
        t[0]=Llamada(t[1],t[3],t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_lista_expresiones(t):
    """ lista_expresiones : lista_expresiones COMA  expresion"""
    t[1].append(t[3])
    t[0] = t[1]


def p_lista_expresiones_corte(t):
    """ lista_expresiones : expresion"""
    t[0] = [t[1]]



def p_bloque(t):
    """bloque  : LLAVEIZQ  LLAVEDER
            | LLAVEIZQ  instrucciones LLAVEDER """

    if len(t) == 3:
        t[0] = []
    else:
        t[0] = t[2]

def p_instrucciones(t):
    """instrucciones : instrucciones instruccion"""
    t[1].append(t[2])
    t[0]=t[1]

def p_instrucciones_instruccion(t):
    """instrucciones : instruccion"""
    t[0]=[t[1]]

def p_instruccion(t):
    """instruccion : print PTCOMA
                | declaracion PTCOMA
                | asignacion PTCOMA
                | if_i
                | llamadaF PTCOMA
                | return PTCOMA
                | loop 
                | break PTCOMA
                | while
                | continue PTCOMA
                | for """
    t[0]=t[1]

def p_print(t):
    """print : PRINTLN NOT PIZQ lista_expresiones PDER """
    t[0]=Print(t[4],t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_return(t):
    """return : RETURN 
                | RETURN expresion"""
    if len(t)==2:
        t[0]=Return(None,t.lexer.lineno,find_column(entrada,t.slice[1]))
    elif len(t)==3:
        t[0]=Return(t[2],t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_declaracion1(t):
    """declaracion : LET MUT ID DOBLEPT tipo_dato IGUAL expresion
                | LET ID DOBLEPT tipo_dato IGUAL expresion """

    if len(t)==8:
        t[0]=Declaracion(t[3],t[7],True,t.lexer.lineno,find_column(entrada,t.slice[1]),t[5])
    if len(t)==7:
        t[0]=Declaracion(t[2],t[6],False,t.lexer.lineno,find_column(entrada,t.slice[1]),t[4])

def p_declaracion2(t):
    """declaracion : LET MUT ID IGUAL expresion
                | LET ID IGUAL expresion """

    if len(t)==6:
        t[0]=Declaracion(t[3],t[5],True,t.lexer.lineno,find_column(entrada,t.slice[1]))
    if len(t)==5:
        t[0]=Declaracion(t[2],t[4],False,t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_asignacion(t):
    """asignacion : ID IGUAL expresion"""
    t[0]= Asignacion(t[1],t[3],t.lexer.lineno,find_column(entrada,t.slice[2]))

def p_if_instruccion(t):
    """if_i : IF expresion bloque else"""
    t[0] = If_i(t[2],t[3],t[4],t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_else_instruccion(t):
    """else : ELSE if_i
            | ELSE  bloque
            | empty"""
    
    if len(t)==3:
        t[0] = t[2]
    if len(t)==2:
        t[0]=[]

def p_vacio(t):
    """empty : """
    pass
    # para romper la recursividad 


def p_loop(t):
    """loop : LOOP bloque"""
    t[0]= Loop(t[2],t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_break(t):
    """break : BREAK 
                | BREAK expresion"""
    if len(t)==2:
        t[0]=Break(None,t.lexer.lineno,find_column(entrada,t.slice[1]))
    elif len(t)==3:
        t[0]=Break(t[2],t.lexer.lineno,find_column(entrada,t.slice[1]))


def p_while(t):
    """while : WHILE expresion bloque"""
    t[0]= While(t[2],t[3],t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_continue(t):
    """ continue : CONTINUE"""
    t[0]=Continue(t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_for1(t):
    """ for : FOR ID IN expresion PUNTO PUNTO expresion bloque """
    t[0]=For(t[2],t[4],t[7],1,t[8],t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_for2(t):
    """ for : FOR ID IN expresion PUNTO CHARS PIZQ PDER bloque"""
    t[0]=For(t[2],t[4],None,2,t[9],t.lexer.lineno,find_column(entrada,t.slice[1]))

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
                | as
                | if_e
                | llamadaF
                | loop"""
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

def p_if_Expresion(t):
    """ if_e : IF expresion LLAVEIZQ expresion LLAVEDER
            |  IF expresion LLAVEIZQ expresion LLAVEDER ELSE LLAVEIZQ expresion LLAVEDER
            |  IF expresion LLAVEIZQ expresion LLAVEDER listaelse
            |  IF expresion LLAVEIZQ expresion LLAVEDER listaelse ELSE LLAVEIZQ expresion LLAVEDER"""

    if len(t)==6:
        t[0]=If_e(t[2],t[4],[],None,t.lexer.lineno,find_column(entrada,t.slice[1]))
    elif len(t)==7:
        t[0]=If_e(t[2],t[4],t[6],None,t.lexer.lineno,find_column(entrada,t.slice[1]))
    elif len(t)==10:
        t[0]=If_e(t[2],t[4],[],t[8],t.lexer.lineno,find_column(entrada,t.slice[1]))
    elif len(t)==11:
        t[0]=If_e(t[2],t[4],t[6],t[9],t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_elseif_lista(t):
    """ listaelse : listaelse elseif """
    t[1].append(t[2])
    t[0]=t[1]
    
def p_elseif_otra(t):
    """listaelse : elseif """
    t[0]=[t[1]]

def p_elseif_def(t):
    """elseif : ELSE IF expresion LLAVEIZQ expresion LLAVEDER"""
    t[0]=If_e(t[3],t[5],[],None,t.lexer.lineno,find_column(entrada,t.slice[1]))

def p_expresion_primitiva(t):
    """expresion : ENTERO
                    | DECIMAL
                    | ID
                    | CARACTER
                    | CADENA
                    | TRUE
                    | FALSE"""

    if t.slice[1].type == 'ENTERO':
        t[0] = Primitivo(t[1],TipoDato.I64)
    elif t.slice[1].type == 'DECIMAL':
        t[0] = Primitivo(t[1], TipoDato.F64)
    elif t.slice[1].type == 'CARACTER':
        t[0] = Primitivo(t[1], TipoDato.CHAR)
    elif t.slice[1].type == 'CADENA':
        t[0] = Primitivo(t[1], TipoDato.STR)
    elif t.slice[1].type == 'ID':
        t[0] = AccesoSimbolo(t[1],t.lexer.lineno,find_column(entrada,t.slice[1]))
    elif t.slice[1].type == 'TRUE':
        t[0] = Primitivo(True, TipoDato.BOOL)
    elif t.slice[1].type == 'FALSE':
        t[0] = Primitivo(False, TipoDato.BOOL)

def p_tipo_dato(t):
    """ tipo_dato : I64
                     | F64
                     | BOOL
                     | CHAR
                     | str
                     | STRING
                     """

    if t[1] == 'i64':
        t[0] = TipoDato.I64
    if t[1] == 'f64':
        t[0] = TipoDato.F64
    if t[1] == 'bool':
        t[0] = TipoDato.BOOL
    if t[1] == 'char':
        t[0] = TipoDato.CHAR
    if t[1] == '&str':
        t[0] = TipoDato.STR
    if t[1] == 'string':
        print("holaaaaaaaaaaaaaaaaaa")
        t[0] = TipoDato.STRING

def p_str(t):
    """str : Y STR"""
    t[0]="&str"
def p_error(t):
    print(f"SE ENCONTRO UN ERROR {t} En linea {t.lexer.lineno} columna {find_column(entrada,t)}")

parser = yacc.yacc()
entrada=""


def parse(input):
    global lexer,entrada
    entrada=input
    lexer = lex.lex()
    return parser.parse(input)