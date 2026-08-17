### RecordTypeParameterName

Generic type parameter names for generic records must either be:

1. a single uppercase letter optionally followed by a single digit (e.g., `T`, `E`, `K`, `V`, `T1`); or

2. an `UpperCamelCase` name ending with `T` or `Type` (e.g., `ItemT`, `KeyType`, `ValueType`).

```java
// valid style
public record Pair<K, V>(K key, V value) { 
    ...
} // Pair

// valid style
public record Entry<KeyType, ValueType>(KeyType key, ValueType val) { 
    ...
} // Entry
```

```java
// invalid style; lowercase
public record Pair<key, value>(key k, value v) { 
    ...
} // Pair

// invalid style; does not end with T or Type
public record Entry<Key, Value>(Key k, Value v) { 
    ...
} // Entry
```

**Rationale:**
Record type parameters serve a role similar to type parameters in generic classes and interfaces, and should follow the same established conventions. Using single uppercase letters or `T`-suffixed names ensures they remain visually distinct from concrete record names and component field names.
