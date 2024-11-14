// Generated from /Users/adrian/compiler-construction/project-2/program/Compiscript.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CompiscriptParser}.
 */
public interface CompiscriptListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(CompiscriptParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(CompiscriptParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(CompiscriptParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(CompiscriptParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void enterClassDecl(CompiscriptParser.ClassDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void exitClassDecl(CompiscriptParser.ClassDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#funDecl}.
	 * @param ctx the parse tree
	 */
	void enterFunDecl(CompiscriptParser.FunDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#funDecl}.
	 * @param ctx the parse tree
	 */
	void exitFunDecl(CompiscriptParser.FunDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(CompiscriptParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(CompiscriptParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(CompiscriptParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(CompiscriptParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakStmt(CompiscriptParser.BreakStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakStmt(CompiscriptParser.BreakStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void enterContinueStmt(CompiscriptParser.ContinueStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void exitContinueStmt(CompiscriptParser.ContinueStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#exprStmt}.
	 * @param ctx the parse tree
	 */
	void enterExprStmt(CompiscriptParser.ExprStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#exprStmt}.
	 * @param ctx the parse tree
	 */
	void exitExprStmt(CompiscriptParser.ExprStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void enterForStmt(CompiscriptParser.ForStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void exitForStmt(CompiscriptParser.ForStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(CompiscriptParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(CompiscriptParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void enterPrintStmt(CompiscriptParser.PrintStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void exitPrintStmt(CompiscriptParser.PrintStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnStmt(CompiscriptParser.ReturnStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnStmt(CompiscriptParser.ReturnStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(CompiscriptParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(CompiscriptParser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(CompiscriptParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(CompiscriptParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#funAnon}.
	 * @param ctx the parse tree
	 */
	void enterFunAnon(CompiscriptParser.FunAnonContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#funAnon}.
	 * @param ctx the parse tree
	 */
	void exitFunAnon(CompiscriptParser.FunAnonContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(CompiscriptParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(CompiscriptParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(CompiscriptParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(CompiscriptParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#logicOr}.
	 * @param ctx the parse tree
	 */
	void enterLogicOr(CompiscriptParser.LogicOrContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#logicOr}.
	 * @param ctx the parse tree
	 */
	void exitLogicOr(CompiscriptParser.LogicOrContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#logicAnd}.
	 * @param ctx the parse tree
	 */
	void enterLogicAnd(CompiscriptParser.LogicAndContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#logicAnd}.
	 * @param ctx the parse tree
	 */
	void exitLogicAnd(CompiscriptParser.LogicAndContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#equality}.
	 * @param ctx the parse tree
	 */
	void enterEquality(CompiscriptParser.EqualityContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#equality}.
	 * @param ctx the parse tree
	 */
	void exitEquality(CompiscriptParser.EqualityContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterComparison(CompiscriptParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitComparison(CompiscriptParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(CompiscriptParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(CompiscriptParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(CompiscriptParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(CompiscriptParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(CompiscriptParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(CompiscriptParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#instantiation}.
	 * @param ctx the parse tree
	 */
	void enterInstantiation(CompiscriptParser.InstantiationContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#instantiation}.
	 * @param ctx the parse tree
	 */
	void exitInstantiation(CompiscriptParser.InstantiationContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#unary}.
	 * @param ctx the parse tree
	 */
	void enterUnary(CompiscriptParser.UnaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#unary}.
	 * @param ctx the parse tree
	 */
	void exitUnary(CompiscriptParser.UnaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#call}.
	 * @param ctx the parse tree
	 */
	void enterCall(CompiscriptParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#call}.
	 * @param ctx the parse tree
	 */
	void exitCall(CompiscriptParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(CompiscriptParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(CompiscriptParser.PrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(CompiscriptParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(CompiscriptParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(CompiscriptParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(CompiscriptParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(CompiscriptParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(CompiscriptParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiscriptParser#functions}.
	 * @param ctx the parse tree
	 */
	void enterFunctions(CompiscriptParser.FunctionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiscriptParser#functions}.
	 * @param ctx the parse tree
	 */
	void exitFunctions(CompiscriptParser.FunctionsContext ctx);
}