### OneStatementPerLine

Each Java statement must be placed on its own line. Combining multiple statements on a single line using semicolons is prohibited.

This rule applies to variable declarations, assignments, method invocations, loop constructs, `break`, `continue`, and `return` statements.

#### Valid Examples

```java
// Valid: Each statement on its own line
int count = 0;
count++;
System.out.println(count);
return count;
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Multiple assignment and print statements on a single line
int count = 0; count++; System.out.println(count);
```

```java
// Invalid: Placing 'if' condition and body statement on the same line
if (isDone) return;
```

```java
// Invalid: Multiple variable declarations on one line
int x = 10; int y = 20;
```

#### How to Fix

- Split combined statements across multiple lines, terminating each statement with a newline following the semicolon.
- Wrap single-line `if` statements with curly braces on multiple lines (as required by [`NeedBraces`](#needbraces) and [`LeftCurly`](#leftcurly)).

#### Rationale & Instructor Notes

**Rationale:**
Single-statement lines improve code readability, simplify visual code reviews, make git diffs precise, and ensure that debugger breakpoints can be placed accurately on individual operations.

**Instructor Note:**
In Java, statements are the fundamental unit of execution. Placing one statement per line keeps your code clean and easy to step through line-by-line in a debugger.
