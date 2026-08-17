### CommentsIndentation

Block comments (`/* ... */`) and single-line comments (`// ...`) must have the same indentation level as the surrounding code block or the statement that immediately follows them.

```java
// Valid style: comment indented to the same level as the code
public void calculate() {
    // initialize counter
    int count = 0;
} // calculate
```

```java
// Invalid style: comment incorrectly indented
public void calculate() {
// initialize counter (too far left)
    int count = 0;
        // initialize total (too far right)
    int total = 0;
} // calculate
```

**Rationale:**
Comments that align with surrounding code create clean visual hierarchy and improve readability.
