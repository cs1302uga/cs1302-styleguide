### MultipleVariableDeclarations

Each variable must be declared in its own separate statement on a distinct line. Declaring multiple variables in a single comma-separated statement is disallowed.

#### Valid Examples

```java
// Valid: Separate declaration statements on distinct lines
int count = 0;
int total = 0;
String studentName = "";
String courseId = "";
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Comma-separated variable declarations
int count = 0, total = 0;
```

```java
// Invalid: Comma-separated uninitialized declarations
double width, height, length;
```

#### How to Fix

- Split comma-separated declarations into separate statements, declaring the type on each line:

  ```java
  double width = 0.0;
  double height = 0.0;
  double length = 0.0;
  ```

#### Rationale & Instructor Notes

**Rationale:**
Declaring one variable per statement allows each variable to be documented independently, makes initial values explicit, and prevents common Java bugs where modifiers or type properties (such as array brackets or pointer-like semantics) are mistakenly assumed to apply to all variables in the list.

**Instructor Note:**
  Declaring one variable per line makes it much easier to track variable lifecycles, add inline comments, and refactor code without disturbing adjacent declarations.
