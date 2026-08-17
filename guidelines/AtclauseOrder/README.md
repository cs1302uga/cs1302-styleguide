### AtclauseOrder

When multiple Javadoc block tags (`@...`) are present on a class, interface, enum, method, constructor, or field, they must appear in the following standard order:

1. `@param`
2. `@return`
3. `@throws`
4. `@see`
5. `@since`
6. `@serial` (or `@serialField`, `@serialData`)
7. `@deprecated`

```java
/**
 * Computes the result.
 *
 * @param input the input value
 * @return the computed result
 * @throws IllegalArgumentException if input is negative
 * @see #otherMethod()
 */
public int compute(int input) {
    ...
} // compute
```

```java
/**
 * @return the computed result  // Invalid style: @return before @param
 * @param input the input value
 */
```

**Rationale:**
Following a universal ordering convention allows readers to quickly scan documentation comments for parameters, return values, exceptions, and references in an intuitive sequence.
