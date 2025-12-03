lexer grammar PalabrasLexer;

// --- PALABRAS PARA NÚMEROS ---
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

// Puedes seguir extendiendo...

// --- OPERADORES ---
MAS: 'mas';
MENOS: 'menos';
POR: 'por';
ENTRE: 'entre';

// --- PARÉNTESIS ---
LPAREN: 'abrir' | 'parentesis abrir';
RPAREN: 'cerrar' | 'parentesis cerrar';

// --- ESPACIOS ---
WS: [ \t\r\n]+ -> skip;
