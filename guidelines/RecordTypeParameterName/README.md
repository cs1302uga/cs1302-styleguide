### RecordTypeParameterName

Generic type parameter names for generic records must conform to one of two formats:

1. A single uppercase letter optionally followed by a single digit (e.g., `T`, `E`, `K`, `V`, `T1`); or
2. An `UpperCamelCase` name ending with `T` or `Type` (e.g., `ItemT`, `KeyType`, `ValueType`).

#### Valid Examples

```java
// Valid: Single uppercase generic type parameters
public record Pair<K, V>(K key, V value) {
    ...
} // Pair

// Valid: Descriptive names ending with T or Type
public record ResultHolder<DataT, ErrorType>(DataT data, ErrorType error) {
    ...
} // ResultHolder
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Lowercase type parameter names
public record Pair<key, value>(key k, value v) { }

// Invalid: Multi-character names without trailing T or Type
public record Entry<Key, Value>(Key k, Value v) { }
```

#### How to Fix

- Rename generic parameters declared on the record header to single uppercase letters (e.g., `<K, V>`) or suffix multi-character names with `T` or `Type` (e.g., `<KeyType, ValueType>`).

#### Rationale & Instructor Notes

**Rationale:**
Generic records serve as lightweight data carriers. Adhering to the type parameter naming convention keeps record headers clean and prevents type parameters from shadowing or resembling concrete classes.

**Instructor Note:**
When creating generic records (like key-value pairs or tuples), use `<K, V>` or `<T, U>`.
