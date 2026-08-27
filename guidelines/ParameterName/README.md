### ParameterName

Method and constructor formal parameter names must be written in `lowerCamelCase`.

#### Valid Examples

```java
// Valid: lowerCamelCase formal parameters
public void setScore(int finalScore, String studentName) {
    // parameter assignment
} // setScore

public Course(String coursePrefix, int courseNumber) {
    // constructor initialization
} // Course
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase starting letter
public void setScore(int FinalScore, String studentName) {
} // setScore
```

```java
// Invalid: Snake_case with underscores
public void setScore(int finalScore, String student_name) {
} // setScore
```

#### How to Fix

- Ensure every formal parameter identifier begins with a lowercase letter and uses `lowerCamelCase` without underscores.
- Update any matching `@param` tags in your method Javadoc comments to reflect the corrected parameter name.

#### Rationale & Instructor Notes

**Rationale:**
Consistent parameter naming ensures clarity in API signatures, IDE auto-completion hints, and generated Javadoc pages across the entire codebase.

**Instructor Note:**
Parameter names should clearly communicate what information the method expects. Avoid vague single-letter names (like `x`, `y`, `s`) when a meaningful noun (like `targetElement`, `filePath`, `studentName`) clarifies the method's purpose.
