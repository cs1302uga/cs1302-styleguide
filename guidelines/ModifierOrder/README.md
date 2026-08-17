### ModifierOrder

When using modifier keywords, you should ensure that their order conforms to
the suggestions in the Java Language Specification, sections
[8.1.1, 8.3.1, 8.4.4](https://docs.oracle.com/javase/specs/jls/se8/html/jls-8.html), and
[9.4](https://docs.oracle.com/javase/specs/jls/se8/html/jls-9.html).

The correct order is:

```
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

**Rationale:**
This ordering convention for modifiers is pervasive among Java programmers and
is even the same convention used by Oracle and Google.
