### ConstantName

Constant names must use `CONSTANT_CASE`: all uppercase letters with words separated by a single underscore (`_`).

A **constant** in Java is defined as a field that is declared both `static` and `final`, or a field declared in an interface or annotation interface (which are implicitly `public static final`), excluding standard JVM serialization identifiers (`serialVersionUID` and `serialPersistentFields`).

#### Valid Examples

```java
public class MathUtils {

    // Valid: static final fields in CONSTANT_CASE
    public static final double PI = 3.141592653589793;
    public static final int MAX_BUFFER_SIZE = 1024;
    public static final String DEFAULT_ENCODING = "UTF-8";

} // MathUtils

public interface DatabaseConfig {

    // Valid: Interface fields are implicitly public static final
    String DEFAULT_HOST = "localhost";
    int DEFAULT_PORT = 5432;

} // DatabaseConfig

public interface DatabaseConfig {

    // Valid: Interface fields are implicitly public static final
    public static final String DEFAULT_HOST = "localhost";
    public static final int DEFAULT_PORT = 5432;

} // DatabaseConfig
```

#### Common Pitfalls & Invalid Examples

```java
public class MathUtils {

    // Invalid: lowerCamelCase used on static final constant
    public static final int maxBufferSize = 1024;

    // Invalid: Missing underscores between words
    public static final String DEFAULTENCODING = "UTF-8";

} // MathUtils
```

#### How to Fix

- Convert all letters in `static final` constant names to uppercase, separating words with underscores (`_`).
- Remember that fields that are `final` but **not** `static` (instance constants) are not considered class constants under this rule; they must be written in `lowerCamelCase` as specified in [`MemberName`](#membername).

#### Rationale & Instructor Notes

**Rationale:**
`CONSTANT_CASE` gives immediate visual cues to anyone reading your code that a value is immutable and shared across all instances of the class.

**Instructor Note:**
If a variable is only `final` (e.g., `private final int studentId;`), it is an instance field that varies per object instance and must be named in `lowerCamelCase`. Only add `CONSTANT_CASE` when the variable is both `static` and `final`.
