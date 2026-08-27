### MethodParamPad

There must be no whitespace between a method, constructor, or annotation identifier and its opening parenthesis (`(`).

#### Valid Examples

```java
// Valid: Opening parenthesis directly adjacent to method name
public void calculateTotal(int count) {
    doSomething();
    String formatted = String.format("Count: %d", count);
} // calculateTotal
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Space before opening parenthesis in method declaration
public void calculateTotal (int count) {
    // Invalid: Space before opening parenthesis in method call
    doSomething ();
} // calculateTotal
```

#### How to Fix

- Remove the space between the method or constructor name and the opening parenthesis `(`.

#### Rationale & Instructor Notes

**Rationale:**
Placing `(` immediately adjacent to the identifier clearly distinguishes method calls and declarations from control flow statements (such as `if (...)` or `while (...)`), which *do* require a preceding space.

**Instructor Note:**
Rule of thumb: Keywords get a space before `(` (e.g. `if (x)`), but method names do NOT get a space (e.g. `foo(x)`).
