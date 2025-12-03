// Generated from Palabras.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PalabrasParser}.
 */
public interface PalabrasListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PalabrasParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(PalabrasParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PalabrasParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(PalabrasParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link PalabrasParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(PalabrasParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link PalabrasParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(PalabrasParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link PalabrasParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(PalabrasParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link PalabrasParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(PalabrasParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link PalabrasParser#numero}.
	 * @param ctx the parse tree
	 */
	void enterNumero(PalabrasParser.NumeroContext ctx);
	/**
	 * Exit a parse tree produced by {@link PalabrasParser#numero}.
	 * @param ctx the parse tree
	 */
	void exitNumero(PalabrasParser.NumeroContext ctx);
}