### GenericWhitespace

Whitespace around generic type arguments and type parameters (the `<` and `>` angle brackets) must adhere to standard Java conventions:

* No whitespace precedes `<` in generic class/interface instantiations, type declarations, or method declarations.
* No whitespace immediately follows `<` or immediately precedes `>`.
* Whitespace follows `>` only if followed by a keyword, variable name, or operator (not when followed by `(`, `)`, `[`, `]`, or `,`).

#### Valid Examples

```java
// Valid: Proper spacing around generic angle brackets
List<String> names = new ArrayList<>();
Map<String, List<Integer>> scoreMap = new HashMap<>();

public <T> T getFirst(List<T> items) {
    return items.isEmpty() ? null : items.get(0);
} // getFirst
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Spaces inside angle brackets
List< String > names = new ArrayList< >();

// Invalid: Space before opening angle bracket
List <String> names = new ArrayList<>();
```

#### How to Fix

* Remove any spaces immediately after `<` or before `>`.
* Remove any spaces before `<` in type declarations (e.g. write `List<String>`, not `List <String>`).

#### Rationale & Instructor Notes

**Rationale:**
Standard spacing around angle brackets ensures generic declarations remain compact and distinct from comparison operators (`<` and `>`).

**Instructor Note:**
When using generics, the diamond operator (`<>`) in constructor calls may be empty, but it must not have any spaces inside the angle brackets: `new ArrayList<>()`.
