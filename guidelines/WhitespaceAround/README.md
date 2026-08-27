### WhitespaceAround

Operators, control keywords, and braces must be surrounded by appropriate whitespace.

Specifically:

* Binary and ternary operators (`+`, `-`, `*`, `/`, `=`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `&&`, `||`, `?`, `:`) must have a space on both sides.
* Control keywords (`if`, `for`, `while`, `switch`, `catch`, `synchronized`) must be followed by a space before the opening parenthesis `(`.
* Left curly braces `{` must be preceded by a space.
* Right curly braces `}` must be followed by a space when followed by keywords like `else`, `catch`, `finally`, or `while`.

Empty compact blocks (such as empty method, constructor, or interface declarations: `{}`) are exempt from requiring internal spaces.

#### Valid Examples

```java
// Valid: Spaces around operators, after keywords, and before braces
if (n == 0) {
    total = count + 1;
} else {
    total = count - 1;
} // if

while (n > 0) {
    n--;
} // while
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Missing space around equality operator '=='
if (n==0) {
    ...
} // if

// Invalid: Missing space between 'while' and '('
while(n > 0) {
    ...
} // while

// Invalid: Missing space before opening brace '{'
if (n == 0){
    ...
} // if
```

#### How to Fix

* Insert a single space on each side of binary operators (e.g. `a + b`, `x = y`, `score >= 90`).

* Insert a single space between control flow keywords and parentheses (e.g. `if (...)`, `for (...)`).

#### Rationale & Instructor Notes

**Rationale:**
Adequate whitespace around tokens prevents visual crowding, making expressions,
assignments, and control structures much easier to read and parse.

**Instructor Note:**
A common mistake in beginner code is jamming expressions together (e.g.,
`for(int i=0;i<10;i++)`). Use proper spacing: `for (int i = 0; i < 10; i++)`.
