### StaticVariableName

Static non-final field names (i.e., the names of static variables that are not final) must be written in `lowerCamelCase`.

#### Valid Examples

```java
public class Counter {

    // Valid: static mutable variables in lowerCamelCase
    private static int instanceCount = 0;
    private static String globalEnvironment = "production";

} // Counter
```

#### Common Pitfalls & Invalid Examples

```java
public class Counter {

    // Invalid: CONSTANT_CASE on non-final static variable
    private static int INSTANCE_COUNT = 0;

    // Invalid: Snake_case with underscores
    private static int instance_count = 0;

    // Invalid: UpperCamelCase
    private static int InstanceCount = 0;

} // Counter
```

#### How to Fix

- If a static variable is intended to be mutable and shared across instances, name it in `lowerCamelCase`.
- If a static variable was intended to be an immutable constant, add the `final` modifier and use `CONSTANT_CASE` as required by [`ConstantName`](#constantname).

#### Rationale & Instructor Notes

**Rationale:**
Static non-final fields represent mutable class state. Naming them in `lowerCamelCase` prevents them from being mistaken for compile-time constants.

**Instructor Note:**
Mutable static variables should be used sparingly. When they are used (such as for object ID generators or instance counters), ensure they follow `lowerCamelCase`.
