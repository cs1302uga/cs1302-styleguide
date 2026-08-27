### ArrayTypeStyle

Array brackets (`[]`) must be attached to the **type** identifier (Java style), never to the variable name (C style).

#### Valid Examples

```java
// Valid: Java style - brackets attached to type
String[] names = new String[10];
int[] scores = new int[] {1, 2, 3};

public static void main(String[] args) {
} // main

public int[] getScores() {
    return this.scores;
} // getScores
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: C style - brackets attached to variable name
String names[] = new String[10];
int scores[] = new int[] {1, 2, 3};

public static void main(String args[]) {
    ...
} // main
```

#### How to Fix

- Move square brackets `[]` from after the variable name to directly after the element type name (e.g. `String[] args`, not `String args[]`).

#### Rationale & Instructor Notes

**Rationale:**
In Java, an array is a distinct reference type. Attaching the brackets to the type name (`int[]`) clearly specifies what *type* the variable holds, consistent with how all other reference type variables are declared.

**Instructor Note:**
C-style array syntax exists in Java solely for backward compatibility with C/C++. Always write `String[] args` in modern Java.
