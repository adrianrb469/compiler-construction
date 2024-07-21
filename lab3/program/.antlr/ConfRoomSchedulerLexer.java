// Generated from /Users/adrian/Documents/University/2024/s2/compilers/compiler-construction/lab3/program/ConfRoomScheduler.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ConfRoomSchedulerLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, NAME=9, 
		INT=10, ID=11, DATE=12, TIME=13, STRING=14, NEWLINE=15, WS=16;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "NAME", 
			"INT", "ID", "DATE", "TIME", "STRING", "NEWLINE", "WS", "DIGIT"
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


	public ConfRoomSchedulerLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ConfRoomScheduler.g4"; }

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
		"\u0004\u0000\u0010\u008b\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0004"+
		"\bV\b\b\u000b\b\f\bW\u0001\t\u0004\t[\b\t\u000b\t\f\t\\\u0001\n\u0004"+
		"\n`\b\n\u000b\n\f\na\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r"+
		"\u0005\rw\b\r\n\r\f\rz\t\r\u0001\r\u0001\r\u0001\u000e\u0003\u000e\u007f"+
		"\b\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0004\u000f\u0084\b\u000f"+
		"\u000b\u000f\f\u000f\u0085\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0000\u0000\u0011\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0000\u0001\u0000\u0005\u0002"+
		"\u0000AZaz\u0001\u000009\u0003\u000009AZaz\u0003\u0000\n\n\r\r\"\"\u0002"+
		"\u0000\t\t  \u008f\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000"+
		"\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000"+
		"\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000"+
		"\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000"+
		"\u0000\u0001#\u0001\u0000\u0000\u0000\u0003+\u0001\u0000\u0000\u0000\u0005"+
		"0\u0001\u0000\u0000\u0000\u00073\u0001\u0000\u0000\u0000\t8\u0001\u0000"+
		"\u0000\u0000\u000b;\u0001\u0000\u0000\u0000\rA\u0001\u0000\u0000\u0000"+
		"\u000fM\u0001\u0000\u0000\u0000\u0011U\u0001\u0000\u0000\u0000\u0013Z"+
		"\u0001\u0000\u0000\u0000\u0015_\u0001\u0000\u0000\u0000\u0017c\u0001\u0000"+
		"\u0000\u0000\u0019n\u0001\u0000\u0000\u0000\u001bt\u0001\u0000\u0000\u0000"+
		"\u001d~\u0001\u0000\u0000\u0000\u001f\u0083\u0001\u0000\u0000\u0000!\u0089"+
		"\u0001\u0000\u0000\u0000#$\u0005R\u0000\u0000$%\u0005E\u0000\u0000%&\u0005"+
		"S\u0000\u0000&\'\u0005E\u0000\u0000\'(\u0005R\u0000\u0000()\u0005V\u0000"+
		"\u0000)*\u0005E\u0000\u0000*\u0002\u0001\u0000\u0000\u0000+,\u0005R\u0000"+
		"\u0000,-\u0005O\u0000\u0000-.\u0005O\u0000\u0000./\u0005M\u0000\u0000"+
		"/\u0004\u0001\u0000\u0000\u000001\u0005A\u0000\u000012\u0005T\u0000\u0000"+
		"2\u0006\u0001\u0000\u0000\u000034\u0005F\u0000\u000045\u0005R\u0000\u0000"+
		"56\u0005O\u0000\u000067\u0005M\u0000\u00007\b\u0001\u0000\u0000\u0000"+
		"89\u0005T\u0000\u00009:\u0005O\u0000\u0000:\n\u0001\u0000\u0000\u0000"+
		";<\u0005E\u0000\u0000<=\u0005V\u0000\u0000=>\u0005E\u0000\u0000>?\u0005"+
		"N\u0000\u0000?@\u0005T\u0000\u0000@\f\u0001\u0000\u0000\u0000AB\u0005"+
		"D\u0000\u0000BC\u0005E\u0000\u0000CD\u0005S\u0000\u0000DE\u0005C\u0000"+
		"\u0000EF\u0005R\u0000\u0000FG\u0005I\u0000\u0000GH\u0005P\u0000\u0000"+
		"HI\u0005T\u0000\u0000IJ\u0005I\u0000\u0000JK\u0005O\u0000\u0000KL\u0005"+
		"N\u0000\u0000L\u000e\u0001\u0000\u0000\u0000MN\u0005C\u0000\u0000NO\u0005"+
		"A\u0000\u0000OP\u0005N\u0000\u0000PQ\u0005C\u0000\u0000QR\u0005E\u0000"+
		"\u0000RS\u0005L\u0000\u0000S\u0010\u0001\u0000\u0000\u0000TV\u0007\u0000"+
		"\u0000\u0000UT\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000WU\u0001"+
		"\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000X\u0012\u0001\u0000\u0000"+
		"\u0000Y[\u0007\u0001\u0000\u0000ZY\u0001\u0000\u0000\u0000[\\\u0001\u0000"+
		"\u0000\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]\u0014"+
		"\u0001\u0000\u0000\u0000^`\u0007\u0002\u0000\u0000_^\u0001\u0000\u0000"+
		"\u0000`a\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000\u0000ab\u0001\u0000"+
		"\u0000\u0000b\u0016\u0001\u0000\u0000\u0000cd\u0003!\u0010\u0000de\u0003"+
		"!\u0010\u0000ef\u0005/\u0000\u0000fg\u0003!\u0010\u0000gh\u0003!\u0010"+
		"\u0000hi\u0005/\u0000\u0000ij\u0003!\u0010\u0000jk\u0003!\u0010\u0000"+
		"kl\u0003!\u0010\u0000lm\u0003!\u0010\u0000m\u0018\u0001\u0000\u0000\u0000"+
		"no\u0003!\u0010\u0000op\u0003!\u0010\u0000pq\u0005:\u0000\u0000qr\u0003"+
		"!\u0010\u0000rs\u0003!\u0010\u0000s\u001a\u0001\u0000\u0000\u0000tx\u0005"+
		"\"\u0000\u0000uw\b\u0003\u0000\u0000vu\u0001\u0000\u0000\u0000wz\u0001"+
		"\u0000\u0000\u0000xv\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000"+
		"y{\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000{|\u0005\"\u0000\u0000"+
		"|\u001c\u0001\u0000\u0000\u0000}\u007f\u0005\r\u0000\u0000~}\u0001\u0000"+
		"\u0000\u0000~\u007f\u0001\u0000\u0000\u0000\u007f\u0080\u0001\u0000\u0000"+
		"\u0000\u0080\u0081\u0005\n\u0000\u0000\u0081\u001e\u0001\u0000\u0000\u0000"+
		"\u0082\u0084\u0007\u0004\u0000\u0000\u0083\u0082\u0001\u0000\u0000\u0000"+
		"\u0084\u0085\u0001\u0000\u0000\u0000\u0085\u0083\u0001\u0000\u0000\u0000"+
		"\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u0087\u0001\u0000\u0000\u0000"+
		"\u0087\u0088\u0006\u000f\u0000\u0000\u0088 \u0001\u0000\u0000\u0000\u0089"+
		"\u008a\u0007\u0001\u0000\u0000\u008a\"\u0001\u0000\u0000\u0000\u0007\u0000"+
		"W\\ax~\u0085\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}