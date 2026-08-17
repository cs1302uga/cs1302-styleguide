### EmptyCatchBlock

Empty `catch` blocks are not allowed.

```java
try {
    ...
} catch (IOException ioe) {
    // empty; invalid style
}
```

**Rationale:** The purpose of a `catch` block is to handle an exception.
If it is not appropriate for you to handle the exception in a method
directly, then explore the possibility of propagating the exception up
using `throws` in the method signature.

**Note:** Depending on the parsing behavior of the `checkstyle` program,
an empty `catch` block may trigger the `EmptyBlock` policy instead.
