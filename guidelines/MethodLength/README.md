### MethodLength

The bodies of methods and constructors should never exceed 60 lines.
This includes the line(s) with the method's signature and opening curly brace,
all lines in the body of the method (including blank lines), and the line with the
method's ending curly brace. The method length does not include a method's Javadoc
comment; however, it does include any comments and blank lines contained within the
body of the method.

**Rationale:**
If a method becomes very long, it is hard to understand. Here is the spirit of this
guideline: methods that are too big and/or repetitive should be refactored to include
proper looping constructs and/or broken up into smaller methods to improve readability.

**Instructor Note:**
You should always try to limit the number of lines for a method so that the
entire method can be seen on the screen at once, even when multiple files
are open at the same time on a single screen.
