### MissingJavadocMethod

All methods and constructors, except the `main` method, must have Javadoc documentation.

If a method is annotated with `@Override`, then it is assumed to have Javadoc documentation inherited from the method it is overriding. If an overriding method is not annotated with `@Override`, you must explicitly provide full Javadoc documentation to remain compliant.

#### Valid Examples

```java
/**
 * Calculates the total cost of all items in the shopping cart.
 *
 * @param taxRate the applicable decimal tax percentage
 * @return the total price including taxes
 */
public double calculateTotal(double taxRate) {
    // calculation logic
    return 0.0;
} // calculateTotal

/** {@inheritDoc} */
@Override
public String toString() {
    return "ShoppingCart instance";
} // toString

/**
 * Main entry point for testing. Javadoc is optional on the main method.
 *
 * @param args command-line arguments
 */
public static void main(String[] args) {
    System.out.println("Executing driver...");
} // main
```

When overriding a method from an external library or interface where source code is unavailable to the Javadoc tool, use:

```java
/**
 * Summary sentence.
 *
 * <p>
 * {@inheritDoc}
 */
@Override
public String toString() {
    return "StudentRecord";
} // toString
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Missing Javadoc documentation on helper method
private void initializeDatabase() {
    // database initialization
} // initializeDatabase
```

```java
// Invalid: Missing @Override annotation and missing Javadoc comment
public boolean equals(Object other) {
    return this == other;
} // equals
```

#### How to Fix

- Add a complete Javadoc block (`/** ... */`) above each method and constructor definition.
- Always annotate overridden methods with `@Override`. If you add a Javadoc comment to an overridden method, include `{@inheritDoc}`.
- Remember that `private` and `protected` helper methods also require Javadoc documentation in this style guide.

#### Rationale & Instructor Notes

**Rationale:**
Providing sufficiently detailed documentation makes code maintenance and bug identification much easier. It is critical for code that other developers will use without seeing the internal implementation.

**Instructor Note:**
Well-documented code is just as important as correctly working code. In fact, writing Javadoc *before* writing the method body is a proven technique known as **Test-Driven Development (TDD)**, used to clarify your algorithmic requirements before implementation.
