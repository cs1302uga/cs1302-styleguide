### ParenPad

There must be no whitespace immediately following an opening parenthesis (`(`) or immediately preceding a closing parenthesis (`)`) in method calls, constructor calls, control flow expressions (`if`, `for`, `while`, `switch`), and type casts.

```java
if (x > 0) {                 // valid style
    String str = (String) o; // valid style
    foo(a, b);               // valid style
} // if
```

```java
if ( x > 0 ) {               // invalid style; spaces inside parens
    String str = ( String ) o; // invalid style; spaces inside parens
    foo( a, b );             // invalid style; spaces inside parens
} // if
```

**Rationale:**
Padding inside parentheses adds unnecessary horizontal spacing and impairs readability.
