### ClassTypeParameterName

Generic type parameter names for generic classes must conform to one of two formats:

1. A single uppercase letter optionally followed by a single digit (e.g., `E`, `T`, `K`, `V`, `T1`); or
2. An `UpperCamelCase` name ending with `T` or `Type` (e.g., `ElementT`, `RequestType`, `DataT`).

#### Valid Examples

```java
// Valid: Single uppercase letters
public class CustomList<E> {
} // CustomList<E>

// Valid: Descriptive names ending with T or Type
public class ApiResponse<DataT> {
} // ApiResponse<DataT>

public class DatabaseSession<ContextType> {
} // DatabaseSession<ContextType>
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Lowercase type parameter name
public class CustomList<element> {
} // CustomList<element>

// Invalid: UpperCamelCase without trailing T or Type (looks like a concrete class)
public class ApiResponse<Data> {
} // ApiResponse<Data>
```

#### How to Fix

- Use conventional single-letter type parameters (`E` for Element, `T` for Type, `K` for Key, `V` for Value).
- If using multi-character names for readability, ensure they end with `T` or `Type` (e.g., `ElementT` or `ElementType`).

#### Rationale & Instructor Notes

**Rationale:**
Single uppercase letters or `T`/`Type`-suffixed names prevent generic type parameters from being visually confused with concrete class names (like `String` or `Data`).

**Instructor Note:**
When implementing custom collections such as `LinkedList<E>` or `BinarySearchTree<T>`), use `E` for collections of elements and `T` for generic types.
