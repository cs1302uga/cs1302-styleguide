### MissingJavadocMethod

All methods, except the `main` method, must have Javadoc documentation.

If a method is annotated with `@Override`, then it is assumed to have
Javadoc documentation inherited from the method it's overriding.
If a method overrides a method without using the `@Override` annotation,
then you are required to explicitly provide a Javadoc comment for that
method to stay compliant with this style guide.

If you want to explicitly write a Javadoc comment for an override that
inherits its documentation from the method it is overriding, then use
the following comment:

```java
/** {@inheritDoc} */
```

If the Javadoc tool does not have access to the source code for the class or interface, then
it is suggested that you use the following comment, replacing the sentence with something appropriate,
in order to avoid a blank description in the generated documentation website:

```java
/**
 * Summary sentence.
 *
 * <p>
 * {@inheritDoc}
 */
 ```

You can even add more text after the `{@inheritDoc}` if you want to provide more details
in addition to what is inherited:

```java
/**
 * Summary sentence.
 *
 * <p>
 * {@inheritDoc}
 *
 * <p>
 * A sentence or two concerning how this method behaves in a
 * particular way due to the underlying implementation.
 */
```

**NOTE:** The `<p>` tags in the Javadoc comments above just start new paragraphs in the website output.

**Rationale:**
Providing sufficiently detailed documentation helps make code maintenance and bug
identification much easier. Additionally, it's critical for code that others will
use but not necessarily see the actual implementation (e.g., when you use a `String`
method).

**Instructor Note:**
Well-documented code is just as important as correctly working code.
