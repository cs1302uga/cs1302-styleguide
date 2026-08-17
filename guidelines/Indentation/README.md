### Indentation

The following indentation rules must be followed:

| Property                  | Description                                                                 | Spaces |
|---------------------------|-----------------------------------------------------------------------------|--------|
| `basicOffset`             | how far the new indentation level should be indented when on the next line      | 4      |
| `braceAdjustment`         | how far a brace should be indented when on the next line 	                | 0      |
| `caseIndent`              | how far a case label should be indented when on the next line 	                | 0      |
| `throwsIndent` 	          | how far a throws clause should be indented when on the next line                | 4      |
| `arrayInitIndent`         | how far an array initializer list item should be indented when on the next line | 4      |
| `lineWrappingIndentation` | how far the continuation line should be indented when line-wrapping is present  | 4      |

Sometimes, indentation rules are a little hard to parse when parentheses and
curly braces are involved, as is sometimes the case with multi-line inline lambda
expressions. An inline lambda expression is a lambda expression that is used as
a parameter to a method. Here is an example:

```java
// BAD INDENTATION
Arrays.sort(array, (a, b) -> {
        return a.compareTo(b);  // 'block' child has incorrect indentation
    });                         // 'block rcurly' has incorrect indentation
```

```java
// GOOD INDENTATION
Arrays.sort(array, (a, b) -> {
    return a.compareTo(b);
});
```

If these rules make one of your inline lambda expressions look less readable,
then you are encouraged to refactor your lambda expression, if possible, to
avoid indentation. Here is the same inline lambda written using one line of
code:

```java
// HOWEVER, if you can write using one line, then please do so
Arrays.sort(array, (a, b) -> a.compareTo(b));
```
