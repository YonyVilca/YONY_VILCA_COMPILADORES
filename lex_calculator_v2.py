#Class : lex_calculator_v2.py
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
   'CREAR'  : 'TIPO_CREATE',
   'TABLA'  : 'TIPO_TABLE',
   'ENTERO'  : 'TIPO_INT',
   'NO' : 'TIPO_NOT',  
   'NULO'  : 'TIPO_NULL',
   'IDENTIDAD'  : 'TIPO_IDENTIDAD',
   'CADENAVAR'  : 'TIPO_VARCHAR',
   'UNICA'  : 'TIPO_UNIQUE',
   'POR DEFECTO'  : 'TIPO_DEFAULT',
   'RESTRICCION'  : 'TIPO_CONSTRAINT',
   'PRINCIPAL'  : 'TIPO_PRIMARY',
   'LLAVE'  : 'TIPO_KEY',
   'AUTOINCREMENTO'  : 'TIPO_AUTO_INCREMENT',
   'ASCENDENTE'  : 'TIPO_ASC',
   'ESTABLECER'  : 'TIPO_SET',
   'DONDE'  : 'TIPO_WHERE',
   'ELIMINAR'  : 'TIPO_DROP',
   'OBTENER'  : 'TIPO_SELECT',
   'DESDE'  : 'TIPO_FROM',
   'PROCEDIMIENTO'  : 'TIPO_PROCEDURE',
   'COMO'  : 'TIPO_AS',
   'INICIO'  : 'TIPO_BEGIN',
   'FIN'  : 'TIPO_END',
   'EJECUTAR'  : 'TIPO_EXEC',
   'ACTUALIZAR'  : 'TIPO_UPDATE',
   'DECIMAL'  : 'TIPO_DECIMAL',
   'REAL'  : 'TIPO_REAL',
   'BOOLEANO'  : 'TIPO_BOOLEAN',
   'FECHA'  : 'TIPO_DATE',
   'HORA'  : 'TIPO_TIME',
   'POR'  : 'TIPO_BY',
   'ORDENAR'  : 'TIPO_ORDER',
   'DESCENDENTE'  : 'TIPO_DESC',
}

tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'COMMA',
    'COLON',
    'SEMICOLON',
    'ID',
    'CADENA',
    'COMENTARIOL',
    'COMENTARIOB',
    'GREATEROREQUAL',
    'LESSOREQUAL'
    
 ] + list(reserved.values())
 # Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUAL  = r'\='
t_GREATEROREQUAL  = r'\>='
t_LESSOREQUAL  = r'\<='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA   = r','
t_COLON   = r':'
t_SEMICOLON = r';'
t_COMENTARIOL = r'--.*'
t_COMENTARIOB = r'/\*(.|\n)*?\*/'
#t_NUMBER  = r'\d+'
# A regular expression rule with some action code
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]+'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
def t_CADENA(t):
    r"'[^']*'"
    return t
def t_NUMBER(t):
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
# Test it out
data = '''
-- Este es un comentario de una línea
CREAR TABLA Persona (
    id ENTERO PRINCIPAL LLAVE AUTOINCREMENTO,
    nombre CADENAVAR(50),
    edad ENTERO,
    );
    
    ACTUALIZAR Persona
    ESTABLECER nombre = 'Juan', edad = 20
    DONDE id = 1;
    
    ELIMINAR TABLA Persona;
    
    OBTENER nombre, edad
    DESDE Persona
    DONDE ciudad = 'Guatemala'
    ORDENAR nombre ASCENDENTE;
    
    CREAR PROCEDIMIENTO Obtener_Persona
    COMO
    INICIO
        OBTENER * DESDE Persona;
    FIN;
    
    EJECUTAR Obtener_Persona;
'''
# Give the lexer some input
lexer.input(data)
# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    #print(tok)
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
