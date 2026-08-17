### MethodTypeParameterName

Generic type parameter names for generic methods must either be:

1. a single uppercase letter optionally followed by a single digit (e.g., `T`, `R`, `E`, `T1`); or

2. an `UpperCamelCase` name ending with `T` or `Type` (e.g., `ResultT`, `ReturnType`).

```java
public <T> T getFirst(List<T> list) { // valid style
    return list.get(0);
} // getFirst

public <ReturnType> ReturnType process(Task<ReturnType> task) { // valid style
    return task.execute();
} // process
```

```java
public <type> type getFirst(List<type> list) { // invalid style; lowercase
    return list.get(0);
} // getFirst
```

**Rationale:**
Conforming to standard single-letter or `T`-suffixed type parameter conventions ensures generic method signatures remain intuitive and readable.
