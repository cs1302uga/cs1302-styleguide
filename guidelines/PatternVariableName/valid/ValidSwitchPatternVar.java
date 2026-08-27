package edu.uga.cs1302.example;

/**
 * Valid pattern variable names in switch expression.
 */
public class ValidSwitchPatternVar {

    /**
     * Process object using switch pattern matching.
     *
     * @param obj object to process
     * @return description string
     */
    public String process(Object obj) {
        return switch (obj) {
            case Integer intVal -> "Integer: " + (intVal * 2);
            case String strVal -> "String: " + strVal.length();
            case Double _ -> "Unnamed Double";
            case null -> "Null object";
            default -> "Unknown";
        };
    } // process

} // ValidSwitchPatternVar
