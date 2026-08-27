### CommentsIndentation

Block comments (`/* ... */`) and single-line comments (`// ...`) must have the exact same indentation level as the surrounding code block or the statement that immediately follows them.

#### Valid Examples

```java
// Valid: Comments indented to the exact indentation level of surrounding code
public void calculate() {
    // Initialize running counter
    int count = 0;

    /*
     * Iterate through all available records
     * and accumulate the total score.
     */
    for (int i = 0; i < scores.length; i++) {
        // Add current score
        count += scores[i];
    } // for
} // calculate
```

#### Common Pitfalls & Invalid Examples

```java
public void calculate() {
// Invalid: Comment indented too far to the left (0 spaces instead of 4)
    int count = 0;

        // Invalid: Comment indented too far to the right (8 spaces instead of 4)
    int total = 0;
} // calculate
```

#### How to Fix

- Align the comment's leading slashes (`//` or `/*`) with the indentation level of the code directly below or around it.

#### Rationale & Instructor Notes

**Rationale:**
Properly indented comments maintain the visual hierarchy of the enclosing code structure and prevent reading distractions.

**Instructor Note:**
Comments explaining a block or statement should line up horizontally with that statement. Trailing closing comments (e.g., `} // if`) belong on the same line as the closing brace.
