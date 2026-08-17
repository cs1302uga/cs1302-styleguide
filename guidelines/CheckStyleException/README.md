### CheckStyleException

A `CheckstyleException` (specifically `com.puppycrawl.tools.checkstyle.api.CheckstyleException`)
is an error thrown by `check1302` and `checkstyle` themselves and not by the program being
checked. Unlike standard Checkstyle violations (which just tell you your code is formatted
incorrectly), a `CheckstyleException` means the tool encountered a fatal error and crashed
before it could finish analyzing your code. Because this exception is a generic wrapper,
the actual problem is almost always found further down in the stack trace under the
`Caused by:` line. Most often, this means that the java source code you are trying to
check does not compile.

This exception can happen for a variety of reasons, so the easiest way to
fix it is to compile your code on your own first and fix any compilation errors before
running `check1302` or `checkstyle` again. Common reasons this exception is thrown include:

* Mismatched parentheses, brackets, or braces
* Typos in class or method names
* Missing import statements
* Incompatible Java versions
* Missing or corrupted source files
