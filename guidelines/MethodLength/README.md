### MethodLength

The bodies of methods and constructors must not exceed **60 lines**.

This count includes the method header line with the opening curly brace `{`, all statements, comments, and blank lines within the method body, and the closing curly brace `}`. It does not include the method's preceding Javadoc comment block.

#### Valid Examples

```java
// Valid: Concise, focused method (well under 60 lines)
public double calculateTotalScore(double[] examScores, double labScore) {
    double total = 0.0;
    for (int i = 0; i < examScores.length; i++) {
        total += examScores[i];
    } // for
    double average = total / examScores.length;
    return (average * 0.7) + (labScore * 0.3);
} // calculateTotalScore
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Monolithic method exceeding 60 lines
public void processFullSemesterData(Scanner fileScanner) {
    // 65 lines of parsing, validation, database insertion, and report generation
} // processFullSemesterData
```

#### How to Fix

- Decompose monolithic methods into smaller, reusable private helper methods (functional decomposition).
- Extract repetitive logic into helper functions or loop constructs.
- Separate business logic from I/O parsing and UI formatting.

#### Rationale & Instructor Notes

**Rationale:**
Short, focused methods are easier to read, test, debug, and reason about. When a method exceeds 60 lines, it almost always violates the Single Responsibility Principle.

**Instructor Note:**
A good guideline is that an entire method should fit comfortably on your editor screen without scrolling. If a method is growing beyond 40-50 lines, start extracting helper methods.
