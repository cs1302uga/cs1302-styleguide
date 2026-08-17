### StaticVariableName

Static non-final field names (class variables) must be written in `lowerCamelCase`.

```java
public class Counter {

    // valid style
    private static int instanceCount = 0; 

} // Counter
```

```java
public class Counter {

    // invalid style; uppercase start
    private static int InstanceCount = 0;  

    // invalid style; underscore
    private static int instance_count = 0; 

} // Counter
```

**Note:** A `static` **field** that is also `final` is a **constant** and must be written in `CONSTANT_CASE` as described in [`ConstantName`](#constantname).

**Rationale:**
Static non-final fields are **mutable class-level variables** and must be visually distinguished from constants.
