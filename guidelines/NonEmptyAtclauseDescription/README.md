### NonEmptyAtclauseDescription

Every Javadoc block tag (such as `@param`, `@return`, and `@throws`) must include a non-empty description.

```java
/**
 * Searches for a record by identifier.
 *
 * @param id the unique numeric identifier
 * @return the matching student record
 * @throws NoSuchElementException if no record with the given id exists
 */
public Student findById(int id) {
    ...
} // findById
```

```java
/**
 * @param id
 * @return
 */
public Student findById(int id) { // Invalid style: empty tag descriptions
    ...
} // findById
```

**Rationale:**
A Javadoc tag without a descriptive explanation provides no meaningful documentation beyond what is already visible in the method signature.
