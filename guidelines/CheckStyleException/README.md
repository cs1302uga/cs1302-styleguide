### CheckStyleException

A `CheckstyleException` (specifically `com.puppycrawl.tools.checkstyle.api.CheckstyleException`) is a fatal error thrown by `check1302` or `checkstyle` itself when it cannot parse your Java source code.

Unlike standard Checkstyle style violations (which report formatting or naming warnings), a `CheckstyleException` indicates that the audit tool crashed before completing its analysis.

#### Common Causes

Most `CheckstyleException` crashes occur because the source file **does not compile**. Common causes include:

* Unclosed curly braces `}`, parentheses `)`, or quotes `"`
* Java syntax errors or malformed expressions
* Missing import statements or unresolved type names
* Java version mismatch (e.g., using preview features unsupported by the installed parser)

#### How to Fix

1. **Step 1: Always compile your code first with `javac`**:

   ```bash
   javac -d bin -cp bin src/cs1302/MyClass.java
   ```

2. **Step 2: Fix all compiler syntax errors reported by `javac`**.

3. **Step 3: Re-run `check1302` only after `javac` compiles with 0 errors**:

   ```bash
   check1302 src/cs1302/MyClass.java
   ```

#### Rationale & Instructor Notes

**Rationale:**
Checkstyle builds an Abstract Syntax Tree (AST) to evaluate code style rules. If the source file contains syntax errors that violate the Java grammar, the AST parser cannot construct the tree and throws an exception.

**Instructor Note:**
If you ever see a long Java stack trace when running `check1302`, do not panic! It almost always means your Java code has a compiler syntax error. Run `javac` to see the compiler error message.
