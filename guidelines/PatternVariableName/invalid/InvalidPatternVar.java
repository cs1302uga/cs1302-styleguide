package edu.uga.cs1302.example;

/**
 * Invalid pattern variable names.
 */
public class InvalidPatternVar {

    /**
     * Method with invalid pattern variable.
     *
     * @param obj object to check
     */
    public void check(Object obj) {
        if (obj instanceof String StringVal) {
            System.out.println(StringVal.length());
        } // if
        if (obj instanceof String string_val) {
            System.out.println(string_val.length());
        } // if
    } // check

} // InvalidPatternVar
