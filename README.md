**UNDER CONSTRUCTION; IN PROGRESS**
<hr/>

# CS1302 Code Style Guide

1. [Guidelines](#guidelines)
   1. ArrayTypeStyle
   1. EmptyCatchBlock
   1. EmptyLineSeparator
   1. FileTabCharacter
   1. LeftCurly
   1. LineLength
   1. ModifierOrder
   1. NeedBraces
   1. OneStatementPerLine
   1. OneTopLevelClass
   1. OuterTypeFilename
   1. RightCurly
   1. WhitespaceAround
1. [Recommended Emacs Configuration](#recommended-emacs-configuration)
1. [How to Check](#how-to-check)
   1. [Setup Checkstyle](#setup-checkstyle)
   1. [Run Checkstyle](#run-checkstyle)

## Guidelines

### ArrayTypeStyle

You should use the Java style for array type declarations and not the C style. 

```java
public static void main(String[] args) { // Java style; valid style
```

```java
public static void main(String args[]) { // C style; invalid style
```

### EmptyCatchBlock

Empty `catch` blocks are not allowed. 

**Rationale:** The purpose of a `catch` block is to handle an exception.
If it is not appropriate for you to handle the exception in a method
directly, then explore the posibility of propagating the exception up
using `throws` in the method signature.

### EmptyLineSeparator

You should ensure that empty line separators after header, package, all 
import declarations, fields, constructors, methods, nested classes, 
static initializers and instance initializers. An exception to this
policy is made to allow no empty lines between fields (e.g., between
instance variables in a class).

### FileTabCharacter

No tab characters (`\t`) are allowed in the whitespace of the source code.
This does not include tabs in string literals. For example, the following
snippet is okay:

```java
String s = "word1\tword2";
```

**Rationale:** 
Use of tabs instead of spaces may result in different text editors displaying
same file in different ways, depending on the tab width configured for the
given editor. Developers should not need to configure the tab width of their 
text editors in order to be able to read source code.

### LeftCurly

Left curly braces (`{`) for code blocks must always be on the end of the line. 
For example:

```java
if (condition) {
    ...
```        

### LineLength

You should limit the number of characters, including whitespace, on any given 
line to 100 characters. Except as noted below, any line that would exceed this 
limit must be manually line-wrapped in a consistent manner. Exceptions to the 
column limit include:
* lines where obeying the column limit is not possible (for example, a long URL
  in Javadoc, or a long JSNI method reference);
* package and import statements; and
* command line input examples in a comment that may be cut-and-pasted into a shell.

**Rationale:** Long lines are hard to read in printouts or if developers have 
limited screen space for the source code, e.g. if the editor displays additional 
information like line numbers, multiple files, project tree, class hierarchy, etc.

### ModifierOrder

When using modifier keywords, you should ensure that their order conforms to 
the suggestions in the Java Language specification, sections 
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

### NeedBraces

Braces are always used where technically optional. Braces should be used with 
`if`, `else`, `for`, `do`, and `while` statements, even when the body is empty 
or contains only a single statement.

### OneStatementPerLine

In general, you only have one statement per line. The policy specifically checks 
the following types of statements: variable declaration statements, empty statements, 
import statements, assignment statements, expression statements, increment statements, 
object creation statements, for loop statements, break statements, 
continue statements, and return statements.

**Rationale:**
It's very difficult to read multiple statements on one line.
In the Java programming language, statements are the fundamental unit of execution. 
All statements except blocks are terminated by a semicolon. 
Blocks are denoted by open and close curly braces.

### OneTopLevelClass

Each top-level class, interface or enum resides in a source file of its own. 
Official description of a 'top-level' term: 
[7.6. Top Level Type Declarations](https://docs.oracle.com/javase/specs/jls/se8/html/jls-7.html#jls-7.6). 
If the file does not contain a `public` class, enum or interface, then the top-level
type is the first type in file.

### OuterTypeFilename

In any given `.java` file, the outer type name and the file name must match. 
For example, the class `Foo` must be in a file named `Foo.java`.

**Rationale:** Although this is only technically required by the Java Language
Specification when the outer type is declared with `public` visibility, we
stick to this convention for other visibilities as well. In any case, most of
the time your outer type will be declared as `public`. 

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

### WhitespaceAround

You need to ensure that code tokens are surrounded by whitespace. Empty constructor, 
method, class, enum, interface, loop bodies (blocks), lambdas of the forms
presented below are exempt:

```java
public MyClass() {}      // empty constructor
public void func() {}    // empty method
public interface Foo {} // empty interface
public class Foo {} // empty class
public enum Foo {} // empty enum
MyClass c = new MyClass() {}; // empty anonymous class
while (i == 1) {} // empty while loop
for (int i = 1; i > 1; i++) {} // empty for loop
do {} while (i == 1); // empty do-while loop
Runnable noop = () -> {}; // empty lambda
public @interface Beta {} // empty annotation type
```

## Recommended Emacs Configuration

## How to Check

### Setup Checkstyle

1. **Add `/usr/local/checkstyle` to your `PATH`.** You can do this by adding the 
   following to your `~/.bash_profile`, then logging out and back in:

   ```
   # setup checkstyle
   export PATH=/usr/local/checkstyle:$PATH
   ```

### Run Checkstyle

<hr/>

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-nd/4.0/)

<small>
Copyright &copy; Michael E. Cotterell, Brad Barnes, and the University of Georgia.
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a> to students and the public.
The content and opinions expressed on this Web page do not necessarily reflect the views of nor are they endorsed by the University of Georgia or the University System of Georgia.
</small>
