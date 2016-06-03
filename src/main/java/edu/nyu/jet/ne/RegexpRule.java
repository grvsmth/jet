package edu.nyu.jet.ne;

import java.util.regex.Pattern;

import edu.nyu.jet.tipster.Annotation;
import edu.nyu.jet.tipster.Document;

public class RegexpRule {
	private MatchType matchType;

	private Pattern pattern;

	public RegexpRule(MatchType type, String pattern) {
		this.matchType = type;
		this.pattern = Pattern.compile(pattern);
	}

	public boolean accept(Document doc, Annotation[] tokens, int pos) {
		if (this.matchType == MatchType.ANY) {
			return true;
		}

		String token = doc.normalizedText(tokens[pos]);
		boolean matched = pattern.matcher(token).matches();
		boolean ret;

		switch (matchType) {
		case NORMAL:
			ret = matched;
			break;

		case NOT:
			ret = !matched;
			break;

		default:
			throw new InternalError();
		}

		return ret;
	}
}
