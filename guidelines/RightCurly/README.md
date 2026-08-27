### RightCurly

Right curly braces (`}`) for single-part code blocks must appear on their own separate line, aligned with the start of the statement that opened the block.

For multi-block statements (such as `if`/`else if`/`else`, `try`/`catch`/`finally`, and `do`/`while`), the right curly brace must appear on the same line as the keyword that begins the next block (e.g., `} else {`, `} catch (...) {`, `} finally {`, `} while (...);`).

#### Valid Examples

```java
// Valid: Single block right curly brace on its own line
if (isValid) {
    process();
} // if

// Valid: Multi-block statements with right curly on the same line as next keyword
if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else {
    grade = "C";
} // if

// Valid: try-catch-finally multi-block alignment
try {
    readFile(filename);
} catch (IOException ioe) {
    handleError(ioe);
} finally {
    cleanup();
} // try

// Valid: do-while loop
do {
    count++;
} while (count < 10);
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Right curly brace separated from 'else' onto a different line
if (score >= 90) {
    grade = "A";
}
else {
    grade = "B";
} // if
```

```java
// Invalid: Right curly brace separated from 'catch'
try {
    readFile(filename);
}
catch (IOException ioe) {
    handleError(ioe);
} // try
```

#### How to Fix

- In `if-else` chains, place `} else {` and `} else if (...) {` on a single continuous line.
- In `try-catch-finally` constructs, place `} catch (...) {` and `} finally {` on the same line as the closing brace of the preceding block.
- In `do-while` loops, place `} while (...);` on the same line as the closing brace.

#### Rationale & Instructor Notes

**Rationale:**
Keeping related control flow clauses on the same line visually unifies the multi-part structure into a cohesive compound statement rather than disjoint blocks.

**Instructor Note:**
In CSCI 1302, it is customary, but not required, to place closing block comments (e.g., `} // if` or `} // try`) just after a final closing brace for a block to help with debugging and understanding the code. The comment should match the keyword that opens the block, and should be indented to align with the opening keyword for the block. This note applies to single-block and multi-block control flow structures alike.
