# Generated from PalabrasParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,2,1,2,1,2,1,2,1,2,3,
        2,42,8,2,1,3,1,3,1,3,0,2,0,2,4,0,2,4,6,0,1,1,0,1,10,46,0,8,1,0,0,
        0,2,22,1,0,0,0,4,41,1,0,0,0,6,43,1,0,0,0,8,9,6,0,-1,0,9,10,3,2,1,
        0,10,19,1,0,0,0,11,12,10,3,0,0,12,13,5,11,0,0,13,18,3,2,1,0,14,15,
        10,2,0,0,15,16,5,12,0,0,16,18,3,2,1,0,17,11,1,0,0,0,17,14,1,0,0,
        0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,1,1,0,0,0,21,19,1,
        0,0,0,22,23,6,1,-1,0,23,24,3,4,2,0,24,33,1,0,0,0,25,26,10,3,0,0,
        26,27,5,13,0,0,27,32,3,4,2,0,28,29,10,2,0,0,29,30,5,14,0,0,30,32,
        3,4,2,0,31,25,1,0,0,0,31,28,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,
        33,34,1,0,0,0,34,3,1,0,0,0,35,33,1,0,0,0,36,42,3,6,3,0,37,38,5,15,
        0,0,38,39,3,0,0,0,39,40,5,16,0,0,40,42,1,0,0,0,41,36,1,0,0,0,41,
        37,1,0,0,0,42,5,1,0,0,0,43,44,7,0,0,0,44,7,1,0,0,0,5,17,19,31,33,
        41
    ]

class PalabrasParser ( Parser ):

    grammarFileName = "PalabrasParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'uno'", "'dos'", "'tres'", "'cuatro'", 
                     "'cinco'", "'seis'", "'siete'", "'ocho'", "'nueve'", 
                     "'diez'", "'mas'", "'menos'", "'por'", "'entre'" ]

    symbolicNames = [ "<INVALID>", "UNO", "DOS", "TRES", "CUATRO", "CINCO", 
                      "SEIS", "SIETE", "OCHO", "NUEVE", "DIEZ", "MAS", "MENOS", 
                      "POR", "ENTRE", "LPAREN", "RPAREN", "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_numero = 3

    ruleNames =  [ "expr", "term", "factor", "numero" ]

    EOF = Token.EOF
    UNO=1
    DOS=2
    TRES=3
    CUATRO=4
    CINCO=5
    SEIS=6
    SIETE=7
    OCHO=8
    NUEVE=9
    DIEZ=10
    MAS=11
    MENOS=12
    POR=13
    ENTRE=14
    LPAREN=15
    RPAREN=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(PalabrasParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(PalabrasParser.ExprContext,0)


        def MAS(self):
            return self.getToken(PalabrasParser.MAS, 0)

        def MENOS(self):
            return self.getToken(PalabrasParser.MENOS, 0)

        def getRuleIndex(self):
            return PalabrasParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PalabrasParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 17
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = PalabrasParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 11
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 12
                        self.match(PalabrasParser.MAS)
                        self.state = 13
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = PalabrasParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 14
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 15
                        self.match(PalabrasParser.MENOS)
                        self.state = 16
                        self.term(0)
                        pass

             
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(PalabrasParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(PalabrasParser.TermContext,0)


        def POR(self):
            return self.getToken(PalabrasParser.POR, 0)

        def ENTRE(self):
            return self.getToken(PalabrasParser.ENTRE, 0)

        def getRuleIndex(self):
            return PalabrasParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PalabrasParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 31
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = PalabrasParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 25
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 26
                        self.match(PalabrasParser.POR)
                        self.state = 27
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = PalabrasParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 28
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 29
                        self.match(PalabrasParser.ENTRE)
                        self.state = 30
                        self.factor()
                        pass

             
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numero(self):
            return self.getTypedRuleContext(PalabrasParser.NumeroContext,0)


        def LPAREN(self):
            return self.getToken(PalabrasParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(PalabrasParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(PalabrasParser.RPAREN, 0)

        def getRuleIndex(self):
            return PalabrasParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = PalabrasParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.numero()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(PalabrasParser.LPAREN)
                self.state = 38
                self.expr(0)
                self.state = 39
                self.match(PalabrasParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNO(self):
            return self.getToken(PalabrasParser.UNO, 0)

        def DOS(self):
            return self.getToken(PalabrasParser.DOS, 0)

        def TRES(self):
            return self.getToken(PalabrasParser.TRES, 0)

        def CUATRO(self):
            return self.getToken(PalabrasParser.CUATRO, 0)

        def CINCO(self):
            return self.getToken(PalabrasParser.CINCO, 0)

        def SEIS(self):
            return self.getToken(PalabrasParser.SEIS, 0)

        def SIETE(self):
            return self.getToken(PalabrasParser.SIETE, 0)

        def OCHO(self):
            return self.getToken(PalabrasParser.OCHO, 0)

        def NUEVE(self):
            return self.getToken(PalabrasParser.NUEVE, 0)

        def DIEZ(self):
            return self.getToken(PalabrasParser.DIEZ, 0)

        def getRuleIndex(self):
            return PalabrasParser.RULE_numero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)




    def numero(self):

        localctx = PalabrasParser.NumeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_numero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2046) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        self._predicates[1] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




