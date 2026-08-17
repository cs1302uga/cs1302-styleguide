### WhitespaceAround

You need to ensure that code tokens are surrounded by whitespace.

```java
if (n==0) { // invalid
    ...
} // if
```

```java
if (n == 0) { // valid
    ...
} // if
```

```java
while(n == 0) { // invalid
    ...
} // while
```

```java
while (n == 0) { // valid
    ...
} // while
```

Empty constructor, method, class, enum, interface, and loop bodies (blocks),
as well as lambdas of the forms presented below, are exempt:

```java
public MyClass() {} // empty constructor
public void func() {} // empty method
public interface Foo {} // empty interface
public class Foo {} // empty class
public enum Foo {} // empty enum
MyClass c = new MyClass() {}; // empty anonymous class
while (i == 1) {} // empty while loop
for (int i = 1; i > 1; i++) {} // empty for loop
do {} while (i == 1); // empty do-while loop
Runnable noop = () -> {}; // empty lambda
public @interface Beta {} // empty annotation type
```

**Rationale:**
This convention improves readability.
