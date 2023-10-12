#Class : tokens.py
#Description : analizador léxico para el lenguaje SimpliciQL
#Author : Yony Alex Vilca Mamani
#Fecha : 07-Setiembre-2023
#Course : Compiladores
#Editor : Visual studio Code
# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape, 
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea) 

 # List of token names.   This is always required
reserved = {
  'crear'  : 'tipo_create',
   'tabla'  : 'tipo_table',
   'entero'  : 'tipo_int',
   'no' : 'tipo_not',  
   'nulo'  : 'tipo_null',
   'identidad'  : 'tipo_identity',
   'cadenavar'  : 'tipo_varchar',
   'unica'  : 'tipo_unique',
   'por defecto'  : 'tipo_default',
   'restriccion'  : 'tipo_constraint',
   'principal'  : 'tipo_primarykey',
   'autoincremento'  : 'tipo_autoincrement',
   'ascendente'  : 'tipo_asc',
   'establecer'  : 'tipo_set',
   'donde'  : 'tipo_where',
   'eliminar'  : 'tipo_drop',
   'obtener'  : 'tipo_select',
   'desde'  : 'tipo_from',
   'procedimiento'  : 'tipo_procedure',
   'como'  : 'tipo_as',
   'inicio'  : 'tipo_begin',
   'fin'  : 'tipo_end',
   'ejecutar'  : 'tipo_exec',
   'actualizar'  : 'tipo_update',
   'decimal'  : 'tipo_decimal',
   'real'  : 'tipo_real',
   'booleano'  : 'tipo_boolean',
   'fecha'  : 'tipo_date',
   'hora'  : 'tipo_time',
   'fechahora'  : 'tipo_datetime',
   'por'  : 'tipo_by',
   'ordenar'  : 'tipo_order',
   'descendente'  : 'tipo_desc',
   'flotante'  : 'tipo_float',
   'evaluar'  : 'tipo_eval',
   'limpiar'  : 'tipo_clear',
   'insertar'  : 'tipo_insert',
   'abortar'  : 'tipo_abort',
   'agregar'  : 'tipo_add',
   'alinear'  : 'tipo_align',
   'por_defecto'  : 'tipo_bydefault',
   'todos'  : 'tipo_all',
   'mover'  : 'tipo_move',
   'promedio'  : 'tipo_avg',
   'en'  : 'tipo_in',
   'doble'  : 'tipo_double',
   'extraer'  : 'tipo_extract',
   'alterar'  : 'tipo_alter',
   'columna'  : 'tipo_column',
   'renombrar'  : 'tipo_rename',
   'hacia'  : 'tipo_to',
   'dentro'  : 'tipo_into',
   'valores'  : 'tipo_values',
   'foranea'  : 'tipo_foreignkey',
   'referencia'  : 'tipo_reference',
   'contar'  : 'tipo_count',
   'distinto'  : 'tipo_distinct',

}

tokens = [
    'number',
    'mas',
    'menos',
    'comodin',
    'divide',
    'lparen',
    'rparen',
    'igual',
    'coma',
    'dospuntos',
    'puntoycoma',
    'id',
    'cadena',
    'comentariol',
    'comentariob',
    'mayorigual',
    'menorigual',
    'punto',
    'noiguala',
    'nomenorque',
    'nomayorque',
    'modulo',
    "pmarca",
    "mayor",
    "menor"

    
 ] + list(reserved.values())
 # Regular expression rules for simple tokens
t_mas    = r'\+'
t_menos   = r'-'
t_comodin   = r'\*'
t_divide  = r'/'
t_igual  = r'\='
t_mayorigual    = r'\>='
t_menorigual  = r'\<='
t_mayor = r'>'
t_menor  = r'<'
t_lparen  = r'\('
t_rparen  = r'\)'
t_noiguala  = r'\<\>'
t_nomenorque = r'\!\>'
t_nomayorque  = r'\!\<'
t_modulo  = r'%'
t_coma   = r','
t_dospuntos   = r':'
t_puntoycoma = r';'
t_comentariol = r'--.*'
t_comentariob = r'/\*(.|\n)*?\*/'
t_punto = r'\.'
t_pmarca = r'@\w+'
#t_NUMBER  = r'\d+' 
# A regular expression rule with some action code
def t_id(t):
    r'[a-zA-Z_][a-zA-Z0-9_]+'
    t.type = reserved.get(t.value,'id')    # Check for reserved words
    return t
def t_cadena(t):
    r"'[^']*'"
    return t
def t_number(t):
    r'\d+'
    t.value = int(t.value)  # guardamos el valor del lexema  
    #print("se reconocio el numero")
    return t
 # Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
# Build the lexer
lexer = lex.lex()

def get_tokens(file):
    tokens = []

    f = open(file, "r")
    data = f.read()

    lexer.input(data)
    
    # Tokenize
    while True:
        unitok=[]
        tok = lexer.token()
        if not tok: 
            break
        tokens.append( [tok.type, tok.value, tok.lineno] )

    return tokens

if __name__ == "__main__":
    tokens = get_tokens("AnalizadorSintactico/data.txt")
    for tok in tokens:
        print( str(tok) + ' ', end='\n')
    print()
    