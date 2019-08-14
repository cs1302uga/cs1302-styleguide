**UNDER CONSTRUCTION; IN PROGRESS**
<hr/>

# CS1302 Code Style Guide

1. [Guidelines](#guidelines)
   1. EmptyCatchBlock
   1. FileTabCharacter
   1. LineLength
   1. NeedBraces
   1. OneTopLevelClass
   1. OuterTypeFilename
1. [Recommended Emacs Configuration](#recommended-emacs-configuration)
1. [How to Check](#how-to-check)
   1. [Setup Checkstyle](#setup-checkstyle)
   1. [Run Checkstyle](#run-checkstyle)

## Guidelines

### EmptyCatchBlock

Empty `catch` blocks are not allowed. 

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

### NeedBraces

Braces are always used where technically optional. Braces should be used with 
`if`, `else`, `for`, `do`, and `while` statements, even when the body is empty 
or contains only a single statement.

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

## Recommended Emacs Configuration

## How to Check

### Setup Checkstyle

### Run Checkstyle

<hr/>

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-nd/4.0/)

<small>
Copyright &copy; Michael E. Cotterell, Brad Barnes, and the University of Georgia.
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a> to students and the public.
The content and opinions expressed on this Web page do not necessarily reflect the views of nor are they endorsed by the University of Georgia or the University System of Georgia.
</small>
