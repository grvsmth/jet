package edu.nyu.jet.actions;

import edu.nyu.jet.tipster.Document;
import edu.nyu.jet.tipster.Span;

/**
 * User defined actions in Jet.
 *
 * @author yhe
 * @version 1.0
 */
public interface JetAction {
    boolean initialized();
    void initialize(String param);
    void process(Document doc, Span span);
    void process(Document doc);
}
