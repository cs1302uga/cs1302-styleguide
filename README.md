# CSCI 1302 Code Style Guide

![Approved for: Fall 2019](https://img.shields.io/badge/Approved%20for-Fall%202019-brightgreen)

This document serves as the complete definition of CSCI 1302's coding standards 
for Java source code. For the purposes of this course, a Java source file is 
described as being in _valid style_ if and only if it adheres to the rules herein.
This document not only contains the specific guidelines that must be followed,
but also includes editor configuration reccomendations as well information
about how to use the `checkstyle` tool to check your code for compliance.

## Table of Contents

1. [Motivation](#motivation)
1. [Specific Guidelines](#specific-guidelines)
   1. [ArrayTypeStyle](#arraytypestyle)
   1. [ConstantName](#constantname)
   1. [EmptyBlock](#emptyblock)
   1. [EmptyCatchBlock](#emptycatchblock)
   1. [EmptyLineSeparator](#emptylineseparator)
   1. [FileTabCharacter](#filetabcharacter)
   1. [Indentation](#indentation)
   1. [JavadocMethod](#javadocmethod)
   1. [LeftCurly](#leftcurly)
   1. [LineLength](#linelength)
   1. [MemberName](#membername)
   1. [MissingJavadocMethod](#missingjavadocmethod)
   1. [MissingJavadocType](#missingjavadoctype)
   1. [ModifierOrder](#modifierorder)
   1. [NeedBraces](#needbraces)
   1. [OneStatementPerLine](#onestatementperline)
   1. [OneTopLevelClass](#onetoplevelclass)
   1. [OuterTypeFilename](#outertypefilename)
   1. [RightCurly](#rightcurly)
   1. [SummaryJavadoc](#summaryjavadoc)
   1. [TypeName](#typename)
   1. [WhitespaceAround](#whitespacearound)
1. [Recommended Emacs Configurations](#recommended-emacs-configurations)
1. [Recommended Vi Configurations](#recommended-vi-configurations)
1. [How to Check](#how-to-check)
   1. [Setup Checkstyle](#setup-checkstyle)
   1. [Run Checkstyle](#run-checkstyle)
      1. [Multiple Files](#multiple-files)
      1. [Setup an Alias](#setup-an-alias)
      1. [Output Examples](#output-examples)

# Motivation

Many companies will not let you commit changes for review until their established
guidelines are met--a notable example is Google. Why do these companies do this?
The short answer is that it makes things easier for everybody. 

If your code looks good, which we'll define here as adhering to an established 
style guide, then:
  
* It's easier to read, especially when compared to code that applies stylistic choices 
  inconsistently. It's certainly easier to read by those who are familiar with the 
  conventions outlined in the style guide.
  
* It's easier to identify common bugs and syntax errors (e.g., missing a curly brace). 
  This saves real world time when it comes to fixing problems in your code.
  
* It's easier to extend and/or incorporate into other projects. This results in your 
  code being more useful to others as well as your future self.
  
The list could go on. The important thing to remember is that quality not only
refers to the output of a program but also its effect on the people who interact
with the code. Rarely, in practice, are you the only one who will read and use your
code. If you're a software engineer, then it's very likely that many others will 
interact your code as well. 

# Specific Guidelines

The name for each of these guidelines corresponds to a `checkstyle` module
configured in [`cs1302_checks.xml`](cs1302_checks.xml) for use  by the
`checkstyle` program. This was done so that it's easier for users to relate 
`checkstyle` program output to the actual guidelines. 

## ArrayTypeStyle

You must use the Java style for array type declarations and not the C style. 
The Java style places the square brackets (i.e., the `[]`) to left of the
variable name, next to the array's element type.

```java
public static void main(String[] args) { // Java style; valid style
```

```java
public static void main(String args[]) { // C style; invalid style
```

```java
String[] someVar; // Java style; valid style
```

```java
String someVar[]; // C style; invalid style
```

**Rationale:** 
While the C style is also syntactically correct in Java, Oracle advises that,
"convention discourages this form; the brackets identify the array type and 
should appear with the type designation."

## ConstantName

Constant names must use `CONSTANT_CASE`: all uppercase letters, with each word separated 
from the next by a single underscore. A _constant_ is a `static` and `final` field or an 
interface/annotation field, except `serialVersionUID` and `serialPersistentFields`.

**Rationale:**
This naming convention for constants is pervasive among Java programmers and is even
the same convention used by Oracle and Google. This specific convention allows most
programmers to easily identify a constant when used in source code.

## EmptyBlock

Empty code blocks are not allowed.

**Rationale:** 
Code blocks are for code. If, for some reason, you believe that you need an empty code
block, then take a step back and rework your control flow.

## EmptyCatchBlock

Empty `catch` blocks are not allowed. 

```java
try {
    ...
} catch (IOException ioe) {
    // empty; invalid style
}
```

**Rationale:** The purpose of a `catch` block is to handle an exception.
If it is not appropriate for you to handle the exception in a method
directly, then explore the posibility of propagating the exception up
using `throws` in the method signature.

## EmptyLineSeparator

You should ensure that empty line separators are present after header, 
package, all import declarations, fields, constructors, methods, nested classes, 
static initializers and instance initializers. An exception to this
policy is made to allow no empty lines between fields (e.g., between
instance variables in a class).

```java
import java.util.Scanner; // not separated by
public class MyClass {    // at least one line;
    private int x;        // invalid style
    ...
```

This policy also disallows multiple instance variable declarations on the
same line using the comma operator:

```java
private int n, k; // k declaration not separated from previous statement
```

**Rationale:**
This vastly improves readability. 

## FileTabCharacter

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

## Indentation

The following indentation rules must be followed:

| Property                  | Description                                                                 | Spaces |
|---------------------------|-----------------------------------------------------------------------------|--------|
| `basicOffset`             | how far new indentation level should be indented when on the next line      | 4      |
| `braceAdjustment`         | how far a braces should be indented when on the next line 	                | 0      |
| `caseIndent`              | how far a case label should be indented when on next line 	                | 0      |
| `throwsIndent` 	          | how far a throws clause should be indented when on next line                | 4      |
| `arrayInitIndent`         | how far an array initializer list item should be indented when on next line | 4      |
| `lineWrappingIndentation` | how far continuation line should be indented when line-wrapping is present  | 4      |

## JavadocMethod

All methods, except the `main` method, must have **full** Javadoc documentation, 
including documentation of parameters, exceptions, and return value.
For example:

```java
/**
 * Returns {@code true} if this list contains the specified string. More formally, returns 
 * {@code true} if, and only if, this list contains at least one element {@code s} such that 
 * {@code o.equals(s)}.
 *
 * @param o string whose presence in this list is to be tested
 * @return true if this list contains the specified string
 * @throws NullPointerException if the specified string is {@code null}
 * @throws IllegalArgumentException if the specified string is empty
 */
public boolean contains(String o);
```

## LeftCurly

Left curly braces (`{`) for code blocks must always be on the end of the line. 
For example:

```java
if (condition) {
    ...
```

**Rationale:**
This convention for curly braces is pervasive among Java programmers and 
is even the same convention used by companies like Google.

## LineLength

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

## MemberName

Instance variable names must be written in `lowerCamelCase`.

**Rationale:**
This naming convention for instance variables is pervasive among Java programmers and 
is even the same convention used by Oracle.

## MethodName

Method names must be written in `lowerCamelCase`.

**Rationale:**
This naming convention for methods is pervasive among Java programmers and 
is even the same convention used by Oracle.

## MethodLength

The bodies of methods and constuctors should never exceed 60 lines.
This includes the line(s) with the method's signature and opening curly brace, 
all lines in the body of the method (including blank lines), and the line with the 
method's ending curly brace. The method length does not include a method's Javadoc 
comment, however, it does include any comments and blank lines contained within the 
body of the method.

**Rationale:**
If a method becomes very long it is hard to understand. Here is the spirit of this 
guideline: methods that are too big and/or repetitive should be refactored to include 
proper looping constructs and/or broken up into smaller methods to improve readability.

**Instructor Note:**
You should always try to limit the number of lines for a method so that the 
entire method can be seen on the screen at once, even when multiple files
are open at the same time on a single screen.

## MissingJavadocMethod

All methods, except the `main` method, must have Javadoc documentation.

**Rationale:**
Providing sufficiently detailed documention helps make code maintenance and bug
identification much easier. Additionally, it's critical for code that others will
use but not necessarily see the actual implementation (e.g., when you use a `String`
method). 

**Instructor Note:**
Well documented code is just as important as correctly working code.

## MissingJavadocType

All class, enum, interface, and annotation interface definitions must have Javadoc
documentation.

**Rationale:**
Just like methods, type documentation is also important. Oftentimes class and interface
documentation provide important high-level details about implementation, naming 
conventions, etc. In some cases, even code examples are provided directly in the
documentation to make things easier for programmers who wish to use the code.

**Instructor Note:**
Well documented code is just as important as correctly working code.

## ModifierOrder

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

**Rationale:**
This ordering convention for methods is pervasive among Java programmers and 
is even the same convention used by Oracle and Google.

## NeedBraces

Curly braces are always used where technically optional. Braces should be used with 
`if`, `else`, `for`, `do`, and `while` statements, even when the body is empty 
or contains only a single statement.

**Rationale:**
Consider `if` statements without curly braces. In Java, only the first statement
following such `if` statements is executed when the conditional's expression
evaluates to `true`. Potential bugs can be avoided by using curly braces to
clearly indicating what statement or statements are to execute when the 
conditional's expression evaluates to `true`.

**Instructor Note:**
One common bug that we've seen over the years is students adding statements
to a brace-less `if` statement with the intent that those statements only
execute when the conditional's expression evaluates to `true`. That is,
they forgot to add the curly braces. This guideline helps protect you
against that scenario and improves readability. 

## OneStatementPerLine

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

## OneTopLevelClass

Each top-level class, interface or enum resides in a source file of its own. 
Official description of a 'top-level' term: 
[7.6. Top Level Type Declarations](https://docs.oracle.com/javase/specs/jls/se8/html/jls-7.html#jls-7.6). 
If the file does not contain a `public` class, enum or interface, then the top-level
type is the first type in file.

## OuterTypeFilename

In any given `.java` file, the outer type name and the file name must match. 
For example, the class `Foo` must be in a file named `Foo.java`.

**Rationale:** Although this is only technically required by the Java Language
Specification when the outer type is declared with `public` visibility, we
stick to this convention for other visibilities as well. In any case, most of
the time your outer type will be declared as `public`. 

## RightCurly

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

**Rationale:**
This convention for curly braces is pervasive among Java programmers and 
is even the same convention used by companies like Google.

## SummaryJavadoc

In Javadoc comments, the
[summary sentence](https://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#firstsentence)
should always be present and correctly punctuated.
The only exception to this rule is when the first statement in the comment
is `{@inheritDoc}`.

**Rationale:**
The first sentence of a Javadoc comment is the text that appears in the
summary lists of a generated Javadoc website. Failure to either include a summary
or correctly punctuate the summary can result in poor output.  

## TypeName

Type names for classes, interfaces, enums, and annotations must be written in _UpperCamelCase_. 
Class names are typically nouns or noun phrases. For example, `Character` or `ImmutableList`. 
Interface names may also be nouns or noun phrases (for example, `List`), but may sometimes be 
adjectives or adjective phrases instead (for example, `Readable`).

**Rationale:**
This convention for type names is pervasive among Java programmers and 
is even the same convention used by companies like Oracle and Google.

## WhitespaceAround

You need to ensure that code tokens are surrounded by whitespace. 

```java
if (n==0) { // invalid
    ...
```
```java
if (n == 0) { // valid
    ...
```
```java
while(n == 0) { // invalid
    ...
```
```java
while (n == 0) { // valid
    ...
```

Empty constructor, method, class, enum, interface, loop bodies (blocks), 
lambdas of the forms presented below are exempt:

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

**Rationale:**
This convention improves readability.

## Recommended Emacs Configurations

Emacs can be configured in a couple different ways. The usual way is to edit
a file in your user home directory called `.emacs` and place desired configuration
settings there. You can create the `~/.emacs` file if it does not exist. If you 
have an `~/.emacs.el` or `~/.emacs.d/init.el file`, then you can place the lines 
in that file instead of `~/.emacs`.

```
;; add and configure line numbers and column numbers
(setq line-number-mode t)
(setq column-number-mode t)
(global-linum-mode 1)
(setq linum-format "%d ")
```

```
;; set a dedicated directory for backup files
(setq backup-directory-alist `(("." . "~/.saves")))
```

```
;; no tab characters in whitespace
(setq-default indent-tabs-mode nil)
```

```
;; handle indentation with 4 white spaces
(setq-default c-default-style "linux"
              c-basic-offset 4)
(setq-default tab-width 4)
(setq indent-line-function 'insert-tab)
```

```
;; auto remove trailing white space
(add-hook 'before-save-hook 'delete-trailing-whitespace)
```

```
;; highlight lines that exceed some column limit
(setq-default
 whitespace-line-column 100
 whitespace-style '(face lines))
(add-hook 'prog-mode-hook #'whitespace-mode)
```

## Recommended Vi Configurations

Vi/Vim can be configured in a couple different ways. The usual way is to edit
a file in your user home directory called `.vimrc` and place desired configuration
settings there. You can create the `~/.vimrc` file if it does not exist.

```
" enable line numbers
set number
```

```
" handle tabs and indents
filetype plugin indent on
set tabstop=4
set shiftwidth=4
set expandtab 
```

```
" show trailing whitespace
set list listchars=trail:.,extends:>
```

## How to Check

## Setup Checkstyle

Before you can use the `checkstyle` command on Nike for the first time, you will
need to configure your environment to make it available. To do this, follow the
steps below while logged into Nike:

1. **Add `/usr/local/checkstyle` to your `PATH`.** You can do this by adding the 
   following to your `~/.bash_profile`, then logging out and back in:

   ```
   # setup checkstyle
   export PATH=/usr/local/checkstyle:$PATH
   ```

## Run Checkstyle

To run checkstyle on an individual file, say `src/cs1302/Test.java`, you can execute
the command below. **The program is only guaranteed to work if your code compiles.**

```
$ checkstyle -c cs1302_checks.xml src/cs1302/Test.java
```

The `-c cs1302_checks.xml` option ensures that `checkstyle` is checking for compliance
with this styleguide. 

In the program output, any warnings that appear relate directly 
to style guidelines presented earlier in this document. For example:

```
[WARN] src/cs1302/Test.java:2: Missing a Javadoc comment. [MissingJavadocType]
```

Here, we see that the `MissingJavadocType` guideline was not met on line `2` in
`src/cs1302/Test.java`. The output even gives a short description of what it
thinks is wrong. If the short description is not sufficient to determine what the
issue is, then you should consult the specific guideline item in this styleguide
for more information.

### Multiple Files

You might want to check all the files in some `src` directory. To do this, you
try the following command:

```
$ find src -name "*.java" | xargs checkstyle -c cs1302_checks.xml
```

### Setup an Alias

Since you will be using the `checkstyle` command often, you may want to set up
a Bash alias to avoid typing the entire command each time. 
**To do this, add the following line to the end of your `~/.bash_profile` file:**

```
alias check1302="checkstyle -c cs1302_checks.xml"
```

After adding the line to your `~/.bash_profile` file, exit your text editor, 
then run the command:

```
$ source ~/.bash_profile
```

Now, you can run `checkstyle` on a Java file using the following, shortened, command:

```
$ check1302 src/cs1302/Test.java
```

### Output Examples

Here is some example output for an **invalid file**:

```
Starting audit...
[WARN] src/cs1302/Test.java:2: Missing a Javadoc comment. [MissingJavadocType]
[WARN] src/cs1302/Test.java:7:9: '{' at column 9 should be on the previous line. [LeftCurly]
[WARN] src/cs1302/Test.java:7:9: Must have at least one statement. [EmptyBlock]
[WARN] src/cs1302/Test.java:11: 'if' construct must use '{}'s. [NeedBraces]
Audit done.
```

Here is some example output for a **valid file**:

```
Starting audit...
Audit done.
```

<hr/>

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-nd/4.0/) [![DOI](https://zenodo.org/badge/202375392.svg)](https://zenodo.org/badge/latestdoi/202375392)

<small>
Copyright &copy; Michael E. Cotterell, Bradley J. Barnes, and the University of Georgia.
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a> to students and the public.
The content and opinions expressed on this Web page do not necessarily reflect the views of nor are they endorsed by the University of Georgia or the University System of Georgia.
Portions of this document are adapted from 
<a href="https://google.github.io/styleguide/">Google's Style Guides</a>
under a Creative Commons Attribution 3.0 Unported (CC BY 3.0) License.
</small>
