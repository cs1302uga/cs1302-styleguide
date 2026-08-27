### Indentation

The following indentation rules must be followed:

| Property                  | Description                                                                     | Spaces |
|---------------------------|---------------------------------------------------------------------------------|--------|
| `basicOffset`             | how far the new indentation level should be indented when on the next line      | 4      |
| `braceAdjustment`         | how far a brace should be indented when on the next line                        | 0      |
| `caseIndent`              | how far a case label should be indented when on the next line                   | 0      |
| `throwsIndent`            | how far a throws clause should be indented when on the next line                | 4      |
| `arrayInitIndent`         | how far an array initializer list item should be indented when on the next line | 4      |
| `lineWrappingIndentation` | how far the continuation line should be indented when line-wrapping is present  | 4      |

Each new block level (classes, methods, control structures) must be indented
by exactly 4 spaces relative to the enclosing scope:

```java
// Valid style: 4-space indentation per block level
public class CalculationService {

    public void calculate() {
        int total = 0;
        if (total > 0) {
            total++;
        } // if
    } // calculate

} // CalculationService
```

```java
// Invalid style: 2-space indentation
public class CalculationService {

  public void calculate() {
    int total = 0;
    if (total > 0) {
      total++;
    } // if
  } // calculate

} // CalculationService
```

Case labels in a `switch` statement are aligned with the `switch` statement
(`caseIndent = 0`):

```java
// Valid style: switch statement with aligned case labels
public String getDayCategory(int day) {
    String category;
    switch (day) {
    case 1:
    case 7:
        category = "Weekend";
        break;
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
        category = "Weekday";
        break;
    default:
        category = "Invalid";
        break;
    } // switch
    return category;
} // getDayCategory
```

In a `switch` expression, `case` and `default` labels are indented by 4 spaces relative to the `switch` expression keyword, and `->` is used instead of `:` as the separator:

```java
// Valid style: switch expression with aligned case labels
public String getDayCategory(int day) {
    String category = switch (day) {
        case 1, 7 -> "Weekend";
        case 2, 3, 4, 5, 6 -> "Weekday";
        default -> {
            String error = "Invalid day: " + day;
            yield error;
        } // default
    };
    return category;
} // getDayCategory
```

Continuation lines for line wrapping, `throws` clauses, and multi-line array
initializers are indented by 4 spaces:

```java
// Valid style: 4-space continuation indentation
public void processItems(List<String> items)
    throws IllegalArgumentException, IllegalStateException {
    int[] numbers = new int[] {
        1,
        2,
        3
    };
} // processItems
```

Sometimes, indentation rules are a little hard to parse when parentheses and
curly braces are involved, as is sometimes the case with multi-line inline lambda
expressions. An inline lambda expression is a lambda expression that is supplied
as an argument for a parameter of a method. Here is an example:

```java
// BAD INDENTATION
Arrays.sort(array, (a, b) -> {
        return a.compareTo(b);  // 'block' child has incorrect indentation
    });                         // 'block rcurly' has incorrect indentation
```

```java
// GOOD INDENTATION
Arrays.sort(array, (a, b) -> {
    return a.compareTo(b);
});
```

If these rules make one of your inline lambda expressions look less readable,
then you are encouraged to refactor your lambda expression, if possible, to
avoid indentation. Here is the same inline lambda written using one line of
code:

```java
// HOWEVER, if you can write using one line, then please do so
Arrays.sort(array, (a, b) -> a.compareTo(b));
```

#### How to Fix

- Configure your text editor (e.g., Emacs, Vim, etc.) to insert **4 spaces** per tab press and disable hard tabs (`indent-tabs-mode nil` / `expandtab`).
- Indent each nested block level by exactly 4 spaces relative to its enclosing braces.
- Indent continuation lines (line wrapping, `throws` clauses, multi-line arrays) by 4 spaces.

#### Rationale & Instructor Notes

**Rationale:**
Consistent 4-space indentation establishes a clear visual hierarchy, making the scope and nesting of classes, methods, and control flow immediately apparent.

**Instructor Note:**
In CS2, never mix 2-space and 4-space indentation. If your editor indents by 2 spaces by default, adjust its settings to 4 spaces for Java files.
