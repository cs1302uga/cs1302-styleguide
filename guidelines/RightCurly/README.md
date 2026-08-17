### RightCurly

Right curly braces (`}`) for single-part blocks must be on their own line.
Right curly braces for multi-part blocks must be on the same line as the
next part of a multi-block statement. For example:

```java
if (a > 0) {
    ...
} // this is okay
```

```java
if (a > 0) {
    ...
} else { // this is okay
    ...
```

```java
if (a > 0) {
    ...
} // this is not okay
else {
    ...
```

**Rationale:**
This convention for curly braces is pervasive among Java programmers and
is even the same convention used by companies like Google.
