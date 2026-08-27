### TypeName

Type names for classes, interfaces, records, enums, and annotation interfaces must be written in `UpperCamelCase` (PascalCase).

Such type names are typically nouns or noun phrases (e.g., `StudentRecord`, `LinkedList`, `GradeCalculator`). Interface names may also be nouns (e.g., `List`, `Map`) or adjectives describing capabilities (e.g., `Comparable`, `Readable`, `Iterable`).

#### Valid Examples

```java
// Valid: Classes and records in UpperCamelCase
public class GradeCalculator {
} // GradeCalculator

public record StudentRecord(String id, String name) {
} // StudentRecord

// Valid: Interfaces in UpperCamelCase
public interface DataFilter {
} // DataFilter

// Valid: Enums in UpperCamelCase
public enum Semester {
    FALL, SPRING, SUMMER
} // Semester
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Lowercase starting letter
public class gradeCalculator {
} // gradeCalculator
```

```java
// Invalid: Snake_case with underscores
public class Student_Record {
} // Student_Record
```

#### How to Fix

- Capitalize the first letter of each word in the type name and remove all underscores.
- Rename the `.java` file so that its filename exactly matches the public type name (as required by [`OuterTypeFilename`](#outertypefilename)).

#### Rationale & Instructor Notes

**Rationale:**
The `UpperCamelCase` convention immediately distinguishes type names from variables and methods (`lowerCamelCase`) and constants (`CONSTANT_CASE`), enabling developers to understand identifier roles instantly when scanning code.

**Instructor Note:**
In Java, naming a class `student` or `student_record` will cause Checkstyle errors. Remember to use `Student` or `StudentRecord`.
