// Generated from /Users/adrian/compiler-construction/lab3/program/ConfRoomScheduler.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ConfRoomSchedulerParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, NAME=12, INT=13, ID=14, DATE=15, TIME=16, STRING=17, 
		NEWLINE=18, WS=19;
	public static final int
		RULE_prog = 0, RULE_stat = 1, RULE_reserve = 2, RULE_cancel = 3, RULE_list = 4, 
		RULE_reschedule = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stat", "reserve", "cancel", "list", "reschedule"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'RESERVE'", "'ROOM'", "'AT'", "'FROM'", "'TO'", "'EVENT'", "'TYPE'", 
			"'DESCRIPTION'", "'CANCEL'", "'LIST'", "'RESCHEDULE'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"NAME", "INT", "ID", "DATE", "TIME", "STRING", "NEWLINE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ConfRoomScheduler.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ConfRoomSchedulerParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ConfRoomSchedulerParser.EOF, 0); }
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(12);
				stat();
				}
				}
				setState(15); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 265730L) != 0) );
			setState(17);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatContext extends ParserRuleContext {
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	 
		public StatContext() { }
		public void copyFrom(StatContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BlankContext extends StatContext {
		public TerminalNode NEWLINE() { return getToken(ConfRoomSchedulerParser.NEWLINE, 0); }
		public BlankContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).enterBlank(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).exitBlank(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RescheduleStatContext extends StatContext {
		public RescheduleContext reschedule() {
			return getRuleContext(RescheduleContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ConfRoomSchedulerParser.NEWLINE, 0); }
		public RescheduleStatContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).enterRescheduleStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).exitRescheduleStat(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ListStatContext extends StatContext {
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ConfRoomSchedulerParser.NEWLINE, 0); }
		public ListStatContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).enterListStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).exitListStat(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ReserveStatContext extends StatContext {
		public ReserveContext reserve() {
			return getRuleContext(ReserveContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ConfRoomSchedulerParser.NEWLINE, 0); }
		public ReserveStatContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).enterReserveStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).exitReserveStat(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CancelStatContext extends StatContext {
		public CancelContext cancel() {
			return getRuleContext(CancelContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ConfRoomSchedulerParser.NEWLINE, 0); }
		public CancelStatContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).enterCancelStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).exitCancelStat(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		try {
			setState(36);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new ReserveStatContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(19);
				reserve();
				setState(21);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
				case 1:
					{
					setState(20);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case T__8:
				_localctx = new CancelStatContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(23);
				cancel();
				setState(25);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
				case 1:
					{
					setState(24);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case T__9:
				_localctx = new ListStatContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(27);
				list();
				setState(29);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
				case 1:
					{
					setState(28);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case T__10:
				_localctx = new RescheduleStatContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(31);
				reschedule();
				setState(33);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
				case 1:
					{
					setState(32);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case NEWLINE:
				_localctx = new BlankContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(35);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReserveContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(ConfRoomSchedulerParser.NAME, 0); }
		public TerminalNode ID() { return getToken(ConfRoomSchedulerParser.ID, 0); }
		public TerminalNode DATE() { return getToken(ConfRoomSchedulerParser.DATE, 0); }
		public List<TerminalNode> TIME() { return getTokens(ConfRoomSchedulerParser.TIME); }
		public TerminalNode TIME(int i) {
			return getToken(ConfRoomSchedulerParser.TIME, i);
		}
		public List<TerminalNode> STRING() { return getTokens(ConfRoomSchedulerParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ConfRoomSchedulerParser.STRING, i);
		}
		public ReserveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reserve; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).enterReserve(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).exitReserve(this);
		}
	}

	public final ReserveContext reserve() throws RecognitionException {
		ReserveContext _localctx = new ReserveContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_reserve);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(T__0);
			setState(39);
			match(NAME);
			setState(40);
			match(T__1);
			setState(41);
			match(ID);
			setState(42);
			match(T__2);
			setState(43);
			match(DATE);
			setState(44);
			match(T__3);
			setState(45);
			match(TIME);
			setState(46);
			match(T__4);
			setState(47);
			match(TIME);
			setState(48);
			match(T__5);
			setState(49);
			match(STRING);
			setState(50);
			match(T__6);
			setState(51);
			match(STRING);
			setState(54);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__7) {
				{
				setState(52);
				match(T__7);
				setState(53);
				match(STRING);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CancelContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(ConfRoomSchedulerParser.INT, 0); }
		public CancelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cancel; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).enterCancel(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).exitCancel(this);
		}
	}

	public final CancelContext cancel() throws RecognitionException {
		CancelContext _localctx = new CancelContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_cancel);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(T__8);
			setState(57);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListContext extends ParserRuleContext {
		public ListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).enterList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).exitList(this);
		}
	}

	public final ListContext list() throws RecognitionException {
		ListContext _localctx = new ListContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RescheduleContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(ConfRoomSchedulerParser.INT, 0); }
		public TerminalNode DATE() { return getToken(ConfRoomSchedulerParser.DATE, 0); }
		public List<TerminalNode> TIME() { return getTokens(ConfRoomSchedulerParser.TIME); }
		public TerminalNode TIME(int i) {
			return getToken(ConfRoomSchedulerParser.TIME, i);
		}
		public RescheduleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reschedule; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).enterReschedule(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConfRoomSchedulerListener ) ((ConfRoomSchedulerListener)listener).exitReschedule(this);
		}
	}

	public final RescheduleContext reschedule() throws RecognitionException {
		RescheduleContext _localctx = new RescheduleContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_reschedule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(T__10);
			setState(62);
			match(INT);
			setState(63);
			match(T__4);
			setState(64);
			match(DATE);
			setState(65);
			match(T__3);
			setState(66);
			match(TIME);
			setState(67);
			match(T__4);
			setState(68);
			match(TIME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0013G\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0001\u0000\u0004\u0000\u000e\b\u0000\u000b\u0000\f"+
		"\u0000\u000f\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0003\u0001"+
		"\u0016\b\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u001a\b\u0001\u0001"+
		"\u0001\u0001\u0001\u0003\u0001\u001e\b\u0001\u0001\u0001\u0001\u0001\u0003"+
		"\u0001\"\b\u0001\u0001\u0001\u0003\u0001%\b\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u00027\b\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0000\u0000\u0006\u0000\u0002\u0004\u0006\b\n\u0000\u0000"+
		"J\u0000\r\u0001\u0000\u0000\u0000\u0002$\u0001\u0000\u0000\u0000\u0004"+
		"&\u0001\u0000\u0000\u0000\u00068\u0001\u0000\u0000\u0000\b;\u0001\u0000"+
		"\u0000\u0000\n=\u0001\u0000\u0000\u0000\f\u000e\u0003\u0002\u0001\u0000"+
		"\r\f\u0001\u0000\u0000\u0000\u000e\u000f\u0001\u0000\u0000\u0000\u000f"+
		"\r\u0001\u0000\u0000\u0000\u000f\u0010\u0001\u0000\u0000\u0000\u0010\u0011"+
		"\u0001\u0000\u0000\u0000\u0011\u0012\u0005\u0000\u0000\u0001\u0012\u0001"+
		"\u0001\u0000\u0000\u0000\u0013\u0015\u0003\u0004\u0002\u0000\u0014\u0016"+
		"\u0005\u0012\u0000\u0000\u0015\u0014\u0001\u0000\u0000\u0000\u0015\u0016"+
		"\u0001\u0000\u0000\u0000\u0016%\u0001\u0000\u0000\u0000\u0017\u0019\u0003"+
		"\u0006\u0003\u0000\u0018\u001a\u0005\u0012\u0000\u0000\u0019\u0018\u0001"+
		"\u0000\u0000\u0000\u0019\u001a\u0001\u0000\u0000\u0000\u001a%\u0001\u0000"+
		"\u0000\u0000\u001b\u001d\u0003\b\u0004\u0000\u001c\u001e\u0005\u0012\u0000"+
		"\u0000\u001d\u001c\u0001\u0000\u0000\u0000\u001d\u001e\u0001\u0000\u0000"+
		"\u0000\u001e%\u0001\u0000\u0000\u0000\u001f!\u0003\n\u0005\u0000 \"\u0005"+
		"\u0012\u0000\u0000! \u0001\u0000\u0000\u0000!\"\u0001\u0000\u0000\u0000"+
		"\"%\u0001\u0000\u0000\u0000#%\u0005\u0012\u0000\u0000$\u0013\u0001\u0000"+
		"\u0000\u0000$\u0017\u0001\u0000\u0000\u0000$\u001b\u0001\u0000\u0000\u0000"+
		"$\u001f\u0001\u0000\u0000\u0000$#\u0001\u0000\u0000\u0000%\u0003\u0001"+
		"\u0000\u0000\u0000&\'\u0005\u0001\u0000\u0000\'(\u0005\f\u0000\u0000("+
		")\u0005\u0002\u0000\u0000)*\u0005\u000e\u0000\u0000*+\u0005\u0003\u0000"+
		"\u0000+,\u0005\u000f\u0000\u0000,-\u0005\u0004\u0000\u0000-.\u0005\u0010"+
		"\u0000\u0000./\u0005\u0005\u0000\u0000/0\u0005\u0010\u0000\u000001\u0005"+
		"\u0006\u0000\u000012\u0005\u0011\u0000\u000023\u0005\u0007\u0000\u0000"+
		"36\u0005\u0011\u0000\u000045\u0005\b\u0000\u000057\u0005\u0011\u0000\u0000"+
		"64\u0001\u0000\u0000\u000067\u0001\u0000\u0000\u00007\u0005\u0001\u0000"+
		"\u0000\u000089\u0005\t\u0000\u00009:\u0005\r\u0000\u0000:\u0007\u0001"+
		"\u0000\u0000\u0000;<\u0005\n\u0000\u0000<\t\u0001\u0000\u0000\u0000=>"+
		"\u0005\u000b\u0000\u0000>?\u0005\r\u0000\u0000?@\u0005\u0005\u0000\u0000"+
		"@A\u0005\u000f\u0000\u0000AB\u0005\u0004\u0000\u0000BC\u0005\u0010\u0000"+
		"\u0000CD\u0005\u0005\u0000\u0000DE\u0005\u0010\u0000\u0000E\u000b\u0001"+
		"\u0000\u0000\u0000\u0007\u000f\u0015\u0019\u001d!$6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}