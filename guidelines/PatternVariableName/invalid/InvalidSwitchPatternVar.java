package edu.uga.cs1302.example;

/**
 * Invalid pattern variable names in switch expression.
 */
public class InvalidSwitchPatternVar {

    /**
     * Process object using switch pattern matching with invalid identifier.
     *
     * @param obj object to process
     * @return description string
     */
    public String process(Object obj) {
        return switch (obj) {
            case Integer IntVal -> "Integer: " + (IntVal * 2);
            default -> "Unknown";
        };
    } // process

} // InvalidSwitchPatternVar
