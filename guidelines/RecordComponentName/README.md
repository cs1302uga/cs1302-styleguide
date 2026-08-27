### RecordComponentName

Record component names declared in Java record headers must be written in `lowerCamelCase`.

#### Valid Examples

```java
// Valid: Record components in lowerCamelCase
public record StudentRecord(String firstName, String lastName, int studentId) {
    ...
} // StudentRecord

public record CourseEnrollment(String courseCode, int sectionNumber, boolean isWaitlisted) {
    ...
} // CourseEnrollment
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase start and underscore
public record StudentRecord(String FirstName, int student_id) {
} // StudentRecord
```

#### How to Fix

- Write all record components in `lowerCamelCase` without underscores.
- If you document record components in the class Javadoc with `@param`, ensure the `@param` tag names match the component names.

#### Rationale & Instructor Notes

**Rationale:**
In Java records, each record component automatically generates a `private final` instance field and a `public` method with the exact same name as the component (e.g., `firstName()`). Naming components in `lowerCamelCase` guarantees that these generated methods follow Java naming conventions.

**Instructor Note:**
Java records are a modern language feature (standard since Java 16) for creating transparent, immutable data carriers. Always name the components using `lowerCamelCase`.
