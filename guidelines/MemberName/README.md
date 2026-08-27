### MemberName

Non-static instance field names (member variables) must be written in `lowerCamelCase`.

#### Valid Examples

```java
public class Student {

    // Valid: lowerCamelCase instance variable names
    private String firstName;
    private String lastName;
    private int creditHours;
    private double gradePointAverage;

} // Student
```

#### Common Pitfalls & Invalid Examples

```java
public class Student {

    // Invalid: Uppercase starting letter
    private String FirstName;

    // Invalid: Snake_case with underscores
    private int credit_hours;

    // Invalid: Hungarian notation / leading prefix
    private String m_lastName;

} // Student
```

#### How to Fix

- Ensure instance fields start with a lowercase letter, use camelCase for subsequent words, and contain no underscores or prefix tags (such as `m_` or `s_`).

#### Rationale & Instructor Notes

**Rationale:**
Standardized field naming ensures that object attributes are easily readable and clearly distinguished from types and static constants.

**Instructor Note:**
Instance variables represent the internal state of an object. Keep names concise and self-descriptive in `lowerCamelCase`.
