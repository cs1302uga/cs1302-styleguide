### GenericWhitespace

Whitespace around generic type arguments and type parameters (the `<` and `>` angle brackets) must adhere to standard Java conventions:

* No whitespace precedes `<` in generic class/interface instantiations or declarations.
* No whitespace immediately follows `<` or precedes `>`.
* Whitespace follows `>` only if followed by a keyword, variable name, or operator.

```java
List<String> names = new ArrayList<>(); // valid style
Map<String, List<Integer>> map;         // valid style
```

```java
List < String > names = new ArrayList < > (); // invalid style
```

**Rationale:**
Consistent spacing around angle brackets ensures generic declarations remain compact, distinct from comparison operators, and visually clean.
