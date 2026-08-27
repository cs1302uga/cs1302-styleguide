### LocalVariableName

Local variable names (variables declared inside methods, constructors, or block scopes) must be written in `lowerCamelCase`.

#### Valid Examples

```java
public void processTransaction() {
    int studentCount = 10;
    String firstName = "Ada";
    boolean hasCompleted = false;
    double currentBalance = 150.75;
} // processTransaction
```

#### Common Pitfalls & Invalid Examples

```java
public void processTransaction() {
    int StudentCount = 10;     // Invalid: Starts with uppercase letter
    String first_name = "Ada"; // Invalid: Contains underscore
    double TOTAL = 100.0;      // Invalid: CONSTANT_CASE is not used for local variables
} // processTransaction
```

#### How to Fix

- Ensure local variables begin with a lowercase letter and use `lowerCamelCase` without underscores.
- Even if a local variable is declared `final`, it remains a local variable and must follow `lowerCamelCase` (do not use `CONSTANT_CASE` for local variables).

#### Rationale & Instructor Notes

**Rationale:**
Consistent local variable naming creates clean visual distinction from type names (`UpperCamelCase`) and constants (`CONSTANT_CASE`), reducing cognitive load while reading algorithms.

**Instructor Note:**
Choose descriptive names for your local variables rather than single-letter names, except for simple loop counters (`i`, `j`, `k`).
