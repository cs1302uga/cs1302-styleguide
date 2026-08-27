package edu.uga.cs1302.example;

/**
 * Valid switch expression indentation.
 */
public class ValidSwitchExpression {

    /**
     * Categorize day of week.
     *
     * @param day numeric day (1-7)
     * @return name of day category
     */
    public String getDayCategory(int day) {
        String category = switch (day) {
            case 1, 7 -> "Weekend";
            case 2, 3, 4, 5, 6 -> "Weekday";
            default -> {
                String error = "Invalid day: " + day;
                yield error;
            }
        };
        return category;
    } // getDayCategory

} // ValidSwitchExpression
