### LeftCurly

Left curly braces (`{`) that open code blocks (classes, interfaces, records, methods, constructors, and control structures) must always be placed at the end of the line that introduces the block (also known as Egyptian style, the One True Brace Style (1TBS), or the Kernighan and Ritchie (K&R) style).

#### Valid Examples

```java
// Valid: Left curly brace at the end of the class header line
public class StudentManager {

    // Valid: Left curly brace at the end of the method header line
    public void processGrades(int[] scores) {
        // Valid: Left curly brace at the end of the 'if' condition line
        if (scores.length > 0) {
            System.out.println("Processing...");
        } // if
    } // processGrades

} // StudentManager
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Left curly brace on its own line (Allman / C++ style)
public class StudentManager
{
    public void processGrades(int[] scores)
    {
        if (scores.length > 0)
        {
            System.out.println("Processing...");
        } // if
    } // processGrades
} // StudentManager
```

#### How to Fix

- Move any opening curly brace `{` that appears at the start of a line to the end of the preceding line, separated by a single space.

#### Rationale & Instructor Notes

**Rationale:**
Placing the opening brace at the end of the declaration line is the standard convention in the Java programming language, used by Oracle, Google, and the wider Java open-source community. It saves vertical screen space while preserving clear block visual hierarchy.

**Instructor Note:**
Students transitioning from C++ or C# often bring with them the Allman style (brace on a new line). In Java and CSCI 1302, always place `{` at the end of the line.
