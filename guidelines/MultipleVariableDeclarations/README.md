### MultipleVariableDeclarations

Each variable declaration must be declared in its own statement on a separate line. Declaring multiple variables in a single statement using commas is disallowed.

```java
int count = 0; // valid style
int total = 0; // valid style
```

```java
int count, total; // invalid style; multiple variables in single declaration
```

**Rationale:**
Declaring one variable per line ensures every variable can be independently documented, easily modified, and read without ambiguity.
