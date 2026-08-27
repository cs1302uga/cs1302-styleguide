### LambdaParameterName

Parameter names declared in lambda expressions must be written in `lowerCamelCase` or declared as an unnamed parameter using a single underscore (`_`).

#### Valid Examples

```java
// Valid: lowerCamelCase lambda parameter
list.forEach(elementItem -> System.out.println(elementItem));

// Valid: Multiple lambda parameters in lowerCamelCase
Comparator<String> comp = (firstStr, secondStr) -> firstStr.compareTo(secondStr);

// Valid: Unnamed parameter for unused arguments (Java 22+)
map.forEach((key, _) -> System.out.println("Key: " + key));
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase starting letter
list.forEach(ElementItem -> System.out.println(ElementItem));

// Invalid: Snake_case with underscores
Comparator<String> comp = (first_str, second_str) -> first_str.compareTo(second_str);
```

#### How to Fix

- Ensure lambda parameters start with a lowercase letter and use `lowerCamelCase`.
- If a lambda parameter is unused, use the unnamed identifier `_`.

#### Rationale & Instructor Notes

**Rationale:**
Lambda parameters are local identifiers and must conform to the universal `lowerCamelCase` naming convention used for all Java parameters and local variables. When declaring lambda parameters, you should ensure that their names conform to the suggestions in the Java Language Specification, sections [15.27.1](https://docs.oracle.com/javase/specs/jls/se21/html/jls-15.html#jls-15.27.1), [6.8.6](https://docs.oracle.com/javase/specs/jls/se21/html/jls-6.html#jls-6.8.6), and [6.1](https://docs.oracle.com/javase/specs/jls/se21/html/jls-6.html#jls-6.1).

**Instructor Note:**
Choose meaningful lambda parameter names (e.g., `event -> ...` or `e -> ...`, `student -> ...`) for lambda parameters, and use unnamed parameters (`_`) for unused parameters.
