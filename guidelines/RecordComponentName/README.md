### RecordComponentName

Record component names declared in record headers must be written in `lowerCamelCase`.

```java
public record StudentRecord(String firstName, int studentId) { // valid style
} // StudentRecord
```

```java
public record StudentRecord(String FirstName, int student_id) { // invalid style
} // StudentRecord
```

**Rationale:**
Record components define both private final fields and public accessor methods on the resulting record type. Naming them in `lowerCamelCase` ensures generated accessor methods (e.g. `firstName()`) adhere to standard Java method naming conventions.
