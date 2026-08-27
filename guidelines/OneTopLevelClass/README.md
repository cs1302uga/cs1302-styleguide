### OneTopLevelClass

Each top-level class, interface, record, or enum must reside in its own dedicated `.java` source file. Having multiple top-level type declarations within a single source file is prohibited.

#### Valid Examples

File: `StudentRecord.java`:

```java
// Valid: Single top-level record definition in StudentRecord.java
public record StudentRecord(String name, int id) {
} // StudentRecord
```

File: `GradeCalculator.java`:

```java
// Valid: Single top-level class definition in GradeCalculator.java
public class GradeCalculator {
    // class members
} // GradeCalculator
```

#### Common Pitfalls & Invalid Examples

File: `DataStructures.java`

```java
// Invalid: Multiple top-level classes in a single source file
public class DataStructures {
    ...
} // DataStructures

class HelperNode { // Invalid: Second top-level class in the same file
    ...
} // HelperNode
```

#### How to Fix

- Move each top-level class, record, interface, or enum into its own separate `.java` file whose name matches the type name.
- If a helper class is only used internally by one class, consider making it a `private static` nested class inside the enclosing class.

#### Rationale & Instructor Notes

**Rationale:**
Placing one top-level type per file aligns with Java compiler lookup rules, ensures that class files are easily discoverable in the filesystem, and prevents compilation issues when building with build tools.

**Instructor Note:**
Never declare two non-nested classes in one `.java` file. Create a separate `.java` file for every top-level class.
