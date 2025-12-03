parser grammar PalabrasParser;

options {
    tokenVocab = PalabrasLexer;
}

// --- REGLA PRINCIPAL ---
expr
    : expr MAS term
    | expr MENOS term
    | term
    ;

// --- MULTIPLICACIÓN Y DIVISIÓN ---
term
    : term POR factor
    | term ENTRE factor
    | factor
    ;

// --- NÚMEROS Y PARÉNTESIS ---
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
