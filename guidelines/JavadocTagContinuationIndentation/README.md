### JavadocTagContinuationIndentation

When a Javadoc block tag description (such as for `@param`, `@return`, or `@throws`) wraps onto subsequent lines, the continuation line(s) must be indented at least **4 spaces** relative to the tag line.

```java
/**
 * Processes student records.
 *
 * @param studentName the full legal name of the student to look up
 *     in the departmental registration database
 * @return the unique academic identifier assigned to the student
 * @throws IllegalArgumentException if the student name is null
 *     or consists only of whitespace
 */
public String lookupStudent(String studentName) {
    ...
} // lookupStudent
```

**Rationale:**
Indenting tag continuation lines visually groups multi-line descriptions with their associated tags and clearly distinguishes them from subsequent tags.
