### OuterTypeFilename

In any `.java` source file, the filename must exactly match the name of the outer top-level class, interface, record, or enum, including matching case.

#### Valid Examples

```java
// In file: src/cs1302/utility/MathOps.java
package cs1302.utility;

public class MathOps {
    ...
} // MathOps
```

#### Common Pitfalls & Invalid Examples

```java
// In file: src/cs1302/utility/mathops.java (all lowercase filename)
package cs1302.utility;

public class MathOps { // Invalid: Filename 'mathops.java' does not match 'MathOps'
    ...
} // MathOps
```

```java
// In file: src/cs1302/utility/Utilities.java
package cs1302.utility;

public class MathOps { // Invalid: Filename 'Utilities.java' does not match 'MathOps'
    ...
} // MathOps
```

#### How to Fix

- Rename the file on disk so that its basename exactly matches the declared public outer type name, respecting case sensitivity (e.g., rename `student.java` to `Student.java`).

#### Rationale & Instructor Notes

**Rationale:**
The Java compiler and classloader locate compiled types by matching fully qualified class names to filesystem directory and file names. Matching filenames prevent compilation failures on case-sensitive operating systems (such as Linux).

**Instructor Note:**
On macOS and Windows, filesystems are often case-insensitive, so `mathops.java` might compile locally, but fail when submitted to Linux-based grading servers (such as Odin). Always match casing exactly!
