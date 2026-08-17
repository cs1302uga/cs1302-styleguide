### ParameterName

Method and constructor formal parameter names must be written in `lowerCamelCase`.

```java
public void setScore(int finalScore, String studentName) { // valid style
    ...
} // setScore
```

```java
public void setScore(int FinalScore, String student_name) { // invalid style
    ...
} // setScore
```

**Rationale:**
Consistent parameter naming ensures seamless readability in method signatures and documentation across the codebase.
