### ParenPad

There must be no whitespace immediately following an opening parenthesis (`(`) or immediately preceding a closing parenthesis (`)`) in method calls, constructor calls, control flow expressions (`if`, `for`, `while`, `switch`), and type casts.

#### Valid Examples

```java
// Valid: No internal padding inside parentheses
if (score > 0) {
    String formatted = (String) rawObject;
    printReport(formatted, count);
} // if
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Space immediately following '(' and preceding ')'
if ( score > 0 ) {
    String formatted = ( String ) rawObject;
    printReport( formatted, count );
} // if
```

#### How to Fix

- Remove spaces directly adjacent to the inside of parentheses: write `(x)` instead of `( x )`.

#### Rationale & Instructor Notes

**Rationale:**
Internal padding inside parentheses adds unnecessary horizontal spacing and disrupts the visual grouping of expressions.

**Instructor Note:**
Keep spaces *outside* parentheses after keywords (e.g. `if (...)`), but keep the inside snug (`(condition)`).
