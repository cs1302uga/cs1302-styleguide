### MethodParamPad

There must be no whitespace between a method, constructor, or annotation identifier and its opening parenthesis (`(`).

```java
public void calculateTotal(int count) { // valid style
    doSomething();                      // valid style
} // calculateTotal
```

```java
public void calculateTotal (int count) { // invalid style; space before (
    doSomething ();                      // invalid style; space before (
} // calculateTotal
```

**Rationale:**
Placing the opening parenthesis directly adjacent to the method or constructor name clearly identifies the token as a callable invocation or declaration.
