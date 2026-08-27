### NeedBraces

Curly braces are required for all control flow statements (`if`, `else`, `for`, `do`, `while`, and `switch`), even when the body contains only a single statement or is empty.

#### Valid Examples

```java
// Valid: Single-statement 'if' with curly braces and closing comment
if (score >= 90) {
    grade = "A";
} // if

// Valid: 'for' loop with braces
for (int i = 0; i < items.length; i++) {
    System.out.println(items[i]);
} // for

// Valid: 'while' loop with braces
while (scanner.hasNextLine()) {
    processLine(scanner.nextLine());
} // while
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Missing curly braces around single-line 'if' body
if (score >= 90)
    grade = "A";
```

```java
// Invalid: Missing braces on 'while' loop
while (hasMoreTokens())
    nextToken();
```

#### How to Fix

- Always wrap the body of `if`, `else`, `for`, `do`, and `while` statements in curly braces `{ ... }`, placing the opening brace on the same line as the conditional header.
- Add an end-of-block trailing comment after the closing curly brace indicating the control construct (e.g., `} // if`, `} // for`, `} // while`).

#### Rationale & Instructor Notes

**Rationale:**
In Java, omitting curly braces causes only the immediately following single statement to be bound to the conditional. Adding a second statement later without adding braces creates a notorious logic bug ("dangling else" or unconditioned execution) that is often invisible at a glance.

**Instructor Note:**
One of the most frequent bugs in introductory and intermediate programming occurs when a student adds a `System.out.println(...)` or cleanup step under an unbraced `if` statement, expecting it to run conditionally. Always using curly braces prevents this entire class of bugs.
