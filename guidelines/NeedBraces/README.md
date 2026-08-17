### NeedBraces

Curly braces are always used where technically optional. Braces should be used with
`if`, `else`, `for`, `do`, and `while` statements, even when the body is empty
or contains only a single statement.

**Rationale:**
Consider `if` statements without curly braces. In Java, only the first statement
following such `if` statements is executed when the conditional's expression
evaluates to `true`. Potential bugs can be avoided by using curly braces to
clearly indicate what statement or statements are to execute when the
conditional's expression evaluates to `true`.

**Instructor Note:**
One common bug that we've seen over the years is students adding statements
to a brace-less `if` statement with the intent that those statements only
execute when the conditional's expression evaluates to `true`. That is,
they forgot to add the curly braces. This guideline helps protect you
against that scenario and improves readability.
