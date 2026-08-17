### PatternVariableName

Pattern variable names introduced in `instanceof` pattern matching or switch pattern matching must be written in `lowerCamelCase`.

```java
if (obj instanceof String stringVal) { // valid style
    System.out.println(stringVal.length());
} // if
```

```java
if (obj instanceof String StringVal) { // invalid style; uppercase start
    ...
} // if

if (obj instanceof String string_val) { // invalid style; underscore
    ...
} // if
```

**Rationale:**
Pattern variables act as local variables in their scoped blocks and should follow the universal Java `lowerCamelCase` naming convention.
