### JavadocParagraph

Paragraphs in Javadoc comments must be separated by an empty line followed by a `<p>` tag on its own line, immediately preceding the new paragraph text. There should not be a closing `</p>` tag.

```java
/**
 * First paragraph summarizing the method.
 *
 * <p>
 * Second paragraph with additional implementation details.
 */
public void process() {
    ...
} // process
```

```java
/**
 * First paragraph.
 * <p> Second paragraph without blank line preceding tag.
 */
```

**Rationale:**
The standard Javadoc HTML generator expects paragraph separation structured with `<p>` on its own line preceded by a blank Javadoc line for optimal website rendering.
