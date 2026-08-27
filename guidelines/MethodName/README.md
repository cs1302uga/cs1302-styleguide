### MethodName

Method names must be written in `lowerCamelCase`.

Method names are typically verbs or verb phrases that clearly describe the action performed (e.g., `calculateTotal`, `findById`, `isEmpty`, `printSummary`).

#### Valid Examples

```java
// Valid: lowerCamelCase method names
public double calculateAverage(int[] scores) {
    return 0.0;
} // calculateAverage

public boolean hasNext() {
    return false;
} // hasNext

public void printReport() {
} // printReport
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase starting letter (UpperCamelCase)
public double CalculateAverage(int[] scores) {
    return 0.0;
} // CalculateAverage
```

```java
// Invalid: Snake_case with underscores
public void print_report() {
} // print_report
```

#### How to Fix

- Start the method name with a lowercase letter and capitalize the first letter of each subsequent word without underscores.

#### Rationale & Instructor Notes

**Rationale:**
`lowerCamelCase` naming prevents methods from being visually confused with class constructors or type definitions.

**Instructor Note:**
Students coming from Python or C often write `calculate_average()` or from C# write `CalculateAverage()`. In Java, always use `calculateAverage()`.
