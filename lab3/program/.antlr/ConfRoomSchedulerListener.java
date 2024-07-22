// Generated from /Users/adrian/Documents/University/2024/s2/compilers/compiler-construction/lab3/program/ConfRoomScheduler.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ConfRoomSchedulerParser}.
 */
public interface ConfRoomSchedulerListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ConfRoomSchedulerParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(ConfRoomSchedulerParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConfRoomSchedulerParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(ConfRoomSchedulerParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code reserveStat}
	 * labeled alternative in {@link ConfRoomSchedulerParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterReserveStat(ConfRoomSchedulerParser.ReserveStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code reserveStat}
	 * labeled alternative in {@link ConfRoomSchedulerParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitReserveStat(ConfRoomSchedulerParser.ReserveStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code cancelStat}
	 * labeled alternative in {@link ConfRoomSchedulerParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterCancelStat(ConfRoomSchedulerParser.CancelStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code cancelStat}
	 * labeled alternative in {@link ConfRoomSchedulerParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitCancelStat(ConfRoomSchedulerParser.CancelStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code listStat}
	 * labeled alternative in {@link ConfRoomSchedulerParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterListStat(ConfRoomSchedulerParser.ListStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code listStat}
	 * labeled alternative in {@link ConfRoomSchedulerParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitListStat(ConfRoomSchedulerParser.ListStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code rescheduleStat}
	 * labeled alternative in {@link ConfRoomSchedulerParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterRescheduleStat(ConfRoomSchedulerParser.RescheduleStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code rescheduleStat}
	 * labeled alternative in {@link ConfRoomSchedulerParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitRescheduleStat(ConfRoomSchedulerParser.RescheduleStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code blank}
	 * labeled alternative in {@link ConfRoomSchedulerParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterBlank(ConfRoomSchedulerParser.BlankContext ctx);
	/**
	 * Exit a parse tree produced by the {@code blank}
	 * labeled alternative in {@link ConfRoomSchedulerParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitBlank(ConfRoomSchedulerParser.BlankContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConfRoomSchedulerParser#reserve}.
	 * @param ctx the parse tree
	 */
	void enterReserve(ConfRoomSchedulerParser.ReserveContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConfRoomSchedulerParser#reserve}.
	 * @param ctx the parse tree
	 */
	void exitReserve(ConfRoomSchedulerParser.ReserveContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConfRoomSchedulerParser#cancel}.
	 * @param ctx the parse tree
	 */
	void enterCancel(ConfRoomSchedulerParser.CancelContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConfRoomSchedulerParser#cancel}.
	 * @param ctx the parse tree
	 */
	void exitCancel(ConfRoomSchedulerParser.CancelContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConfRoomSchedulerParser#list}.
	 * @param ctx the parse tree
	 */
	void enterList(ConfRoomSchedulerParser.ListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConfRoomSchedulerParser#list}.
	 * @param ctx the parse tree
	 */
	void exitList(ConfRoomSchedulerParser.ListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConfRoomSchedulerParser#reschedule}.
	 * @param ctx the parse tree
	 */
	void enterReschedule(ConfRoomSchedulerParser.RescheduleContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConfRoomSchedulerParser#reschedule}.
	 * @param ctx the parse tree
	 */
	void exitReschedule(ConfRoomSchedulerParser.RescheduleContext ctx);
}