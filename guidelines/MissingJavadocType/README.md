### MissingJavadocType

All top-level and nested class, interface, record, enum, and annotation interface definitions must have Javadoc documentation summarizing their purpose and responsibility.

#### Valid Examples

```java
/**
 * Represents a student enrolled in a university course.
 *
 * <p>
 * This class tracks student demographic information, registered credit hours,
 * and academic standing.
 */
public class Student {
    // class members
} // Student

/**
 * Defines the contract for processing payments in the e-commerce system.
 */
public interface PaymentProcessor {
    // interface methods
} // PaymentProcessor

/**
 * Immutable record representing a two-dimensional geometric coordinate point.
 *
 * @param x the horizontal coordinate
 * @param y the vertical coordinate
 */
public record Point(double x, double y) {
} // Point

/**
 * Enumeration of available letter grade options for course evaluation.
 */
public enum Grade {
    A, B, C, D, F
} // Grade
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Missing Javadoc comment on class definition
public class GradeCalculator {
    // implementation
} // GradeCalculator
```

```java
// Single-line comments do not count as Javadoc
/* Block comments with one asterisk do not count as Javadoc either */
public class CourseScheduler {
    // implementation
} // CourseScheduler
```

#### How to Fix

- Add a Javadoc comment starting with `/**` (note the double asterisk) directly above the class, interface, record, or enum declaration.
- Provide at least one complete summary sentence ending with a period describing what the type represents.

#### Rationale & Instructor Notes

**Rationale:**
Type documentation provides essential high-level context about architecture, responsibilities, invariants, and intended usage. It is the primary overview prospective users of your library read first.

**Instructor Note:**
In CS2, every `.java` file you submit must include a class-level Javadoc comment. Make sure your opening comment starts with `/**` and not `/*` or `//`.
