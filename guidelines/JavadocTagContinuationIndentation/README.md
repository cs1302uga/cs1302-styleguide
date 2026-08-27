### JavadocTagContinuationIndentation

When a Javadoc block tag description (such as for `@param`, `@return`, or `@throws`) wraps onto subsequent lines, the continuation line(s) must be indented at least **4 spaces** relative to the start of the tag line.

#### Valid Examples

```java
/**
 * Processes student enrollment and updates course registration records.
 *
 * @param studentName the full legal name of the student to look up
 *     in the departmental registration database
 * @param maxCredits maximum number of credit hours the student is
 *     authorized to enroll in for the specified term
 * @return the unique academic confirmation number assigned to the
 *     completed registration transaction
 * @throws IllegalArgumentException if the student name is null
 *     or consists only of whitespace
 */
public String enrollStudent(String studentName, int maxCredits) {
    // enrollment logic
    return "";
} // enrollStudent
```

#### Common Pitfalls & Invalid Examples

```java
/**
 * Retrieves course information.
 *
 * @param courseId unique four-digit departmental course identifier
 *   used for scheduling                                                // Invalid: indented only 2 spaces (must be >= 4)
 * @return the course catalog details
 */
public Course getCourse(int courseId) {
    return null;
} // getCourse
```

```java
/**
 * Parses user account input.
 *
 * @param rawInput raw string data
 * @throws ParseException
 * if parsing fails due to invalid format                              // Invalid: continuation line has 0-space indentation
 */
public Account parseAccount(String rawInput) throws ParseException {
    return null;
} // parseAccount
```

#### How to Fix

- When a `@param`, `@return`, or `@throws` description exceeds your editor line length and wraps to the next line, indent the continuation line with **4 spaces** after the leading ` * ` delimiter.

#### Rationale & Instructor Notes

**Rationale:**
Indenting tag continuation lines creates a clear visual distinction between where one tag's description ends and the next tag begins, preventing multi-line descriptions from looking like separate tags.

**Instructor Note:**
If you keep your tag descriptions concise, they will rarely need to wrap. When detailed explanations are necessary, ensure your continuation lines are indented by 4 spaces.
