### PatternVariableName

Pattern variable names introduced in `instanceof` pattern matching or switch pattern matching must be written in `lowerCamelCase` or declared as an unnamed pattern variable using a single underscore (`_`).

#### Valid Examples

```java
// Valid: lowerCamelCase pattern variable in instanceof
if (obj instanceof String stringVal) {
    System.out.println(stringVal.length());
} // if

// Valid: Unnamed pattern variable when the matched instance is unused
if (obj instanceof String _) {
    System.out.println("Object is a string instance");
} // if

// Valid: Pattern matching in switch expressions
String description = switch (shape) {
    case Circle circleShape -> "Circle with radius " + circleShape.radius();
    case Rectangle rectShape -> "Rectangle with area " + (rectShape.width() * rectShape.height());
    default -> "Unknown shape";
};
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase starting letter
if (obj instanceof String StringVal) {
    System.out.println(StringVal);
} // if

// Invalid: Snake_case with underscores
if (obj instanceof String string_val) {
    System.out.println(string_val);
} // if
```

#### How to Fix

- Ensure pattern variables use standard `lowerCamelCase`.
- If the pattern variable is not used inside the matching block, declare it as an unnamed pattern variable `_` (Java 22+).

#### Rationale & Instructor Notes

**Rationale:**
Pattern variables act as scoped local variables. Following `lowerCamelCase` maintains uniformity across all variable declarations in Java.

**Instructor Note:**
Pattern matching for `instanceof` (Java 16+) and `switch` (Java 21+) simplifies type casting. When you only need to verify a type without using the casted reference, the unnamed variable `_` makes your intention explicitly clear.
