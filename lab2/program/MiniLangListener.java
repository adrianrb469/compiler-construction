// Generated from MiniLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MiniLangParser}.
 */
public interface MiniLangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(MiniLangParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(MiniLangParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printExpr}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterPrintExpr(MiniLangParser.PrintExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printExpr}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitPrintExpr(MiniLangParser.PrintExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assign}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterAssign(MiniLangParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assign}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitAssign(MiniLangParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifStat}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterIfStat(MiniLangParser.IfStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifStat}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitIfStat(MiniLangParser.IfStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code whileStat}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterWhileStat(MiniLangParser.WhileStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code whileStat}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitWhileStat(MiniLangParser.WhileStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code blank}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterBlank(MiniLangParser.BlankContext ctx);
	/**
	 * Exit a parse tree produced by the {@code blank}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitBlank(MiniLangParser.BlankContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unrecognizedToken}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterUnrecognizedToken(MiniLangParser.UnrecognizedTokenContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unrecognizedToken}
	 * labeled alternative in {@link MiniLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitUnrecognizedToken(MiniLangParser.UnrecognizedTokenContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#ifBlock}.
	 * @param ctx the parse tree
	 */
	void enterIfBlock(MiniLangParser.IfBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#ifBlock}.
	 * @param ctx the parse tree
	 */
	void exitIfBlock(MiniLangParser.IfBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#whileBlock}.
	 * @param ctx the parse tree
	 */
	void enterWhileBlock(MiniLangParser.WhileBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#whileBlock}.
	 * @param ctx the parse tree
	 */
	void exitWhileBlock(MiniLangParser.WhileBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(MiniLangParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(MiniLangParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(MiniLangParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(MiniLangParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parens}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParens(MiniLangParser.ParensContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parens}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParens(MiniLangParser.ParensContext ctx);
	/**
	 * Enter a parse tree produced by the {@code compare}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterCompare(MiniLangParser.CompareContext ctx);
	/**
	 * Exit a parse tree produced by the {@code compare}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitCompare(MiniLangParser.CompareContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(MiniLangParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(MiniLangParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(MiniLangParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(MiniLangParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code id}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterId(MiniLangParser.IdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code id}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitId(MiniLangParser.IdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code constantExpr}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterConstantExpr(MiniLangParser.ConstantExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code constantExpr}
	 * labeled alternative in {@link MiniLangParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitConstantExpr(MiniLangParser.ConstantExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#compareOp}.
	 * @param ctx the parse tree
	 */
	void enterCompareOp(MiniLangParser.CompareOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#compareOp}.
	 * @param ctx the parse tree
	 */
	void exitCompareOp(MiniLangParser.CompareOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link MiniLangParser#constant}.
	 * @param ctx the parse tree
	 */
	void enterConstant(MiniLangParser.ConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link MiniLangParser#constant}.
	 * @param ctx the parse tree
	 */
	void exitConstant(MiniLangParser.ConstantContext ctx);
}