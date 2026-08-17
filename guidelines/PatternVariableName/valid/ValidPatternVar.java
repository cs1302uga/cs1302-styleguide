package edu.uga.cs1302.example;

/**
 * Valid pattern variable names.
 */
public class ValidPatternVar {

    /**
     * Method with valid pattern variable.
     *
     * @param obj object to check
     */
    public void check(Object obj) {
        if (obj instanceof String stringVal) {
            System.out.println(stringVal.length());
        } // if
    } // check

} // ValidPatternVar
