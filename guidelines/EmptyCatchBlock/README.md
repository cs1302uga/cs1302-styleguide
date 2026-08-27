### EmptyCatchBlock

Empty `catch` blocks are strictly disallowed. When catching an exception, you must either handle the exception, log or print an error message, rethrow a custom or wrapped exception, or document why the exception is intentionally ignored.

#### Valid Examples

```java
// Valid: Handling the exception with recovery or logging
try {
    double value = Double.parseDouble(input);
    process(value);
} catch (NumberFormatException nfe) {
    System.err.println("Invalid numeric input format: " + nfe.getMessage());
} // try

// Valid: Intentionally ignored exception with explanatory comment
try {
    Thread.sleep(100);
} catch (InterruptedException ie) {
    // Interruption is expected during normal shutdown; restore interrupt flag
    Thread.currentThread().interrupt();
} // try
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Silently swallowing an exception without handling or explanation
try {
    FileReader reader = new FileReader("config.txt");
    reader.read();
} catch (IOException ioe) {
    // empty catch block
} // try
```

#### How to Fix

- Handle the error appropriately (e.g., alert the user, provide a fallback value, or clean up resources).
- If your method cannot recover from the exception, propagate it by adding `throws <ExceptionType>` to the method signature instead of catching it.
- If ignoring the exception is genuinely intentional, add an explicit explanatory comment inside the catch block explaining why.

#### Rationale & Instructor Notes

**Rationale:**
Silently swallowing exceptions ("exception swallowing") is one of the most dangerous anti-patterns in software development. It hides system failures, corrupts program state, and makes debugging almost impossible because failures fail silently.

**Instructor Note:**
In CS2 labs and projects, never leave a catch block empty. At minimum, print an error or propagate the exception using `throws`.
