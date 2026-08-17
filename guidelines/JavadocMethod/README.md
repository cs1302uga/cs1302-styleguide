### JavadocMethod

All methods, except the `main` method, must have **full** Javadoc documentation,
including documentation of parameters, exceptions, and the return value.
For example:

```java
/**
 * Returns {@code true} if this list contains the specified string. More formally, returns
 * {@code true} if, and only if, this list contains at least one element {@code s} such that
 * {@code o.equals(s)}.
 *
 * @param o string whose presence in this list is to be tested
 * @return true if this list contains the specified string
 * @throws NullPointerException if the specified string is {@code null}
 * @throws IllegalArgumentException if the specified string is empty
 */
public boolean contains(String o);
```
