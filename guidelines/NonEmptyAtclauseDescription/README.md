### NonEmptyAtclauseDescription

Every Javadoc block tag (such as `@param`, `@return`, and `@throws`) must include a meaningful, non-empty description.

#### Valid Examples

```java
/**
 * Searches for a student record by its unique academic identifier.
 *
 * @param studentId the unique integer identifier assigned to the student
 * @return the matching {@code Student} instance, or {@code null} if no match is found
 * @throws NoSuchElementException if no student matching {@code studentId} exists
 */
public Student findById(int studentId) {
    // lookup implementation
    return null;
} // findById
```

#### Common Pitfalls & Invalid Examples

```java
/**
 * Searches for a student record.
 *
 * @param studentId                             // Invalid: empty description for @param
 * @return                                      // Invalid: empty description for @return
 * @throws NoSuchElementException               // Invalid: empty description for @throws
 */
public Student findById(int studentId) {
    return null;
} // findById
```

```java
/**
 * Calculates grade average.
 *
 * @param scores scores                         // Pitfall: trivial placeholder duplicating tag name
 * @return result                               // Pitfall: lacks descriptive value
 */
public double calculateAverage(double[] scores) {
    return 0.0;
} // calculateAverage
```

#### How to Fix

- Ensure every `@param`, `@return`, and `@throws` tag is followed by at least one descriptive word explaining what the parameter is, what the method returns, or under what specific condition the exception is thrown.
- Avoid simply repeating the parameter name; explain what value the parameter represents and any constraints on its value.

#### Rationale & Instructor Notes

**Rationale:**
A Javadoc tag with an empty or redundant description provides no documentation beyond what is already visible in the method header. Clear descriptions convey expectations, constraints, and side effects.

**Instructor Note:**
Good documentation answers "what" and "why", not just "what type". For example, for `@return`, write `@return the total count of active enrollments` rather than `@return int`.
