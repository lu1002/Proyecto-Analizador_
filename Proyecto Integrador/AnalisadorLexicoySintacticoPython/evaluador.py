from PalabrasParserVisitor import PalabrasParserVisitor
from PalabrasParser import PalabrasParser

class Evaluador(PalabrasParserVisitor):

    # expr: expr MAS term | expr MENOS term | term
    def visitExpr(self, ctx):
        if ctx.term() and not ctx.expr():
            return self.visit(ctx.term())

        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())

        if ctx.MAS():
            return left + right
        if ctx.MENOS():
            return left - right

    # term: term POR factor | term ENTRE factor | factor
    def visitTerm(self, ctx):
        if ctx.factor() and not ctx.term():
            return self.visit(ctx.factor())

        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())

        if ctx.POR():
            return left * right
        if ctx.ENTRE():
            return left / right

    # factor: numero | (expr)
    def visitFactor(self, ctx):
        if ctx.numero():
            return self.visit(ctx.numero())
        return self.visit(ctx.expr())

    # Transformar palabras en numeros reales
    def visitNumero(self, ctx):
        if ctx.UNO(): return 1
        if ctx.DOS(): return 2
        if ctx.TRES(): return 3
        if ctx.CUATRO(): return 4
        if ctx.CINCO(): return 5
        if ctx.SEIS(): return 6
        if ctx.SIETE(): return 7
        if ctx.OCHO(): return 8
        if ctx.NUEVE(): return 9
        if ctx.DIEZ(): return 10
