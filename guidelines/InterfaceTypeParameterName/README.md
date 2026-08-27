### InterfaceTypeParameterName

Generic type parameter names for generic interfaces must conform to one of two formats:

1. A single uppercase letter optionally followed by a single digit (e.g., `T`, `E`, `K`, `V`, `T1`); or
2. An `UpperCamelCase` name ending with `T` or `Type` (e.g., `ElementT`, `KeyType`, `ValueType`).

#### Valid Examples

```java
// Valid: Single uppercase letters
public interface Map<K, V> {
    V get(K key);
} // Map<K, V>

// Valid: Descriptive names ending with T or Type
public interface Transformer<InputT, OutputT> {
    OutputT transform(InputT input);
} // Transformer<InputT, OutputT>
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Lowercase type parameter names
public interface Map<key, val> {
} // Map<key, val>

// Invalid: Multi-character name without T/Type suffix
public interface Transformer<Source, Target> {
} // Transformer<Source, Target>
```

#### How to Fix

- Change interface generic parameters to single uppercase letters (`K`, `V`, `T`, `E`) or add the `T` or `Type` suffix (e.g., `SourceT`, `TargetType`).

#### Rationale & Instructor Notes

**Rationale:**
Standardized interface type parameter names ensure consistency between interface contracts and the classes that implement them.

**Instructor Note:**
Using standard type parameter names makes generic interface contracts intuitive and clear, regardless of the interface. These standard names include single uppercase letters (i.e., `T`, `E`, `K`, `V`) or `UpperCamelCase` names ending with `T` or `Type`.
