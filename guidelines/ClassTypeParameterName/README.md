### ClassTypeParameterName

Generic type parameter names for generic classes must either be:

1. a single uppercase letter optionally followed by a single digit (e.g., `T`, `E`, `K`, `V`, `T1`); or

2. an `UpperCamelCase` name ending with `T` or `Type` (e.g., `RequestT`, `ResponseT`, `ValueType`).

```java
public class MyList<E> {         // valid style
    ...
} // MyList<E>

public class Response<DataT> {   // valid style
    ...
} // Response<DataT>
```

```java
public class MyList<element> {   // invalid style; lowercase
    ...
} // MyList<element>

public class Response<Data> {    // invalid style; does not end with T or Type
    ...
} // Response<Data>
```

**Rationale:**
Clear, concise naming conventions for type parameters avoid confusion with concrete class names.
