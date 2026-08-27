### MethodTypeParameterName

Generic type parameter names for generic methods and constructors must conform to one of two formats:

1. A single uppercase letter optionally followed by a single digit (e.g., `T`, `E`, `K`, `V`, `T1`); or
2. An `UpperCamelCase` name ending with `T` or `Type` (e.g., `ResultT`, `ItemType`).

#### Valid Examples

```java
// Valid: Single uppercase letters on generic methods
public <T> T findFirst(List<T> list) {
    return list.isEmpty() ? null : list.get(0);
} // findFirst

// Valid: Descriptive names ending with T or Type
public <ResultT> ResultT executeQuery(String query, Class<ResultT> resultClass) {
    return null;
} // executeQuery
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Lowercase type parameter name
public <type> type getFirst(List<type> list) {
    return list.get(0);
} // getFirst

// Invalid: Multi-character name without T or Type suffix
public <Result> Result executeQuery(String query) {
    return null;
} // executeQuery
```

#### How to Fix

- Change method type parameters placed between `< >` before the return type to single uppercase letters (e.g., `<T>`) or `T`/`Type`-suffixed names (e.g., `<ResultT>`).

#### Rationale & Instructor Notes

**Rationale:**
Generic methods introduce scoped type variables. Conforming to the standard naming scheme ensures readers recognize that `<T>` denotes a generic type rather than a concrete return type.

**Instructor Note:**
In generic helper methods (e.g., sorting, searching, copying collections), `<T>` is universally understood.
