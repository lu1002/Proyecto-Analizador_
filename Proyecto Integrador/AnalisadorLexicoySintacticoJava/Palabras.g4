grammar Palabras;

// --- REGLA PRINCIPAL ---
expr
    : expr MAS term
    | expr MENOS term
    | term
    ;

term
    : term POR factor
    | term ENTRE factor
    | factor
    ;

factor
    : numero
    | LPAREN expr RPAREN
    ;

numero
    : UNO
    | DOS
    | TRES
    | CUATRO
    | CINCO
    | SEIS
    | SIETE
    | OCHO
    | NUEVE
    | DIEZ
    ;

// --- TOKENS DE NÚMEROS ---
UNO: 'uno';
DOS: 'dos';
TRES: 'tres';
CUATRO: 'cuatro';
CINCO: 'cinco';
SEIS: 'seis';
SIETE: 'siete';
OCHO: 'ocho';
NUEVE: 'nueve';
DIEZ: 'diez';

// --- OPERADORES ---
MAS: 'mas';
MENOS: 'menos';
POR: 'por';
ENTRE: 'entre';

// --- PARÉNTESIS ---
LPAREN: 'abrir' | 'parentesis abrir';
RPAREN: 'cerrar' | 'parentesis cerrar';

// --- IGNORAR ESPACIOS ---
WS: [ \t\r\n]+ -> skip;
