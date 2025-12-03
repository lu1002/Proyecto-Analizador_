# Generated from PalabrasParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PalabrasParser import PalabrasParser
else:
    from PalabrasParser import PalabrasParser

# This class defines a complete listener for a parse tree produced by PalabrasParser.
class PalabrasParserListener(ParseTreeListener):

    # Enter a parse tree produced by PalabrasParser#expr.
    def enterExpr(self, ctx:PalabrasParser.ExprContext):
        pass

    # Exit a parse tree produced by PalabrasParser#expr.
    def exitExpr(self, ctx:PalabrasParser.ExprContext):
        pass


    # Enter a parse tree produced by PalabrasParser#term.
    def enterTerm(self, ctx:PalabrasParser.TermContext):
        pass

    # Exit a parse tree produced by PalabrasParser#term.
    def exitTerm(self, ctx:PalabrasParser.TermContext):
        pass


    # Enter a parse tree produced by PalabrasParser#factor.
    def enterFactor(self, ctx:PalabrasParser.FactorContext):
        pass

    # Exit a parse tree produced by PalabrasParser#factor.
    def exitFactor(self, ctx:PalabrasParser.FactorContext):
        pass


    # Enter a parse tree produced by PalabrasParser#numero.
    def enterNumero(self, ctx:PalabrasParser.NumeroContext):
        pass

    # Exit a parse tree produced by PalabrasParser#numero.
    def exitNumero(self, ctx:PalabrasParser.NumeroContext):
        pass



del PalabrasParser