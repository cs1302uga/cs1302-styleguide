### ModifierOrder

When applying multiple modifier keywords to a class, field, constructor, or method, they must appear in the canonical order specified by the Java Language Specification, sections [8.1.1, 8.3.1, 8.4.3](https://docs.oracle.com/javase/specs/jls/se21/html/jls-8.html#jls-8.1.1), and [9.4](https://docs.oracle.com/javase/specs/jls/se21/html/jls-9.html#jls-9.4):

```java
public
protected
private
abstract
default
static
final
transient
volatile
synchronized
native
strictfp
```

#### Valid Examples

```java
// Valid: Correct canonical modifier ordering
public static final int MAX_LIMIT = 100;

public static void main(String[] args) {
} // main

protected abstract void processRecord();

private synchronized void updateState() {
} // updateState
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: 'final' before 'public static'
final public static int MAX_LIMIT = 100;

// Invalid: 'static' before 'public'
static public void main(String[] args) {
} // main

// Invalid: 'synchronized' before 'private'
synchronized private void updateState() {
} // updateState
```

#### How to Fix

- Reorder modifiers so visibility (`public`, `protected`, `private`) comes first, followed by `abstract` / `static`, followed by `final`, followed by concurrency/system modifiers (`synchronized`, `volatile`, etc.).

#### Rationale & Instructor Notes

**Rationale:**
Standard modifier ordering creates visual consistency across classes and libraries, making it easy for readers to quickly ascertain visibility and mutability.

**Instructor Note:**
Always remember: Visibility first (`public static final`), never `final static public`.
