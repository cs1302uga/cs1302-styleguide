### SummaryJavadoc

The first sentence of every Javadoc comment is its [summary sentence](https://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#firstsentence). It must be present, grammatically complete, and end with a period (`.`).

The only exception to this rule is when the first tag in the comment is `{@inheritDoc}`.

#### Valid Examples

```java
/**
 * Calculates the Euclidean distance between two coordinate points.
 *
 * @param p1 the starting coordinate point
 * @param p2 the ending coordinate point
 * @return the straight-line distance between {@code p1} and {@code p2}
 */
public double distance(Point p1, Point p2) {
    // calculation logic
    return 0.0;
} // distance

/** {@inheritDoc} */
@Override
public int hashCode() {
    return 42;
} // hashCode
```

#### Common Pitfalls & Invalid Examples

```java
/**
 * Calculates the Euclidean distance between points  // Invalid: Missing ending period
 *
 * @param p1 point one
 * @param p2 point two
 * @return distance
 */
public double distance(Point p1, Point p2) {
    return 0.0;
} // distance
```

```java
/**
 *                                                  // Invalid: Missing summary sentence completely
 * @return the maximum allowed value
 */
public int getMaxValue() {
    return 100;
} // getMaxValue
```

#### How to Fix

- Ensure the very first line of text in your Javadoc comment clearly summarizes the method or class, and end that sentence with a period (`.`).
- Avoid leading blank lines before the summary sentence.

#### Rationale & Instructor Notes

**Rationale:**
The Javadoc tool extracts the first sentence of each comment to populate the summary table at the top of generated API documentation. A missing or unpunctuated first sentence results in malformed or incomplete summary tables.

**Instructor Note:**
In English grammar and standard Javadoc style, summary sentences start with a capital letter and end with a period. In Java API documentation, it is conventional to write summary sentences in third-person declarative form (e.g., "Returns the element..." or "Calculates the total...").
