### ArrayTypeStyle

You must use the Java style for array type declarations and not the C style.
The Java style places the square brackets (i.e., the `[]`) to the left of the
variable name, next to the array's element type.

```java
public static void main(String[] args) { // Java style; valid style
```

```java
public static void main(String args[]) { // C style; invalid style
```

```java
String[] someVar; // Java style; valid style
```

```java
String someVar[]; // C style; invalid style
```

**Rationale:**
An array is a type of object in Java. While the C style presented above is
syntactically correct in Java (i.e., it will compile), Oracle advises that,
"convention discourages this form; the brackets identify the array type and
should appear with the type designation." When declaring a variable
that refers to an array object, the Java style results in a declaration that
is consistent with how variables for other, non-array types of objects are
declared.
