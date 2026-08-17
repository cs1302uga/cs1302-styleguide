### InterfaceTypeParameterName

Generic type parameter names for generic interfaces must either be:

1. a single uppercase letter optionally followed by a single digit (e.g., `T`, `E`, `K`, `V`, `T1`); or

2. an `UpperCamelCase` name ending with `T` or `Type` (e.g., `ElementT`, `ItemType`).

```java
public interface Map<K, V> {     // valid style
    ...
} // Map

public interface Container<ItemType> { // valid style
    ...
} // Container
```

```java
public interface Map<key, val> { // invalid style; lowercase
    ...
} // Map
```

**Rationale:**
Standardized interface type parameter names ensure consistency across interface contracts and implementations.
