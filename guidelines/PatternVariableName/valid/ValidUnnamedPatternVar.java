package edu.uga.cs1302.example;

/**
 * Valid unnamed pattern variable.
 */
public class ValidUnnamedPatternVar {

    /**
     * Method with valid unnamed pattern variable.
     *
     * @param obj object to check
     */
    public void check(Object obj) {
        if (obj instanceof String _) {
            System.out.println("Object is a string");
        } // if
    } // check

} // ValidUnnamedPatternVar
