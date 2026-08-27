### EmptyLineSeparator

Empty blank lines must separate major structural components in Java source files, including:

* After the `package` statement;
* After `import` declaration groups;
* Between constructors, methods, nested types, static initializers, and instance initializers.

Empty lines are optional between variable field declarations (e.g., consecutive instance variable fields).

#### Valid Examples

```java
package cs1302.example;

import java.util.List;
import java.util.ArrayList;

public class StudentManager {

    private String name;
    private int id;

    public StudentManager(String name, int id) {
        this.name = name;
        this.id = id;
    } // StudentManager

    public String getName() {
        return this.name;
    } // getName

} // StudentManager
```

#### Common Pitfalls & Invalid Examples

```java
package cs1302.example;
import java.util.List;  // Invalid: No blank line between package and imports
public class Student {  // Invalid: No blank line between imports and class
    public void a() {}
    public void b() {}  // Invalid: No blank line between method declarations
}
```

#### How to Fix

* Insert at least one blank line after the package declaration, after your import block, and between consecutive method/constructor declarations.

#### Rationale & Instructor Notes

**Rationale:**
Vertical whitespace separates discrete units of logic, preventing code files from looking like dense walls of text and making visual navigation intuitive.

**Instructor Note:**
Keep one blank line between each method in your class. You do not need blank lines between single-line field declarations.
