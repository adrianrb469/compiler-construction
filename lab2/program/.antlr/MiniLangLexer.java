// Generated from /Users/adrian/compiler-construction/lab2/program/MiniLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MiniLangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, INT=13, FLOAT=14, STRING=15, BOOLEAN=16, 
		NULL=17, MUL=18, DIV=19, ADD=20, SUB=21, ID=22, NEWLINE=23, COMMENT=24, 
		EQ=25, NEQ=26, LT=27, GT=28, LTE=29, GTE=30, FUNC=31, RETURN=32, INVALID_CHAR=33;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "INT", "FLOAT", "STRING", "BOOLEAN", "NULL", 
			"MUL", "DIV", "ADD", "SUB", "ID", "NEWLINE", "COMMENT", "EQ", "NEQ", 
			"LT", "GT", "LTE", "GTE", "FUNC", "RETURN", "INVALID_CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'print'", "'('", "')'", "';'", "'if'", "'else'", "'while'", "'do'", 
			"'{'", "'}'", "'='", "','", null, null, null, null, "'null'", "'*'", 
			"'/'", "'+'", "'-'", null, null, null, "'=='", "'!='", "'<'", "'>'", 
			"'<='", "'>='", "'func'", "'return'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "INT", "FLOAT", "STRING", "BOOLEAN", "NULL", "MUL", "DIV", "ADD", 
			"SUB", "ID", "NEWLINE", "COMMENT", "EQ", "NEQ", "LT", "GT", "LTE", "GTE", 
			"FUNC", "RETURN", "INVALID_CHAR"
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


	public MiniLangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MiniLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000!\u00cc\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0004\fj\b\f\u000b"+
		"\f\f\fk\u0001\r\u0004\ro\b\r\u000b\r\f\rp\u0001\r\u0001\r\u0004\ru\b\r"+
		"\u000b\r\f\rv\u0001\u000e\u0001\u000e\u0005\u000e{\b\u000e\n\u000e\f\u000e"+
		"~\t\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0003\u000f\u008b\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0004\u0015\u009b\b\u0015"+
		"\u000b\u0015\f\u0015\u009c\u0001\u0016\u0003\u0016\u00a0\b\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0005"+
		"\u0017\u00a8\b\u0017\n\u0017\f\u0017\u00ab\t\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f"+
		"\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001 \u0001 \u0000\u0000"+
		"!\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006"+
		"\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017"+
		"/\u00181\u00193\u001a5\u001b7\u001c9\u001d;\u001e=\u001f? A!\u0001\u0000"+
		"\u0004\u0001\u000009\u0001\u0000\"\"\u0002\u0000AZaz\u0002\u0000\n\n\r"+
		"\r\u00d3\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000"+
		"\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000"+
		"\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000"+
		"!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001"+
		"\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000"+
		"\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000"+
		"\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u00003"+
		"\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001\u0000"+
		"\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0000;\u0001\u0000\u0000\u0000"+
		"\u0000=\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000\u0000\u0000A"+
		"\u0001\u0000\u0000\u0000\u0001C\u0001\u0000\u0000\u0000\u0003I\u0001\u0000"+
		"\u0000\u0000\u0005K\u0001\u0000\u0000\u0000\u0007M\u0001\u0000\u0000\u0000"+
		"\tO\u0001\u0000\u0000\u0000\u000bR\u0001\u0000\u0000\u0000\rW\u0001\u0000"+
		"\u0000\u0000\u000f]\u0001\u0000\u0000\u0000\u0011`\u0001\u0000\u0000\u0000"+
		"\u0013b\u0001\u0000\u0000\u0000\u0015d\u0001\u0000\u0000\u0000\u0017f"+
		"\u0001\u0000\u0000\u0000\u0019i\u0001\u0000\u0000\u0000\u001bn\u0001\u0000"+
		"\u0000\u0000\u001dx\u0001\u0000\u0000\u0000\u001f\u008a\u0001\u0000\u0000"+
		"\u0000!\u008c\u0001\u0000\u0000\u0000#\u0091\u0001\u0000\u0000\u0000%"+
		"\u0093\u0001\u0000\u0000\u0000\'\u0095\u0001\u0000\u0000\u0000)\u0097"+
		"\u0001\u0000\u0000\u0000+\u009a\u0001\u0000\u0000\u0000-\u009f\u0001\u0000"+
		"\u0000\u0000/\u00a3\u0001\u0000\u0000\u00001\u00ae\u0001\u0000\u0000\u0000"+
		"3\u00b1\u0001\u0000\u0000\u00005\u00b4\u0001\u0000\u0000\u00007\u00b6"+
		"\u0001\u0000\u0000\u00009\u00b8\u0001\u0000\u0000\u0000;\u00bb\u0001\u0000"+
		"\u0000\u0000=\u00be\u0001\u0000\u0000\u0000?\u00c3\u0001\u0000\u0000\u0000"+
		"A\u00ca\u0001\u0000\u0000\u0000CD\u0005p\u0000\u0000DE\u0005r\u0000\u0000"+
		"EF\u0005i\u0000\u0000FG\u0005n\u0000\u0000GH\u0005t\u0000\u0000H\u0002"+
		"\u0001\u0000\u0000\u0000IJ\u0005(\u0000\u0000J\u0004\u0001\u0000\u0000"+
		"\u0000KL\u0005)\u0000\u0000L\u0006\u0001\u0000\u0000\u0000MN\u0005;\u0000"+
		"\u0000N\b\u0001\u0000\u0000\u0000OP\u0005i\u0000\u0000PQ\u0005f\u0000"+
		"\u0000Q\n\u0001\u0000\u0000\u0000RS\u0005e\u0000\u0000ST\u0005l\u0000"+
		"\u0000TU\u0005s\u0000\u0000UV\u0005e\u0000\u0000V\f\u0001\u0000\u0000"+
		"\u0000WX\u0005w\u0000\u0000XY\u0005h\u0000\u0000YZ\u0005i\u0000\u0000"+
		"Z[\u0005l\u0000\u0000[\\\u0005e\u0000\u0000\\\u000e\u0001\u0000\u0000"+
		"\u0000]^\u0005d\u0000\u0000^_\u0005o\u0000\u0000_\u0010\u0001\u0000\u0000"+
		"\u0000`a\u0005{\u0000\u0000a\u0012\u0001\u0000\u0000\u0000bc\u0005}\u0000"+
		"\u0000c\u0014\u0001\u0000\u0000\u0000de\u0005=\u0000\u0000e\u0016\u0001"+
		"\u0000\u0000\u0000fg\u0005,\u0000\u0000g\u0018\u0001\u0000\u0000\u0000"+
		"hj\u0007\u0000\u0000\u0000ih\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000"+
		"\u0000ki\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000l\u001a\u0001"+
		"\u0000\u0000\u0000mo\u0007\u0000\u0000\u0000nm\u0001\u0000\u0000\u0000"+
		"op\u0001\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000"+
		"\u0000qr\u0001\u0000\u0000\u0000rt\u0005.\u0000\u0000su\u0007\u0000\u0000"+
		"\u0000ts\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000vt\u0001\u0000"+
		"\u0000\u0000vw\u0001\u0000\u0000\u0000w\u001c\u0001\u0000\u0000\u0000"+
		"x|\u0005\"\u0000\u0000y{\b\u0001\u0000\u0000zy\u0001\u0000\u0000\u0000"+
		"{~\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000"+
		"\u0000}\u007f\u0001\u0000\u0000\u0000~|\u0001\u0000\u0000\u0000\u007f"+
		"\u0080\u0005\"\u0000\u0000\u0080\u001e\u0001\u0000\u0000\u0000\u0081\u0082"+
		"\u0005t\u0000\u0000\u0082\u0083\u0005r\u0000\u0000\u0083\u0084\u0005u"+
		"\u0000\u0000\u0084\u008b\u0005e\u0000\u0000\u0085\u0086\u0005f\u0000\u0000"+
		"\u0086\u0087\u0005a\u0000\u0000\u0087\u0088\u0005l\u0000\u0000\u0088\u0089"+
		"\u0005s\u0000\u0000\u0089\u008b\u0005e\u0000\u0000\u008a\u0081\u0001\u0000"+
		"\u0000\u0000\u008a\u0085\u0001\u0000\u0000\u0000\u008b \u0001\u0000\u0000"+
		"\u0000\u008c\u008d\u0005n\u0000\u0000\u008d\u008e\u0005u\u0000\u0000\u008e"+
		"\u008f\u0005l\u0000\u0000\u008f\u0090\u0005l\u0000\u0000\u0090\"\u0001"+
		"\u0000\u0000\u0000\u0091\u0092\u0005*\u0000\u0000\u0092$\u0001\u0000\u0000"+
		"\u0000\u0093\u0094\u0005/\u0000\u0000\u0094&\u0001\u0000\u0000\u0000\u0095"+
		"\u0096\u0005+\u0000\u0000\u0096(\u0001\u0000\u0000\u0000\u0097\u0098\u0005"+
		"-\u0000\u0000\u0098*\u0001\u0000\u0000\u0000\u0099\u009b\u0007\u0002\u0000"+
		"\u0000\u009a\u0099\u0001\u0000\u0000\u0000\u009b\u009c\u0001\u0000\u0000"+
		"\u0000\u009c\u009a\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000"+
		"\u0000\u009d,\u0001\u0000\u0000\u0000\u009e\u00a0\u0005\r\u0000\u0000"+
		"\u009f\u009e\u0001\u0000\u0000\u0000\u009f\u00a0\u0001\u0000\u0000\u0000"+
		"\u00a0\u00a1\u0001\u0000\u0000\u0000\u00a1\u00a2\u0005\n\u0000\u0000\u00a2"+
		".\u0001\u0000\u0000\u0000\u00a3\u00a4\u0005/\u0000\u0000\u00a4\u00a5\u0005"+
		"/\u0000\u0000\u00a5\u00a9\u0001\u0000\u0000\u0000\u00a6\u00a8\b\u0003"+
		"\u0000\u0000\u00a7\u00a6\u0001\u0000\u0000\u0000\u00a8\u00ab\u0001\u0000"+
		"\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000\u00a9\u00aa\u0001\u0000"+
		"\u0000\u0000\u00aa\u00ac\u0001\u0000\u0000\u0000\u00ab\u00a9\u0001\u0000"+
		"\u0000\u0000\u00ac\u00ad\u0006\u0017\u0000\u0000\u00ad0\u0001\u0000\u0000"+
		"\u0000\u00ae\u00af\u0005=\u0000\u0000\u00af\u00b0\u0005=\u0000\u0000\u00b0"+
		"2\u0001\u0000\u0000\u0000\u00b1\u00b2\u0005!\u0000\u0000\u00b2\u00b3\u0005"+
		"=\u0000\u0000\u00b34\u0001\u0000\u0000\u0000\u00b4\u00b5\u0005<\u0000"+
		"\u0000\u00b56\u0001\u0000\u0000\u0000\u00b6\u00b7\u0005>\u0000\u0000\u00b7"+
		"8\u0001\u0000\u0000\u0000\u00b8\u00b9\u0005<\u0000\u0000\u00b9\u00ba\u0005"+
		"=\u0000\u0000\u00ba:\u0001\u0000\u0000\u0000\u00bb\u00bc\u0005>\u0000"+
		"\u0000\u00bc\u00bd\u0005=\u0000\u0000\u00bd<\u0001\u0000\u0000\u0000\u00be"+
		"\u00bf\u0005f\u0000\u0000\u00bf\u00c0\u0005u\u0000\u0000\u00c0\u00c1\u0005"+
		"n\u0000\u0000\u00c1\u00c2\u0005c\u0000\u0000\u00c2>\u0001\u0000\u0000"+
		"\u0000\u00c3\u00c4\u0005r\u0000\u0000\u00c4\u00c5\u0005e\u0000\u0000\u00c5"+
		"\u00c6\u0005t\u0000\u0000\u00c6\u00c7\u0005u\u0000\u0000\u00c7\u00c8\u0005"+
		"r\u0000\u0000\u00c8\u00c9\u0005n\u0000\u0000\u00c9@\u0001\u0000\u0000"+
		"\u0000\u00ca\u00cb\t\u0000\u0000\u0000\u00cbB\u0001\u0000\u0000\u0000"+
		"\t\u0000kpv|\u008a\u009c\u009f\u00a9\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}