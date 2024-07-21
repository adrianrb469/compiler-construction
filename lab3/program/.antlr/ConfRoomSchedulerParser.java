// Generated from /Users/adrian/Documents/University/2024/s2/compilers/compiler-construction/lab3/program/ConfRoomScheduler.g4 by ANTLR 4.13.1
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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, NAME=9, 
		INT=10, ID=11, DATE=12, TIME=13, STRING=14, NEWLINE=15, WS=16;
	public static final int
		RULE_prog = 0, RULE_stat = 1, RULE_reserve = 2, RULE_cancel = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stat", "reserve", "cancel"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'RESERVE'", "'ROOM'", "'AT'", "'FROM'", "'TO'", "'EVENT'", "'DESCRIPTION'", 
			"'CANCEL'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "NAME", "INT", 
			"ID", "DATE", "TIME", "STRING", "NEWLINE", "WS"
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
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(9); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(8);
				stat();
				}
				}
				setState(11); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 33026L) != 0) );
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
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ReserveStatContext extends StatContext {
		public ReserveContext reserve() {
			return getRuleContext(ReserveContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ConfRoomSchedulerParser.NEWLINE, 0); }
		public ReserveStatContext(StatContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CancelStatContext extends StatContext {
		public CancelContext cancel() {
			return getRuleContext(CancelContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ConfRoomSchedulerParser.NEWLINE, 0); }
		public CancelStatContext(StatContext ctx) { copyFrom(ctx); }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		try {
			setState(20);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new ReserveStatContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(13);
				reserve();
				setState(14);
				match(NEWLINE);
				}
				break;
			case T__7:
				_localctx = new CancelStatContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(16);
				cancel();
				setState(17);
				match(NEWLINE);
				}
				break;
			case NEWLINE:
				_localctx = new BlankContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(19);
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
	}

	public final ReserveContext reserve() throws RecognitionException {
		ReserveContext _localctx = new ReserveContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_reserve);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			match(T__0);
			setState(23);
			match(NAME);
			setState(24);
			match(T__1);
			setState(25);
			match(ID);
			setState(26);
			match(T__2);
			setState(27);
			match(DATE);
			setState(28);
			match(T__3);
			setState(29);
			match(TIME);
			setState(30);
			match(T__4);
			setState(31);
			match(TIME);
			setState(32);
			match(T__5);
			setState(33);
			match(STRING);
			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(34);
				match(T__6);
				setState(35);
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
	}

	public final CancelContext cancel() throws RecognitionException {
		CancelContext _localctx = new CancelContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_cancel);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(T__7);
			setState(39);
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

	public static final String _serializedATN =
		"\u0004\u0001\u0010*\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0004\u0000\n\b"+
		"\u0000\u000b\u0000\f\u0000\u000b\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u0015\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u0002%\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0000\u0000\u0004\u0000\u0002\u0004\u0006\u0000\u0000"+
		")\u0000\t\u0001\u0000\u0000\u0000\u0002\u0014\u0001\u0000\u0000\u0000"+
		"\u0004\u0016\u0001\u0000\u0000\u0000\u0006&\u0001\u0000\u0000\u0000\b"+
		"\n\u0003\u0002\u0001\u0000\t\b\u0001\u0000\u0000\u0000\n\u000b\u0001\u0000"+
		"\u0000\u0000\u000b\t\u0001\u0000\u0000\u0000\u000b\f\u0001\u0000\u0000"+
		"\u0000\f\u0001\u0001\u0000\u0000\u0000\r\u000e\u0003\u0004\u0002\u0000"+
		"\u000e\u000f\u0005\u000f\u0000\u0000\u000f\u0015\u0001\u0000\u0000\u0000"+
		"\u0010\u0011\u0003\u0006\u0003\u0000\u0011\u0012\u0005\u000f\u0000\u0000"+
		"\u0012\u0015\u0001\u0000\u0000\u0000\u0013\u0015\u0005\u000f\u0000\u0000"+
		"\u0014\r\u0001\u0000\u0000\u0000\u0014\u0010\u0001\u0000\u0000\u0000\u0014"+
		"\u0013\u0001\u0000\u0000\u0000\u0015\u0003\u0001\u0000\u0000\u0000\u0016"+
		"\u0017\u0005\u0001\u0000\u0000\u0017\u0018\u0005\t\u0000\u0000\u0018\u0019"+
		"\u0005\u0002\u0000\u0000\u0019\u001a\u0005\u000b\u0000\u0000\u001a\u001b"+
		"\u0005\u0003\u0000\u0000\u001b\u001c\u0005\f\u0000\u0000\u001c\u001d\u0005"+
		"\u0004\u0000\u0000\u001d\u001e\u0005\r\u0000\u0000\u001e\u001f\u0005\u0005"+
		"\u0000\u0000\u001f \u0005\r\u0000\u0000 !\u0005\u0006\u0000\u0000!$\u0005"+
		"\u000e\u0000\u0000\"#\u0005\u0007\u0000\u0000#%\u0005\u000e\u0000\u0000"+
		"$\"\u0001\u0000\u0000\u0000$%\u0001\u0000\u0000\u0000%\u0005\u0001\u0000"+
		"\u0000\u0000&\'\u0005\b\u0000\u0000\'(\u0005\n\u0000\u0000(\u0007\u0001"+
		"\u0000\u0000\u0000\u0003\u000b\u0014$";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}