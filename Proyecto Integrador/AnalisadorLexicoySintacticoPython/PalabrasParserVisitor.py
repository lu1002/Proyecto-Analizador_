# Generated from PalabrasParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PalabrasParser import PalabrasParser
else:
    from PalabrasParser import PalabrasParser

# This class defines a complete generic visitor for a parse tree produced by PalabrasParser.

class PalabrasParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PalabrasParser#expr.
    def visitExpr(self, ctx:PalabrasParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PalabrasParser#term.
    def visitTerm(self, ctx:PalabrasParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PalabrasParser#factor.
    def visitFactor(self, ctx:PalabrasParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PalabrasParser#numero.
    def visitNumero(self, ctx:PalabrasParser.NumeroContext):
        return self.visitChildren(ctx)



del PalabrasParser