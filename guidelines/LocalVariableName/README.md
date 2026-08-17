### LocalVariableName

Local variable names (variables declared inside methods, constructors, or code blocks) must be written in `lowerCamelCase`.

```java
int studentCount = 10;   // valid style
String firstName = "Ada"; // valid style
```

```java
int StudentCount = 10;   // invalid style; starts with uppercase letter
String first_name = "Ada"; // invalid style; contains underscore
```

**Rationale:**
This naming convention is pervasive throughout Java programming and provides visual distinction from type names (`UpperCamelCase`) and constants (`CONSTANT_CASE`).
