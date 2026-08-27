### OperatorWrap

When an expression wraps across multiple lines at an operator (e.g., `+`, `-`, `*`, `/`, `&&`, `||`, `==`, `!=`, `:`, or `::`), the operator must wrap to the **new line** (appearing at the beginning of the continuation line).

#### Valid Examples

```java
// Valid: Arithmetic operator wraps to start of continuation line
int total = value1 + value2
    + value3 + value4;

// Valid: String concatenation operator on continuation line
String message = "Header: "
    + "detail one, "
    + "detail two";

// Valid: Logical boolean operators on continuation lines
boolean isValid = hasValidId
    && isRegistered
    && !isSuspended;

// Valid: Method reference operator wraps to new line
Function<String, Integer> parser = Integer
    ::parseInt;
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Operator placed at the end of the previous line
int total = value1 + value2 +
    value3 + value4;

// Invalid: Trailing boolean operator
boolean isValid = hasValidId &&
    isRegistered &&
    !isSuspended;
```

#### How to Fix

- Move any operator at the end of a wrapped line to the beginning of the next continuation line, indented by 4 spaces.

#### Rationale & Instructor Notes

**Rationale:**
Placing operators at the beginning of continuation lines makes it immediately visually apparent that the line is continuing an ongoing expression rather than starting a new statement.

**Instructor Note:**
When splitting long `if` condition expressions across multiple lines, always place `&&` or `||` at the start of the next line.
