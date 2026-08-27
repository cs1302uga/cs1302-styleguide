### EmptyBlock

Empty code blocks are prohibited. Every code block (`class`, `interface`, `method`, `constructor`, `if`, `else`, `for`, `while`, `do-while`, `switch`, `try`, `finally`) must contain at least one executable statement or valid explanatory comment.

#### Valid Examples

```java
// Valid: Block contains executable statements
if (list.isEmpty()) {
    System.out.println("List is empty");
} // if

// Valid: Overridden interface method with documented no-op implementation
@Override
public void windowClosing(WindowEvent e) {
    // Intentionally left empty as no action is required on window closing
} // windowClosing
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Empty 'if' block
if (isValid) {
} // if
```

```java
// Invalid: Empty 'else' block
if (score > 50) {
    passed = true;
} else {
} // if
```

#### How to Fix

- If an `if` or `else` block is empty, invert your conditional expression or remove the unneeded clause entirely.
- If an empty method is required by an interface or abstract class, add an explicit explanatory comment explaining why no operation is performed.
- For empty `catch` blocks, refer to the [`EmptyCatchBlock`](#emptycatchblock) guideline.

#### Rationale & Instructor Notes

**Rationale:**
Empty code blocks often indicate forgotten logic, leftover debugging code, or inverted conditional logic that confuses readers and introduces subtle execution bugs.

**Instructor Note:**
If you write `if (condition) {} else { doSomething(); }`, then simplify it to `if (!condition) { doSomething(); }` to avoid the empty block.
