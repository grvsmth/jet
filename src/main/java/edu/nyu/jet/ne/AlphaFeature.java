// -*- tab-width: 4 -*-
package edu.nyu.jet.ne;

import cc.mallet.pipe.Pipe;
import cc.mallet.types.Instance;
import cc.mallet.types.Token;
import cc.mallet.types.TokenSequence;

class AlphaFeature extends Pipe {
	private String prefix;

	public AlphaFeature(String prefix) {
		this.prefix = prefix;
	}

	public Instance pipe(Instance carrier) {
		TokenSequence tokens = (TokenSequence) carrier.getData();

		for (int i = 0; i < tokens.size(); i++) {
			Token token = tokens.get(i);
			StringBuilder buffer = new StringBuilder(prefix);

			String word = token.getText();
			for (int j = 0; j < word.length(); j++) {
				char ch = word.charAt(j);
				if (Character.isLowerCase(ch) || Character.isUpperCase(ch)) {
					buffer.append(ch);
				}
			}
			if (buffer.length() > prefix.length()) {
				token.setFeatureValue(buffer.toString(), 1.0);
			}
		}

		return carrier;
	}
}
