### LineLength

Java source code lines must not exceed **100 characters** in length (including indentation and trailing whitespace).

Lines that would exceed this limit must be manually line-wrapped in a readable, consistent manner (using 4-space continuation indentation).

The only permitted exceptions are:

* Lines where obeying the column limit is impossible (e.g., a long URL in a Javadoc `@see` tag);
* `package` and `import` statements; and
* Command-line shell examples in Javadoc or code comments intended for copy-pasting.

#### Valid Examples

```java
// Valid: Long expression wrapped cleanly across lines (each under 100 characters)
String studentSummary = "Student: " + student.getFirstName() + " " + student.getLastName()
    + ", ID: " + student.getId()
    + ", Major: " + student.getMajor();

// Valid: Long method invocation wrapped with arguments on continuation lines
boolean isEnrolled = enrollmentService.registerStudentForCourse(
    studentId,
    courseCode,
    termIdentifier
);
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Exceeds 100 characters on a single line
String logMessage = "System encountered an unexpected processing error while evaluating student grade records for term " + currentTerm;
```

#### How to Fix

* Break long mathematical or boolean expressions before operators, wrapping the operator to the next line (see [`OperatorWrap`](#operatorwrap)).
* Break method calls after opening parentheses or commas between arguments, indenting continuation lines by 4 spaces.
* Break long string literals into concatenated sub-strings across multiple lines.

#### Rationale & Instructor Notes

**Rationale:**
Limiting lines to 100 characters prevents horizontal scrolling in code editors, side-by-side git diff tools, terminal displays, and split-window IDE layouts.

**Instructor Note:**
In modern IDEs (VS Code, Eclipse, IntelliJ, Emacs), you can configure a visual line guide at column 100 to alert you when a line is nearing the boundary.
