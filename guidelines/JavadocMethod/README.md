### JavadocMethod

All methods, except the `main` method, must have **full** Javadoc documentation. This requires documenting every formal parameter with `@param`, the return value with `@return` (unless the return type is `void` or a constructor), and any declared checked or unchecked exceptions with `@throws`.

#### Valid Examples

```java
/**
 * Evaluates whether this list contains the specified element.
 *
 * @param target the object whose presence in this list is to be tested
 * @return {@code true} if this list contains the specified element; {@code false} otherwise
 * @throws NullPointerException if the specified element is {@code null} and this list
 *     does not permit null elements
 */
public boolean contains(String target) {
    // implementation details
    return false;
} // contains

/**
 * Main entry point for the test driver application. Javadoc on main is optional.
 *
 * @param args command-line arguments passed to the program
 */
public static void main(String[] args) {
    System.out.println("Driver running...");
} // main
```

#### Common Pitfalls & Invalid Examples

```java
/**
 * Computes the total course score.
 *                                          // Invalid: Missing @param tag for 'examScore'
 * @param labScore student score on laboratory assignments
 * @return the weighted total score
 */
public double calculateTotal(double labScore, double examScore) {
    return labScore + examScore;
} // calculateTotal
```

```java
/**
 * Finds a user by ID.
 *
 * @param id the user numeric identifier    // Invalid: Missing @return tag for non-void method
 */
public User getUser(int id) {
    return null;
} // getUser
```

#### How to Fix

- Ensure every parameter listed in the method signature has a corresponding `@param <paramName>` tag with an accurate description.
- For every non-`void` method, add a `@return` tag describing what value is produced and what special values (such as `null` or `-1`) signify.
- Ensure that if you document `@throws`, the exception type is specified and accompanied by a description of the condition that triggers it.

#### Rationale & Instructor Notes

**Rationale:**
Methods define the functional contract of an object. Comprehensive method documentation allows other programmers to use your methods correctly and safely without needing to inspect internal implementation code.

**Instructor Note:**
In CS2 projects, graders and automated test harnesses verify your Javadoc tags. If you rename a parameter in your method header, make sure you update the corresponding `@param` tag name in the Javadoc comment to match.
