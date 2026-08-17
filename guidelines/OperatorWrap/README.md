### OperatorWrap

When a line-wrapped statement breaks across multiple lines at an operator (e.g., `+`, `-`, `*`, `/`, `&&`, `||`, `==`, `!=`, or `::`), the operator must wrap to the **new line** (i.e., appear at the beginning of the continuation line).

```java
// Valid style examples: operator wraps to the beginning of the continuation line

int total = value1 + value2
    + value3 + value4;

String message =
    "one, " +
    "two, " +
    "three";

if (condition1 && condition2
    && condition3) {
    ...
} // if

boolean isValid = firstCondition
    && secondCondition
    && thirdCondition;
```

```java
// Invalid style examples: operator remains at the end of the previous line

int total = value1 + value2 +
    value3 + value4;

String badMessage = "one, " +
    "two, " +
    "three";

if (condition1 && condition2 &&
    condition3) {
    ...
} // if

boolean isInvalid =
    firstCondition &&
    secondCondition &&
    thirdCondition;
```

**Rationale:**
Placing the operator at the beginning of the continuation line makes it immediately visible that the line is a continuation of the preceding expression.
