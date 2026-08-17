### PackageName

Package names must be written in all lowercase letters, with subpackages separated by a single period (`.`). Package names must not contain uppercase letters, underscores, or other special characters.

```java
package cs1302.example; // valid style
```

```java
package cs1302.MyExample; // invalid style; uppercase letter
package cs1302_example;   // invalid style; underscore
```

**Rationale:**
This naming convention is standard in Java (see the Java Language Specification, section 6.8.1). Lowercase package names avoid name conflicts with type names.
