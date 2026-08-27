### PackageName

Package names must be written exclusively in lowercase ASCII letters and digits, with subpackages separated by a single period (`.`). Each package segment must begin with a lowercase letter and cannot start with a digit. Package names must not contain uppercase letters, underscores, or hyphens.

#### Valid Examples

```java
// Valid: All-lowercase dot-separated package declarations
package cs1302;
package cs1302.utility;
package cs1302.game;
package edu.uga.cs1302.collections;
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase letter in package segment
package cs1302.MyExample;
```

```java
// Invalid: Underscore in package segment
package cs1302_example;
```

```java
// Invalid: Hyphen in package segment
package cs1302-game;
```

#### How to Fix

- Convert all package identifier segments to lowercase letters.
- Ensure the directory hierarchy in your `src/` folder mirrors the exact package name in all-lowercase (e.g., `src/cs1302/utility/MathOps.java`).

#### Rationale & Instructor Notes

**Rationale:**
Lowercase package names prevent naming collisions with type names and ensure portability across different filesystems (e.g., case-sensitive Linux filesystems vs. case-insensitive macOS/Windows filesystems).

**Instructor Note:**
In CSCI 1302 projects, standard packages usually follow `cs1302.<projectname>` (e.g., `cs1302.gallery` or `cs1302.list`). Always use all-lowercase folder and package names.
