### EmptyLineSeparator

You should ensure that empty line separators are present after the header,
package, all import declarations, fields, constructors, methods, nested classes,
static initializers, and instance initializers. An exception to this
policy is made to allow no empty lines between fields (e.g., between
instance variables in a class).

```java
import java.util.Scanner; // not separated by
public class MyClass {    // at least one line;
    private int x;        // invalid style
    ...
```

This policy also disallows multiple instance variable declarations on the
same line using the comma operator:

```java
private int n, k; // k declaration not separated from previous statement
```

**Rationale:**
This vastly improves readability.
