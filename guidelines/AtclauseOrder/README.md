### AtclauseOrder

When multiple Javadoc block tags (`@...`) are present on a class, interface, enum, method, constructor, or field, they must appear in the following standard order:

1. `@param`
2. `@return`
3. `@throws`
4. `@see`
5. `@since`
6. `@serial` (or `@serialField`, `@serialData`)
7. `@deprecated`

#### Valid Examples

```java
/**
 * Searches the collection for the specified student identifier.
 *
 * @param studentId the unique integer identifier of the student
 * @param includeArchived whether to search archived academic records
 * @return the matching student record, or {@code null} if not found
 * @throws IllegalArgumentException if {@code studentId} is negative
 * @see #findStudentByName(String)
 */
public Student findStudent(int studentId, boolean includeArchived) {
    // search implementation
    return null;
} // findStudent
```

#### Common Pitfalls & Invalid Examples

```java
/**
 * Computes grade statistics.
 *
 * @return the calculated grade point average
 * @param grades array of numerical course grades  // Invalid: @return appears before @param
 * @throws NullPointerException if grades is null
 */
public double computeGpa(double[] grades) {
    return 0.0;
} // computeGpa
```

```java
/**
 * Encodes data into binary format.
 *
 * @see #decode(byte[])                           // Invalid: @see appears before @param/@return
 * @param data raw string to encode
 * @return byte array representation
 */
public byte[] encode(String data) {
    return new byte[0];
} // encode
```

#### How to Fix

- Reorder your Javadoc block tags so that all `@param` tags appear first, followed by `@return`, followed by all `@throws` tags, followed by any `@see` references.
- Group tags of the same type together (e.g., list all `@param` tags in the order the parameters appear in the method signature).

#### Rationale & Instructor Notes

**Rationale:**
Following a universal ordering convention allows developers and automated documentation tools to scan documentation comments for parameters, return values, exceptions, and references in a predictable, intuitive sequence.

**Instructor Note:**
In CS2 assignments, a very common mistake is placing `@return` before `@param` or scattering `@throws` tags between parameter descriptions. Always structure your Javadoc tags top-down: Inputs (`@param`) &rarr; Output (`@return`) &rarr; Errors (`@throws`).
