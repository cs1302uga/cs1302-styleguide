# CSCI 1302 Code Style Guide

![Approved for: Fall 2025](https://img.shields.io/badge/Approved%20for-Fall%202025-green)

Make sure you read through this document carefully. **In addition to describing why
code style is important and the code style guidelines for CSCI 1302, it also
describes how to use the `check1302` program on `Odin` to check your code as well
as Emacs and Vi configurations that, if used, will reduce the number of style issues
you have in your code moving forward.**

## Table of Contents

* [Compliance](#compliance)
* [Motivation](#motivation)
* [When and How to Check](#when-and-how-to-check)
  * [When to Check](#when-to-check)
  * [Checkstyle vs. Compiler Errors](#checkstyle-vs-compiler-errors)
  * [Run Checkstyle](#run-checkstyle)
  * [How to Read and Debug Checkstyle Errors](#how-to-read-and-debug-checkstyle-errors)
  * [Incremental Debugging Workflow](#incremental-debugging-workflow)
  * [Multiple Files](#multiple-files)
  * [Output Examples](#output-examples)
* [Recommended Emacs Configurations](#recommended-emacs-configurations)
  * [Show Style Guide Violations in the Editor](#show-style-guide-violations-in-the-editor)
* [Recommended Vi Configurations](#recommended-vi-configurations)
* [Specific Guidelines](#specific-guidelines)
  * [ArrayTypeStyle](#arraytypestyle)
  * [AtclauseOrder](#atclauseorder)
  * [CheckStyleException](#checkstyleexception)
  * [ClassTypeParameterName](#classtypeparametername)
  * [CommentsIndentation](#commentsindentation)
  * [ConstantName](#constantname)
  * [EmptyBlock](#emptyblock)
  * [EmptyCatchBlock](#emptycatchblock)
  * [EmptyLineSeparator](#emptylineseparator)
  * [FileTabCharacter](#filetabcharacter)
  * [GenericWhitespace](#genericwhitespace)
  * [Indentation](#indentation)
  * [InterfaceTypeParameterName](#interfacetypeparametername)
  * [JavadocMethod](#javadocmethod)
  * [JavadocParagraph](#javadocparagraph)
  * [JavadocTagContinuationIndentation](#javadoctagcontinuationindentation)
  * [LambdaParameterName](#lambdaparametername)
  * [LeftCurly](#leftcurly)
  * [LineLength](#linelength)
  * [LocalVariableName](#localvariablename)
  * [MemberName](#membername)
  * [MethodLength](#methodlength)
  * [MethodName](#methodname)
  * [MethodParamPad](#methodparampad)
  * [MethodTypeParameterName](#methodtypeparametername)
  * [MissingJavadocMethod](#missingjavadocmethod)
  * [MissingJavadocType](#missingjavadoctype)
  * [ModifierOrder](#modifierorder)
  * [MultipleVariableDeclarations](#multiplevariabledeclarations)
  * [NeedBraces](#needbraces)
  * [NonEmptyAtclauseDescription](#nonemptyatclausedescription)
  * [OneStatementPerLine](#onestatementperline)
  * [OneTopLevelClass](#onetoplevelclass)
  * [OperatorWrap](#operatorwrap)
  * [OuterTypeFilename](#outertypefilename)
  * [PackageName](#packagename)
  * [ParameterName](#parametername)
  * [ParenPad](#parenpad)
  * [PatternVariableName](#patternvariablename)
  * [RecordComponentName](#recordcomponentname)
  * [RecordTypeParameterName](#recordtypeparametername)
  * [RightCurly](#rightcurly)
  * [StaticVariableName](#staticvariablename)
  * [SummaryJavadoc](#summaryjavadoc)
  * [TypeName](#typename)
  * [WhitespaceAround](#whitespacearound)
* [References](#references)
* [Publication History](#publication-history)

## Compliance

From a technical standpoint, this style guide serves as the complete definition of
the coding standards for Java source code in CSCI 1302 at the University of Georgia.
When it comes to submitting code for an assignment, a Java source file is described
as being in _valid style_ (or compliant with this code style guide) if and only if
it adheres to the rules herein.

We recognize that some of the guidelines may be new for some students, so while
this style guide does contain the technical details for each guideline, it also
provides context, examples, and additional information that you may use to
check your code. In some assignments, terms like "checkstyle audit" or
"check1302 audit" will be used to remind you to check your code for compliance
with this style guide.

We also recognize that the terminal-based text editors used in this course are
new for many students. That is why we include recommendations for how to configure
those editors to help you stay in compliance. These recommendations will not
fix all code style violations, but they should help you avoid writing code that
violates some of the guidelines that are annoying to spot by hand and even more
annoying to fix.

Finally, we also include information about how to use the `check1302` program
on `Odin` to check your code for compliance. This is the same tool that graders
will use to check your code. **It is your responsibility to ensure that all
Java source files included with a submission are compliant.** This obviously
includes code that you write, but it also includes code that may have been given
to you as part of the assignment. It even includes code that may not be used
in your program but is still included with your submission.

## Motivation

Many companies will not let you commit changes for review until your
code meets their established guidelines--a notable example is Google.
Why do these companies do this? The short answer is that enforcing
good style makes things easier for everybody, and while you may not
believe it just yet, it does, in fact, make things easier for you
too.

In the preface to _The Practice of Programming_ [[TPOP](#ref-tpop)] by
[Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan)
and [Pike](https://en.wikipedia.org/wiki/Rob_Pike), the authors ask the
reader to consider some questions related to several difficult, tedious,
or annoying scenarios that programmers find themselves in when writing
code (i.e., the "not fun" parts). Their last two questions are specifically
worth mentioning here:

* Have you ever tried to make a modest change in someone else's program?
* Have you ever rewritten a program because you couldn't understand it?

The authors end their interrogation with the following comments:

> These things happen to programmers all the time. But dealing with such
> problems is often harder than it should be because topics like testing,
> debugging, portability, performance, design alternatives, and
> style--the _practice_ of programming--are not usually the focus of
> computer science or programming courses. Most programmers learn them
> haphazardly as their experience grows, and a few never learn them
> at all.
> **-- Kernighan and Pike**

Regarding style, they even go on to say:

> Good style is so important to good programming that we have chosen
> to cover it first. Well-written programs are better than badly-written
> ones--they have fewer errors and are easier to debug and modify--so
> **it is important to think about style from the beginning**.
> **-- Kernighan and Pike**

If your code looks good, which we will define here as adhering to an
established style guide, then:

* It is easier to read, especially when compared to code that applies stylistic choices
  inconsistently. It is certainly easier to read by those who are familiar with the
  conventions outlined in the style guide.

* It is easier to identify common bugs and syntax errors (e.g., missing a curly brace).
  This saves real-world time when it comes to fixing problems in your code.

* It is easier to extend and/or incorporate into other projects. This results in your
  code being more useful to others as well as your future self.

The list could go on. The important thing to remember is that **quality not only
refers to the output of a program but also its effect on the people who interact
with the code**. Rarely, in practice, are you the only one who will read and use
your code. If you're a software engineer, then it is very likely that _many_
people will interact with your code over time and that you will interact with _lots_
of code written by others as well.

## When and How to Check

Here is a fair and honest warning: if you wait until you are nearly done
writing some code before checking its style, then do not be surprised if
you significantly increase the overall amount of time you need
to complete an assignment. You won't have a good time. Much of that extra
time will be from:

* fixing many code style violations;
* fixing bugs introduced by fixing code style violations;
* fixing bugs earlier that would have been easier to spot had your code
   been in compliance; and
* rewriting code you wrote earlier because you no longer understand
   how it works.

Why would you subject yourself to that? Is there a better way? Remember,
Kernighan and Pike said, "it is important to think about style from the
beginning." If you're a beginner, then that seems almost as daunting as
the alternative, even if you do nod your head as we list out the
benefits. It's daunting because you may not know what good style is yet.
We know this, and that is why we provide you with access to Checkstyle,
a program that automates the process of checking your code for compliance!

### When to Check

You should check your code early and often. The goal is to help you learn
good style, so every time you see that you're not in compliance, you should
take the time to fix it. Although you may find that you have many violations
early on (that's to be expected), over time you will find that you run into
fewer and fewer violations. This happens because you start to write
code in good style. It's a pretty neat way to learn.

If you don't check your code for compliance early and often, then not only
are you dooming yourself to the miserable time sink of "not fun" activities
described earlier, you are actively avoiding learning.

### Checkstyle vs. Compiler Errors

It is essential to understand the distinction between compiler errors and style check violations:

* **Compiler (`javac`)**: The Java compiler validates syntax, grammar, and type safety, converting your source code into executable bytecode (`.class` files). If your code contains a syntax error (e.g., missing semicolon, undefined symbol, type mismatch), the compiler halts and will not produce executable bytecode.
* **Style Checker (`check1302` / Checkstyle)**: Checkstyle performs _static analysis_ on your Java source code. It parses the code into an **Abstract Syntax Tree (AST)** and evaluates whether your code conforms to readability, indentation, naming, and documentation standards.

> **CRITICAL:** **Checkstyle is only guaranteed to work if your code compiles.** Because Checkstyle relies on parsing a syntactically valid Java AST, feeding uncompilable code to `check1302` can produce misleading parser exceptions or crash the audit tool. **Always run `javac` before running `check1302`!**

### Run Checkstyle

To check your Java source code for compliance, you can use a custom version
of the Checkstyle program on `Odin` called `check1302`.

To run the `check1302` program on an individual file, say `src/cs1302/Test.java`,
you can execute the command below:

```bash
check1302 src/cs1302/Test.java
```

### How to Read and Debug Checkstyle Errors

When `check1302` detects style violations, it outputs diagnostic lines formatted as follows:

```plaintext
[ERROR] src/cs1302/Test.java:7:9: '{' at column 9 should be on the previous line. [LeftCurly]
```

Each component of this message provides specific diagnostic information:

1. **Severity Level (`[ERROR]`)**: Indicates that the check failed. All Checkstyle errors must be resolved to achieve full style compliance.
2. **File Path (`src/cs1302/Test.java`)**: The relative path to the Java source file where the violation occurred.
3. **Line and Column (`7:9`)**: The exact location of the issue. In this example, the violation is on line `7`, starting at column `9`.
4. **Diagnostic Description (`'{' at column 9 should be on the previous line.`)**: A concise summary describing what Checkstyle found and what it expected.
5. **Guideline Identifier (`[LeftCurly]`)**: The name of the specific style guide rule enclosed in square brackets. This corresponds directly to the guideline anchor in this document (e.g., [`LeftCurly`](#leftcurly)).

### Incremental Debugging Workflow

To resolve style errors quickly without feeling overwhelmed, follow this recommended 4-step workflow:

1. **Step 1: Verify Clean Compilation First**

   ```bash
   javac -d bin -cp bin src/cs1302/Test.java
   ```

   Confirm that `javac` succeeds with zero errors.

2. **Step 2: Run `check1302`**

   ```bash
   check1302 src/cs1302/Test.java
   ```

3. **Step 3: Fix Errors from Top to Bottom**
   Always fix errors starting from the top of the output. Structural issues (such as missing curly braces, unclosed Javadoc comments, or mismatched delimiters) can cause Checkstyle's parser to misinterpret subsequent lines, creating "cascade" false-positive errors further down the file.

4. **Step 4: Re-Audit Frequently**
   Run `check1302` after fixing one or two issues to verify that the error count decreases and no new formatting violations were introduced.

### Multiple Files

You might want to check all the files in some `src` directory. To do this, you can
pass the entire directory to `check1302` as in the following command:

```bash
check1302 src
```

### Output Examples

Here is some example output for an **invalid file**:

```plaintext
Starting audit...
[ERROR] src/cs1302/Test.java:2: Missing a Javadoc comment. [MissingJavadocType]
[ERROR] src/cs1302/Test.java:7:9: '{' at column 9 should be on the previous line. [LeftCurly]
[ERROR] src/cs1302/Test.java:7:9: Must have at least one statement. [EmptyBlock]
[ERROR] src/cs1302/Test.java:11: 'if' construct must use '{}'s. [NeedBraces]
Audit done.
```

In the example above, the programmer would need to find the four error messages listed in
the [Specific Guidelines](#specific-guidelines) section of this document, and also be sure to
read the description and motivation for each error. Here, the programmer would look up the
`MissingJavadocType`, `LeftCurly`, `EmptyBlock`, and `NeedBraces` details. The `checkstyle`
output usually provides extra information to help you fix the problem as illustrated in
the example above.

Here is some example output for a **valid file**:

```plaintext
Starting audit...
Audit done.
```

## Recommended Emacs Configurations

**_This section is intended for Emacs users._**
_If you are a Vi/Vim user, then refer to the
[Recommended Vi Configurations](#recommended-vi-configurations) section._

Emacs is used by thousands of programmers every day, and each of those
programmers may need to follow one or more style guides at any given
time. Under its default configuration, Emacs can assist programmers in dealing
with many common style issues, and its configuration settings can be
adjusted to help accommodate additional guidelines related to style. While
the degree to which Emacs provides assistance may vary from guideline to
guideline, any assistance at all saves programmers a lot of time and
energy.

To update your Emacs configuration settings so that it assists with
more of the specific guidelines described in this code style guide,
you need to add some text to the end of a configuration file. In most
cases, this file is stored in your home directory and named `.emacs` -- this
is a text file that is literally named `.emacs` (instead of something like
`.emacs.txt`). From your home directory on Odin, execute the `ls -a` command.
This will list files that start with a `.`. If you do not have a `~/.emacs` file,
then check to see
if either `~/.emacs.el` or `~/.emacs.d/init.el` exists; if so, then use one
of those files in the steps below. If none of these files exist, then we recommend that
you create `~/.emacs` and store your configuration settings there.

**If you do not understand what file you need to create or edit,
then please ask your instructor or a TA! The following instructions
assume that your Emacs configuration file is `~/.emacs`, which is the
default for most students.**

You can open the `~/.emacs` file in Emacs using the following command, regardless
of whether the `~/.emacs` file already exists -- if the file does not yet exist, then
it will be created once you save the file using Emacs:

```bash
emacs ~/.emacs
```

Once your `~/.emacs` file is open in Emacs, take a quick look at it. It may be
empty or it may have some existing lines in it -- either situation is okay. If
there are existing lines, then you are NOT required to understand what they do
for this course.

Now, select and copy the configuration text below -- we recommend that you select
it with your mouse and copy it using a right click (and selecting "Copy") instead
of using a keyboard shortcut:

```emacs
;; handle multi-line inline lambda expressions
(setq c-offsets-alist '((arglist-cont-nonempty . 0)))
```

Now, return to Emacs where your `~/.emacs` file should still be open, and navigate to
the bottom/end of the file by pressing `M->` (i.e., `M-Shift-.` where `.` is the period) -- if
the file is empty, then you won't go very far (that's okay). Once your cursor is at the
bottom/end of the file, press the Return key once or twice to create some blank lines, then
paste what you copied above by right-clicking on the terminal screen -- if right-clicking does
not paste the text automatically, then right-click and select the "Paste" option to paste
the text.

Once the text is pasted in the file, press `C-x C-s` to save the file, then `C-x C-c` to
close/exit Emacs.

The configuration changes should take effect the next time you start Emacs. If you get an
error related to your "Init file" the next time you start Emacs, see an instructor
during office hours for assistance. If you do not encounter an error, then you should be
good to go!

<!--
```emacs
;; add and configure line numbers and column numbers
(setq line-number-mode t)
(setq column-number-mode t)
(global-display-line-numbers-mode)

;; set a dedicated directory for backup files
(setq backup-directory-alist `(("." . "~/.saves")))

;; set a backup policy
(setq make-backup-files t)
(setq version-control t)
(setq kept-new-versions 5)
(setq delete-old-versions t)
(setq vc-make-backup-files t)

;; no tab characters in whitespace
(setq-default indent-tabs-mode nil)

;; handle indentation with 4 white spaces
(setq-default c-default-style "linux"
              c-basic-offset 4)
(setq-default tab-width 4)
(setq indent-line-function 'insert-tab)

;; handle multi-line inline lambda expressions
(setq c-offsets-alist '((arglist-cont-nonempty . 0)))

;; auto remove trailing white space
(add-hook 'before-save-hook 'delete-trailing-whitespace)

;; highlight lines that exceed some column limit
(setq-default
 whitespace-line-column 100
 whitespace-style '(face lines))
(add-hook 'prog-mode-hook #'whitespace-mode)

;; run check1302 on saved version of current file with M-x check1302
(defun check1302 ()
  (interactive)
  (when (eq major-mode 'java-mode)
    (shell-command
     (format "check1302 %s" buffer-file-name))))
```

If you want to know what any of these Emacs settings do, then you can use
`M-x describe-variable` while in Emacs. When you see the "Describe variable:" prompt,
provide the setting variable name (e.g., `make-backup-files`).
//-->

<!--
### Additional Emacs Configurations (Optional)

If you followed the instructions provided by your instructor to enable the
CSCI 1302 shell profile on Odin, then the Emacs that you have access to
is pre-configured to let you use additional Emacs packages using
[use-package](https://github.com/jwiegley/use-package). If you include
`use-package` declarations in your Emacs configuration file, then Emacs
may need to download and install some things the next time it runs in order
to make things work -- such installations may take several seconds to
complete, but they only happen once unless package updates are installed.

**NOTE:** Emacs 29.1 and above supports `use-package` statements by default.
Older versions of Emacs require users to manually install the
[use-package](https://github.com/jwiegley/use-package) package
first.

#### Automatically Update Emacs Packages

Add the lines below to your Emacs configuration file to install and
configure the [`auto-package-update`](https://github.com/rranelli/auto-package-update.el)
package via use-package so that your installed Emacs packages are kept up
to date. After setting this up, Emacs will occasionally ask you if you want
to update packages when it starts -- when it does this, it asks the question
in the [echo area](https://www.gnu.org/software/emacs/manual/html_node/emacs/Echo-Area.html)
near the bottom of the screen.

```elisp
;; automatically update emacs packages
(use-package auto-package-update
  :config
  (setq auto-package-update-delete-old-versions t)
  (setq auto-package-update-hide-results t)
  (setq auto-package-update-prompt-before-update t)
  (setq auto-package-update-interval 4)
  (auto-package-update-maybe))
```
-->

### Show Style Guide Violations in the Editor (Optional)

Add the lines below to your Emacs configuration file to install and
configure the [`flycheck`](https://www.flycheck.org/) package via
use-package so that style guide violations are shown directly inside
Emacs when editing Java source code files.

```elisp
;; enable on-the-fly syntax checking
(use-package flycheck
  :init (global-flycheck-mode)
  :commands flycheck-parse-checkstyle
  :config
  (progn
    ;; setup a syntax checker that conforms to the CSCI 1302 Code Style Guide
    (flycheck-define-checker java-checkstyle-checker
      "A Java style checker using Checkstyle."
      :command ("checkstyle" "-c" "/usr/local/mepcott/cs1302/cs1302_checks.xml" "-f" "xml" source)
      :error-parser flycheck-parse-checkstyle
      :enable t
      :modes java-mode)
    ;; show style guide violations in emacs when in java-mode
    (add-to-list 'flycheck-checkers 'java-checkstyle-checker)))
```

## Recommended Vi Configurations

**_This section is intended for Vi/Vim users._**
_If you are an Emacs user, then refer to the
[Recommended Emacs Configurations](#recommended-emacs-configurations) section._

Vi/Vim, hereafter referred to as Vi, is used by thousands of programmers every day,
and each of those programmers may need to follow one or more style guides at any
given time. Under its default configuration, Vi can assist programmers in dealing
with many common style issues, and its configuration settings can be adjusted to
help accommodate additional guidelines related to style. While the degree to which Vi
provides assistance may vary from guideline to guideline, any assistance at all
saves programmers a lot of time and energy.

To update your Vi configuration settings so that it assists with
more of the specific guidelines described in this code style guide,
you need to add some text to the end of a configuration file. In most
cases, this file is stored in your home directory and named `.vimrc` -- this
is a text file that is literally named `.vimrc` (instead of something like
`.vimrc.txt`).

Let's assume that you want to store your settings in `~/.vimrc`.
You can open that file with Vi, even if it does not yet exist -- it
will get created when you save. Once open, add the lines we present below
to the end of the file (could be the top if it's empty), then save the
file and exit Vi. If you did this correctly, then the settings will
take effect the next time you launch Vi. One quick way to see if you
got it working is to open a `.java` file in Vi and see if it shows line
numbers; if so, then you should be good to go!

**If you do not understand what file you need to create or edit,
then please ask your instructor or a TA!**

Here are the lines that you should add to your Vi configuration
file:

```vim
" enable line numbers
set number

" handle tabs and indents
filetype plugin indent on
set tabstop=4
set shiftwidth=4
set expandtab

" show trailing whitespace
set list listchars=trail:.,extends:>
```

## Specific Guidelines

The name for each of these guidelines corresponds to a Checkstyle module
configured in [`cs1302_checks.xml`](cs1302_checks.xml) for use by the
`check1302` program. This was done so that it's easier for users to relate
`check1302` program output to the actual guidelines.

### ArrayTypeStyle

Array brackets (`[]`) must be attached to the **type** identifier (Java style), never to the variable name (C style).

#### Valid Examples

```java
// Valid: Java style - brackets attached to type
String[] names = new String[10];
int[] scores = new int[] {1, 2, 3};

public static void main(String[] args) {
} // main

public int[] getScores() {
    return this.scores;
} // getScores
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: C style - brackets attached to variable name
String names[] = new String[10];
int scores[] = new int[] {1, 2, 3};

public static void main(String args[]) {
    ...
} // main
```

#### How to Fix

- Move square brackets `[]` from after the variable name to directly after the element type name (e.g. `String[] args`, not `String args[]`).

#### Rationale & Instructor Notes

**Rationale:**
In Java, an array is a distinct reference type. Attaching the brackets to the type name (`int[]`) clearly specifies what *type* the variable holds, consistent with how all other reference type variables are declared.

**Instructor Note:**
C-style array syntax exists in Java solely for backward compatibility with C/C++. Always write `String[] args` in modern Java.

### AtclauseOrder

When multiple Javadoc block tags (`@...`) are present on a class, interface, enum, method, constructor, or field, they must appear in the following standard order:

1. `@param`
2. `@return`
3. `@throws`
4. `@see`
5. `@since`
6. `@serial` (or `@serialField`, `@serialData`)
7. `@deprecated`

#### Valid Examples

```java
/**
 * Searches the collection for the specified student identifier.
 *
 * @param studentId the unique integer identifier of the student
 * @param includeArchived whether to search archived academic records
 * @return the matching student record, or {@code null} if not found
 * @throws IllegalArgumentException if {@code studentId} is negative
 * @see #findStudentByName(String)
 */
public Student findStudent(int studentId, boolean includeArchived) {
    // search implementation
    return null;
} // findStudent
```

#### Common Pitfalls & Invalid Examples

```java
/**
 * Computes grade statistics.
 *
 * @return the calculated grade point average
 * @param grades array of numerical course grades  // Invalid: @return appears before @param
 * @throws NullPointerException if grades is null
 */
public double computeGpa(double[] grades) {
    return 0.0;
} // computeGpa
```

```java
/**
 * Encodes data into binary format.
 *
 * @see #decode(byte[])                           // Invalid: @see appears before @param/@return
 * @param data raw string to encode
 * @return byte array representation
 */
public byte[] encode(String data) {
    return new byte[0];
} // encode
```

#### How to Fix

- Reorder your Javadoc block tags so that all `@param` tags appear first, followed by `@return`, followed by all `@throws` tags, followed by any `@see` references.
- Group tags of the same type together (e.g., list all `@param` tags in the order the parameters appear in the method signature).

#### Rationale & Instructor Notes

**Rationale:**
Following a universal ordering convention allows developers and automated documentation tools to scan documentation comments for parameters, return values, exceptions, and references in a predictable, intuitive sequence.

**Instructor Note:**
In CS2 assignments, a very common mistake is placing `@return` before `@param` or scattering `@throws` tags between parameter descriptions. Always structure your Javadoc tags top-down: Inputs (`@param`) &rarr; Output (`@return`) &rarr; Errors (`@throws`).

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

### ClassTypeParameterName

Generic type parameter names for generic classes must conform to one of two formats:

1. A single uppercase letter optionally followed by a single digit (e.g., `E`, `T`, `K`, `V`, `T1`); or
2. An `UpperCamelCase` name ending with `T` or `Type` (e.g., `ElementT`, `RequestType`, `DataT`).

#### Valid Examples

```java
// Valid: Single uppercase letters
public class CustomList<E> {
} // CustomList<E>

// Valid: Descriptive names ending with T or Type
public class ApiResponse<DataT> {
} // ApiResponse<DataT>

public class DatabaseSession<ContextType> {
} // DatabaseSession<ContextType>
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Lowercase type parameter name
public class CustomList<element> {
} // CustomList<element>

// Invalid: UpperCamelCase without trailing T or Type (looks like a concrete class)
public class ApiResponse<Data> {
} // ApiResponse<Data>
```

#### How to Fix

- Use conventional single-letter type parameters (`E` for Element, `T` for Type, `K` for Key, `V` for Value).
- If using multi-character names for readability, ensure they end with `T` or `Type` (e.g., `ElementT` or `ElementType`).

#### Rationale & Instructor Notes

**Rationale:**
Single uppercase letters or `T`/`Type`-suffixed names prevent generic type parameters from being visually confused with concrete class names (like `String` or `Data`).

**Instructor Note:**
When implementing custom collections such as `LinkedList<E>` or `BinarySearchTree<T>`), use `E` for collections of elements and `T` for generic types.

### CommentsIndentation

Block comments (`/* ... */`) and single-line comments (`// ...`) must have the exact same indentation level as the surrounding code block or the statement that immediately follows them.

#### Valid Examples

```java
// Valid: Comments indented to the exact indentation level of surrounding code
public void calculate() {
    // Initialize running counter
    int count = 0;

    /*
     * Iterate through all available records
     * and accumulate the total score.
     */
    for (int i = 0; i < scores.length; i++) {
        // Add current score
        count += scores[i];
    } // for
} // calculate
```

#### Common Pitfalls & Invalid Examples

```java
public void calculate() {
// Invalid: Comment indented too far to the left (0 spaces instead of 4)
    int count = 0;

        // Invalid: Comment indented too far to the right (8 spaces instead of 4)
    int total = 0;
} // calculate
```

#### How to Fix

- Align the comment's leading slashes (`//` or `/*`) with the indentation level of the code directly below or around it.

#### Rationale & Instructor Notes

**Rationale:**
Properly indented comments maintain the visual hierarchy of the enclosing code structure and prevent reading distractions.

**Instructor Note:**
Comments explaining a block or statement should line up horizontally with that statement. Trailing closing comments (e.g., `} // if`) belong on the same line as the closing brace.

### ConstantName

Constant names must use `CONSTANT_CASE`: all uppercase letters with words separated by a single underscore (`_`).

A **constant** in Java is defined as a field that is declared both `static` and `final`, or a field declared in an interface or annotation interface (which are implicitly `public static final`), excluding standard JVM serialization identifiers (`serialVersionUID` and `serialPersistentFields`).

#### Valid Examples

```java
public class MathUtils {

    // Valid: static final fields in CONSTANT_CASE
    public static final double PI = 3.141592653589793;
    public static final int MAX_BUFFER_SIZE = 1024;
    public static final String DEFAULT_ENCODING = "UTF-8";

} // MathUtils

public interface DatabaseConfig {

    // Valid: Interface fields are implicitly public static final
    String DEFAULT_HOST = "localhost";
    int DEFAULT_PORT = 5432;

} // DatabaseConfig

public interface DatabaseConfig {

    // Valid: Interface fields are implicitly public static final
    public static final String DEFAULT_HOST = "localhost";
    public static final int DEFAULT_PORT = 5432;

} // DatabaseConfig
```

#### Common Pitfalls & Invalid Examples

```java
public class MathUtils {

    // Invalid: lowerCamelCase used on static final constant
    public static final int maxBufferSize = 1024;

    // Invalid: Missing underscores between words
    public static final String DEFAULTENCODING = "UTF-8";

} // MathUtils
```

#### How to Fix

- Convert all letters in `static final` constant names to uppercase, separating words with underscores (`_`).
- Remember that fields that are `final` but **not** `static` (instance constants) are not considered class constants under this rule; they must be written in `lowerCamelCase` as specified in [`MemberName`](#membername).

#### Rationale & Instructor Notes

**Rationale:**
`CONSTANT_CASE` gives immediate visual cues to anyone reading your code that a value is immutable and shared across all instances of the class.

**Instructor Note:**
If a variable is only `final` (e.g., `private final int studentId;`), it is an instance field that varies per object instance and must be named in `lowerCamelCase`. Only add `CONSTANT_CASE` when the variable is both `static` and `final`.

### EmptyBlock

Empty code blocks are prohibited. Every code block (`class`, `interface`, `method`, `constructor`, `if`, `else`, `for`, `while`, `do-while`, `switch`, `try`, `finally`) must contain at least one executable statement or valid explanatory comment.

#### Valid Examples

```java
// Valid: Block contains executable statements
if (list.isEmpty()) {
    System.out.println("List is empty");
} // if

// Valid: Overridden interface method with documented no-op implementation
@Override
public void windowClosing(WindowEvent e) {
    // Intentionally left empty as no action is required on window closing
} // windowClosing
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Empty 'if' block
if (isValid) {
} // if
```

```java
// Invalid: Empty 'else' block
if (score > 50) {
    passed = true;
} else {
} // if
```

#### How to Fix

- If an `if` or `else` block is empty, invert your conditional expression or remove the unneeded clause entirely.
- If an empty method is required by an interface or abstract class, add an explicit explanatory comment explaining why no operation is performed.
- For empty `catch` blocks, refer to the [`EmptyCatchBlock`](#emptycatchblock) guideline.

#### Rationale & Instructor Notes

**Rationale:**
Empty code blocks often indicate forgotten logic, leftover debugging code, or inverted conditional logic that confuses readers and introduces subtle execution bugs.

**Instructor Note:**
If you write `if (condition) {} else { doSomething(); }`, then simplify it to `if (!condition) { doSomething(); }` to avoid the empty block.

### EmptyCatchBlock

Empty `catch` blocks are strictly disallowed. When catching an exception, you must either handle the exception, log or print an error message, rethrow a custom or wrapped exception, or document why the exception is intentionally ignored.

#### Valid Examples

```java
// Valid: Handling the exception with recovery or logging
try {
    double value = Double.parseDouble(input);
    process(value);
} catch (NumberFormatException nfe) {
    System.err.println("Invalid numeric input format: " + nfe.getMessage());
} // try

// Valid: Intentionally ignored exception with explanatory comment
try {
    Thread.sleep(100);
} catch (InterruptedException ie) {
    // Interruption is expected during normal shutdown; restore interrupt flag
    Thread.currentThread().interrupt();
} // try
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Silently swallowing an exception without handling or explanation
try {
    FileReader reader = new FileReader("config.txt");
    reader.read();
} catch (IOException ioe) {
    // empty catch block
} // try
```

#### How to Fix

- Handle the error appropriately (e.g., alert the user, provide a fallback value, or clean up resources).
- If your method cannot recover from the exception, propagate it by adding `throws <ExceptionType>` to the method signature instead of catching it.
- If ignoring the exception is genuinely intentional, add an explicit explanatory comment inside the catch block explaining why.

#### Rationale & Instructor Notes

**Rationale:**
Silently swallowing exceptions ("exception swallowing") is one of the most dangerous anti-patterns in software development. It hides system failures, corrupts program state, and makes debugging almost impossible because failures fail silently.

**Instructor Note:**
In CS2 labs and projects, never leave a catch block empty. At minimum, print an error or propagate the exception using `throws`.

### EmptyLineSeparator

Empty blank lines must separate major structural components in Java source files, including:

* After the `package` statement;
* After `import` declaration groups;
* Between constructors, methods, nested types, static initializers, and instance initializers.

Empty lines are optional between variable field declarations (e.g., consecutive instance variable fields).

#### Valid Examples

```java
package cs1302.example;

import java.util.List;
import java.util.ArrayList;

public class StudentManager {

    private String name;
    private int id;

    public StudentManager(String name, int id) {
        this.name = name;
        this.id = id;
    } // StudentManager

    public String getName() {
        return this.name;
    } // getName

} // StudentManager
```

#### Common Pitfalls & Invalid Examples

```java
package cs1302.example;
import java.util.List;  // Invalid: No blank line between package and imports
public class Student {  // Invalid: No blank line between imports and class
    public void a() {}
    public void b() {}  // Invalid: No blank line between method declarations
}
```

#### How to Fix

* Insert at least one blank line after the package declaration, after your import block, and between consecutive method/constructor declarations.

#### Rationale & Instructor Notes

**Rationale:**
Vertical whitespace separates discrete units of logic, preventing code files from looking like dense walls of text and making visual navigation intuitive.

**Instructor Note:**
Keep one blank line between each method in your class. You do not need blank lines between single-line field declarations.

### FileTabCharacter

No tab characters (`\t`) are allowed in the normal whitespace of the source code.
This does not include tabs in string literals. For example, the following
snippet is okay:

```java
String s = "word1\tword2";
```

What tabs are not allowed? Specifically, this policy forbids a tab from
occurring in the underlying whitespace of your source code. Some
examples that illustrate the difference are provided below. When using
`cat` to display a file, the `-T` option can be used to display `TAB` characters
as `^I`.

* Use the command below to generate `One.java`, a small class that
  violates the `FileTabCharacter` guideline by using a single `TAB`
  character in the whitespace just before the declaration of
  `private int x = 1;`:

  ```bash
  echo -e "public class One {\n\tprivate int x = 1;\n} // One\n" > One.java
  ```

  ```bash
  $ cat -T One.java
  public class One
  ^Iprivate int x = 1;
  } // One
  ```

  Since a `TAB` (`\t`) is used in the whitespace, the line with the `TAB`
  may appear differently depending on how the program used to view the
  file is configured. We can simulate that here using the `tabs` command (see `man tabs` on most systems for more information):

  ```bash
  $ tabs 3; cat One.java
  public class One
     private int x = 1;
  } // One
  ```

  ```bash
  $ tabs 5; cat One.java
  public class One
       private int x = 1;
  } // One
  ```

  ```bash
  $ tabs 9; cat One.java
  public class One
           private int x = 1;
  } // One
  ```

* Use the command below to generate `Two.java`, a small class where
  four spaces are used before the declaration of `private int y = 2;`:

  ```bash
  echo -e "public class Two {\n\tprivate int y = 2;\n} // Two\n" > Two.java
  ```

  ```bash
  $ cat -T Two.java
  public class Two
    private int y = 2;
  } // Two
  ```

  Since no `TAB` (`\t`) is used in the whitespace, the line with four
  spaces does not appear differently depending on how the program used
  to view the file is configured. We can simulate that here:

  ```bash
  $ tabs 3; cat Two.java
  public class Two
      private int y = 2;
  } // Two
  ```

  ```bash
  $ tabs 5; cat Two.java
  public class Two
      private int y = 2;
  } // Two
  ```

  ```bash
  $ tabs 9; cat Two.java
  public class Two
      private int y = 2;
  } // Two
  ```

When you go to write the inside/body of a class or method, you likely press the
`TAB` key on your keyboard. Most text editors implement this by placing the
following directly in the contents of the code file where you press the
`TAB` key:

1. One `\t` (single tab character); or
1. Multiple ` ` (whitespace characters).

This policy specifically forbids the first of these two approaches.
If you use the [recommended Emacs configurations](#recommended-emacs-configurations)
or [recommended Vi configurations](#recommended-vi-configurations), then
you will be able to avoid _future_ non-conformance with this policy.

#### How to Fix

* **Fix in Emacs**: Move to the beginning of the file and run `C-u M-x untabify RET`.
* **Fix in Vim**: Run `:set expandtab` followed by `:retab`.

#### Rationale & Instructor Notes

**Rationale:**
The use of tabs instead of spaces results in different text editors and terminal environments displaying the same file with distorted indentation, depending on the tab width configured for the viewer. Using spaces guarantees identical visual indentation everywhere.

**Instructor Note:**
Tab width defaults vary widely across editors and emulators. On Odin, a tab character will show up as 1 tab, which is 4 spaces. Thus, converting tabs to 4 spaces ensures your code looks the same on Odin as it did on your screen.

### GenericWhitespace

Whitespace around generic type arguments and type parameters (the `<` and `>` angle brackets) must adhere to standard Java conventions:

* No whitespace precedes `<` in generic class/interface instantiations, type declarations, or method declarations.
* No whitespace immediately follows `<` or immediately precedes `>`.
* Whitespace follows `>` only if followed by a keyword, variable name, or operator (not when followed by `(`, `)`, `[`, `]`, or `,`).

#### Valid Examples

```java
// Valid: Proper spacing around generic angle brackets
List<String> names = new ArrayList<>();
Map<String, List<Integer>> scoreMap = new HashMap<>();

public <T> T getFirst(List<T> items) {
    return items.isEmpty() ? null : items.get(0);
} // getFirst
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Spaces inside angle brackets
List< String > names = new ArrayList< >();

// Invalid: Space before opening angle bracket
List <String> names = new ArrayList<>();
```

#### How to Fix

* Remove any spaces immediately after `<` or before `>`.
* Remove any spaces before `<` in type declarations (e.g. write `List<String>`, not `List <String>`).

#### Rationale & Instructor Notes

**Rationale:**
Standard spacing around angle brackets ensures generic declarations remain compact and distinct from comparison operators (`<` and `>`).

**Instructor Note:**
When using generics, the diamond operator (`<>`) in constructor calls may be empty, but it must not have any spaces inside the angle brackets: `new ArrayList<>()`.

### Indentation

The following indentation rules must be followed:

| Property                  | Description                                                                     | Spaces |
|---------------------------|---------------------------------------------------------------------------------|--------|
| `basicOffset`             | how far the new indentation level should be indented when on the next line      | 4      |
| `braceAdjustment`         | how far a brace should be indented when on the next line                        | 0      |
| `caseIndent`              | how far a case label should be indented when on the next line                   | 0      |
| `throwsIndent`            | how far a throws clause should be indented when on the next line                | 4      |
| `arrayInitIndent`         | how far an array initializer list item should be indented when on the next line | 4      |
| `lineWrappingIndentation` | how far the continuation line should be indented when line-wrapping is present  | 4      |

Each new block level (classes, methods, control structures) must be indented
by exactly 4 spaces relative to the enclosing scope:

```java
// Valid style: 4-space indentation per block level
public class CalculationService {

    public void calculate() {
        int total = 0;
        if (total > 0) {
            total++;
        } // if
    } // calculate

} // CalculationService
```

```java
// Invalid style: 2-space indentation
public class CalculationService {

  public void calculate() {
    int total = 0;
    if (total > 0) {
      total++;
    } // if
  } // calculate

} // CalculationService
```

Case labels in a `switch` statement are aligned with the `switch` statement
(`caseIndent = 0`):

```java
// Valid style: switch statement with aligned case labels
public String getDayCategory(int day) {
    String category;
    switch (day) {
    case 1:
    case 7:
        category = "Weekend";
        break;
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
        category = "Weekday";
        break;
    default:
        category = "Invalid";
        break;
    } // switch
    return category;
} // getDayCategory
```

In a `switch` expression, `case` and `default` labels are indented by 4 spaces relative to the `switch` expression keyword, and `->` is used instead of `:` as the separator:

```java
// Valid style: switch expression with aligned case labels
public String getDayCategory(int day) {
    String category = switch (day) {
        case 1, 7 -> "Weekend";
        case 2, 3, 4, 5, 6 -> "Weekday";
        default -> {
            String error = "Invalid day: " + day;
            yield error;
        } // default
    };
    return category;
} // getDayCategory
```

Continuation lines for line wrapping, `throws` clauses, and multi-line array
initializers are indented by 4 spaces:

```java
// Valid style: 4-space continuation indentation
public void processItems(List<String> items)
    throws IllegalArgumentException, IllegalStateException {
    int[] numbers = new int[] {
        1,
        2,
        3
    };
} // processItems
```

Sometimes, indentation rules are a little hard to parse when parentheses and
curly braces are involved, as is sometimes the case with multi-line inline lambda
expressions. An inline lambda expression is a lambda expression that is supplied
as an argument for a parameter of a method. Here is an example:

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

#### How to Fix

- Configure your text editor (e.g., Emacs, Vim, etc.) to insert **4 spaces** per tab press and disable hard tabs (`indent-tabs-mode nil` / `expandtab`).
- Indent each nested block level by exactly 4 spaces relative to its enclosing braces.
- Indent continuation lines (line wrapping, `throws` clauses, multi-line arrays) by 4 spaces.

#### Rationale & Instructor Notes

**Rationale:**
Consistent 4-space indentation establishes a clear visual hierarchy, making the scope and nesting of classes, methods, and control flow immediately apparent.

**Instructor Note:**
In CS2, never mix 2-space and 4-space indentation. If your editor indents by 2 spaces by default, adjust its settings to 4 spaces for Java files.

### InterfaceTypeParameterName

Generic type parameter names for generic interfaces must conform to one of two formats:

1. A single uppercase letter optionally followed by a single digit (e.g., `T`, `E`, `K`, `V`, `T1`); or
2. An `UpperCamelCase` name ending with `T` or `Type` (e.g., `ElementT`, `KeyType`, `ValueType`).

#### Valid Examples

```java
// Valid: Single uppercase letters
public interface Map<K, V> {
    V get(K key);
} // Map<K, V>

// Valid: Descriptive names ending with T or Type
public interface Transformer<InputT, OutputT> {
    OutputT transform(InputT input);
} // Transformer<InputT, OutputT>
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Lowercase type parameter names
public interface Map<key, val> {
} // Map<key, val>

// Invalid: Multi-character name without T/Type suffix
public interface Transformer<Source, Target> {
} // Transformer<Source, Target>
```

#### How to Fix

- Change interface generic parameters to single uppercase letters (`K`, `V`, `T`, `E`) or add the `T` or `Type` suffix (e.g., `SourceT`, `TargetType`).

#### Rationale & Instructor Notes

**Rationale:**
Standardized interface type parameter names ensure consistency between interface contracts and the classes that implement them.

**Instructor Note:**
Using standard type parameter names makes generic interface contracts intuitive and clear, regardless of the interface. These standard names include single uppercase letters (i.e., `T`, `E`, `K`, `V`) or `UpperCamelCase` names ending with `T` or `Type`.

### JavadocMethod

All methods, except the `main` method, must have **full** Javadoc documentation. This requires documenting every formal parameter with `@param`, the return value with `@return` (unless the return type is `void` or a constructor), and any declared checked or unchecked exceptions with `@throws`.

#### Valid Examples

```java
/**
 * Evaluates whether this list contains the specified element.
 *
 * @param target the object whose presence in this list is to be tested
 * @return {@code true} if this list contains the specified element; {@code false} otherwise
 * @throws NullPointerException if the specified element is {@code null} and this list
 *     does not permit null elements
 */
public boolean contains(String target) {
    // implementation details
    return false;
} // contains

/**
 * Main entry point for the test driver application. Javadoc on main is optional.
 *
 * @param args command-line arguments passed to the program
 */
public static void main(String[] args) {
    System.out.println("Driver running...");
} // main
```

#### Common Pitfalls & Invalid Examples

```java
/**
 * Computes the total course score.
 *                                          // Invalid: Missing @param tag for 'examScore'
 * @param labScore student score on laboratory assignments
 * @return the weighted total score
 */
public double calculateTotal(double labScore, double examScore) {
    return labScore + examScore;
} // calculateTotal
```

```java
/**
 * Finds a user by ID.
 *
 * @param id the user numeric identifier    // Invalid: Missing @return tag for non-void method
 */
public User getUser(int id) {
    return null;
} // getUser
```

#### How to Fix

- Ensure every parameter listed in the method signature has a corresponding `@param <paramName>` tag with an accurate description.
- For every non-`void` method, add a `@return` tag describing what value is produced and what special values (such as `null` or `-1`) signify.
- Ensure that if you document `@throws`, the exception type is specified and accompanied by a description of the condition that triggers it.

#### Rationale & Instructor Notes

**Rationale:**
Methods define the functional contract of an object. Comprehensive method documentation allows other programmers to use your methods correctly and safely without needing to inspect internal implementation code.

**Instructor Note:**
In CS2 projects, graders and automated test harnesses verify your Javadoc tags. If you rename a parameter in your method header, make sure you update the corresponding `@param` tag name in the Javadoc comment to match.

### JavadocParagraph

Paragraphs in Javadoc comments must be separated by an empty line followed by a `<p>` tag on its own line, immediately preceding the new paragraph text. There should not be a closing `</p>` tag.

#### Valid Examples

```java
/**
 * Loads configuration properties from the specified file path.
 *
 * <p>
 * This method parses key-value pairs stored in standard Java properties format.
 * If duplicate keys are encountered, the last value read replaces earlier values.
 *
 * <p>
 * File I/O operations are buffered for high performance.
 *
 * @param configPath path to the properties configuration file
 */
public void loadConfig(String configPath) {
    // load configuration
} // loadConfig
```

#### Common Pitfalls & Invalid Examples

```java
/**
 * Processes incoming network transactions.
 * <p> Transactions are validated against the fraud prevention service. // Invalid: missing blank line before <p>
 *
 * @param tx transaction object
 */
public void processTransaction(Transaction tx) {
    // process transaction
} // processTransaction
```

```java
/**
 * Encrypts student records.
 *
 * <p>Uses 256-bit AES encryption.</p>                                  // Invalid: closing </p> tag used
 *
 * @param data raw record data
 */
public void encrypt(byte[] data) {
    // encrypt data
} // encrypt
```

#### How to Fix

- Always place the `<p>` tag on its own separate line immediately before the second and subsequent paragraphs.
- Precede every line containing `<p>` with a blank Javadoc line (a line containing only ` *`).
- Do not use closing `</p>` tags in Javadoc comments.

#### Rationale & Instructor Notes

**Rationale:**
The standard Javadoc HTML generation tool converts comments into formatted HTML web pages. HTML rendering collapses multiple consecutive whitespace characters and newlines into a single space; the `<p>` tag tells the browser to create a visual paragraph break.

**Instructor Note:**
Many students try to separate paragraphs simply by hitting Enter twice in their Javadoc comments without adding `<p>`. When Javadoc generates the HTML documentation, those paragraphs will awkwardly merge into one long block of text.

### JavadocTagContinuationIndentation

When a Javadoc block tag description (such as for `@param`, `@return`, or `@throws`) wraps onto subsequent lines, the continuation line(s) must be indented at least **4 spaces** relative to the start of the tag line.

#### Valid Examples

```java
/**
 * Processes student enrollment and updates course registration records.
 *
 * @param studentName the full legal name of the student to look up
 *     in the departmental registration database
 * @param maxCredits maximum number of credit hours the student is
 *     authorized to enroll in for the specified term
 * @return the unique academic confirmation number assigned to the
 *     completed registration transaction
 * @throws IllegalArgumentException if the student name is null
 *     or consists only of whitespace
 */
public String enrollStudent(String studentName, int maxCredits) {
    // enrollment logic
    return "";
} // enrollStudent
```

#### Common Pitfalls & Invalid Examples

```java
/**
 * Retrieves course information.
 *
 * @param courseId unique four-digit departmental course identifier
 *   used for scheduling                                                // Invalid: indented only 2 spaces (must be >= 4)
 * @return the course catalog details
 */
public Course getCourse(int courseId) {
    return null;
} // getCourse
```

```java
/**
 * Parses user account input.
 *
 * @param rawInput raw string data
 * @throws ParseException
 * if parsing fails due to invalid format                              // Invalid: continuation line has 0-space indentation
 */
public Account parseAccount(String rawInput) throws ParseException {
    return null;
} // parseAccount
```

#### How to Fix

- When a `@param`, `@return`, or `@throws` description exceeds your editor line length and wraps to the next line, indent the continuation line with **4 spaces** after the leading ` * ` delimiter.

#### Rationale & Instructor Notes

**Rationale:**
Indenting tag continuation lines creates a clear visual distinction between where one tag's description ends and the next tag begins, preventing multi-line descriptions from looking like separate tags.

**Instructor Note:**
If you keep your tag descriptions concise, they will rarely need to wrap. When detailed explanations are necessary, ensure your continuation lines are indented by 4 spaces.

### LambdaParameterName

Parameter names declared in lambda expressions must be written in `lowerCamelCase` or declared as an unnamed parameter using a single underscore (`_`).

#### Valid Examples

```java
// Valid: lowerCamelCase lambda parameter
list.forEach(elementItem -> System.out.println(elementItem));

// Valid: Multiple lambda parameters in lowerCamelCase
Comparator<String> comp = (firstStr, secondStr) -> firstStr.compareTo(secondStr);

// Valid: Unnamed parameter for unused arguments (Java 22+)
map.forEach((key, _) -> System.out.println("Key: " + key));
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase starting letter
list.forEach(ElementItem -> System.out.println(ElementItem));

// Invalid: Snake_case with underscores
Comparator<String> comp = (first_str, second_str) -> first_str.compareTo(second_str);
```

#### How to Fix

- Ensure lambda parameters start with a lowercase letter and use `lowerCamelCase`.
- If a lambda parameter is unused, use the unnamed identifier `_`.

#### Rationale & Instructor Notes

**Rationale:**
Lambda parameters are local identifiers and must conform to the universal `lowerCamelCase` naming convention used for all Java parameters and local variables. When declaring lambda parameters, you should ensure that their names conform to the suggestions in the Java Language Specification, sections [15.27.1](https://docs.oracle.com/javase/specs/jls/se21/html/jls-15.html#jls-15.27.1), [6.8.6](https://docs.oracle.com/javase/specs/jls/se21/html/jls-6.html#jls-6.8.6), and [6.1](https://docs.oracle.com/javase/specs/jls/se21/html/jls-6.html#jls-6.1).

**Instructor Note:**
Choose meaningful lambda parameter names (e.g., `event -> ...` or `e -> ...`, `student -> ...`) for lambda parameters, and use unnamed parameters (`_`) for unused parameters.

### LeftCurly

Left curly braces (`{`) that open code blocks (classes, interfaces, records, methods, constructors, and control structures) must always be placed at the end of the line that introduces the block (also known as Egyptian style, the One True Brace Style (1TBS), or the Kernighan and Ritchie (K&R) style).

#### Valid Examples

```java
// Valid: Left curly brace at the end of the class header line
public class StudentManager {

    // Valid: Left curly brace at the end of the method header line
    public void processGrades(int[] scores) {
        // Valid: Left curly brace at the end of the 'if' condition line
        if (scores.length > 0) {
            System.out.println("Processing...");
        } // if
    } // processGrades

} // StudentManager
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Left curly brace on its own line (Allman / C++ style)
public class StudentManager
{
    public void processGrades(int[] scores)
    {
        if (scores.length > 0)
        {
            System.out.println("Processing...");
        } // if
    } // processGrades
} // StudentManager
```

#### How to Fix

- Move any opening curly brace `{` that appears at the start of a line to the end of the preceding line, separated by a single space.

#### Rationale & Instructor Notes

**Rationale:**
Placing the opening brace at the end of the declaration line is the standard convention in the Java programming language, used by Oracle, Google, and the wider Java open-source community. It saves vertical screen space while preserving clear block visual hierarchy.

**Instructor Note:**
Students transitioning from C++ or C# often bring with them the Allman style (brace on a new line). In Java and CSCI 1302, always place `{` at the end of the line.

### LineLength

Java source code lines must not exceed **100 characters** in length (including indentation and trailing whitespace).

Lines that would exceed this limit must be manually line-wrapped in a readable, consistent manner (using 4-space continuation indentation).

The only permitted exceptions are:

* Lines where obeying the column limit is impossible (e.g., a long URL in a Javadoc `@see` tag);
* `package` and `import` statements; and
* Command-line shell examples in Javadoc or code comments intended for copy-pasting.

#### Valid Examples

```java
// Valid: Long expression wrapped cleanly across lines (each under 100 characters)
String studentSummary = "Student: " + student.getFirstName() + " " + student.getLastName()
    + ", ID: " + student.getId()
    + ", Major: " + student.getMajor();

// Valid: Long method invocation wrapped with arguments on continuation lines
boolean isEnrolled = enrollmentService.registerStudentForCourse(
    studentId,
    courseCode,
    termIdentifier
);
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Exceeds 100 characters on a single line
String logMessage = "System encountered an unexpected processing error while evaluating student grade records for term " + currentTerm;
```

#### How to Fix

* Break long mathematical or boolean expressions before operators, wrapping the operator to the next line (see [`OperatorWrap`](#operatorwrap)).
* Break method calls after opening parentheses or commas between arguments, indenting continuation lines by 4 spaces.
* Break long string literals into concatenated sub-strings across multiple lines.

#### Rationale & Instructor Notes

**Rationale:**
Limiting lines to 100 characters prevents horizontal scrolling in code editors, side-by-side git diff tools, terminal displays, and split-window IDE layouts.

**Instructor Note:**
In modern IDEs (VS Code, Eclipse, IntelliJ, Emacs), you can configure a visual line guide at column 100 to alert you when a line is nearing the boundary.

### LocalVariableName

Local variable names (variables declared inside methods, constructors, or block scopes) must be written in `lowerCamelCase`.

#### Valid Examples

```java
public void processTransaction() {
    int studentCount = 10;
    String firstName = "Ada";
    boolean hasCompleted = false;
    double currentBalance = 150.75;
} // processTransaction
```

#### Common Pitfalls & Invalid Examples

```java
public void processTransaction() {
    int StudentCount = 10;     // Invalid: Starts with uppercase letter
    String first_name = "Ada"; // Invalid: Contains underscore
    double TOTAL = 100.0;      // Invalid: CONSTANT_CASE is not used for local variables
} // processTransaction
```

#### How to Fix

- Ensure local variables begin with a lowercase letter and use `lowerCamelCase` without underscores.
- Even if a local variable is declared `final`, it remains a local variable and must follow `lowerCamelCase` (do not use `CONSTANT_CASE` for local variables).

#### Rationale & Instructor Notes

**Rationale:**
Consistent local variable naming creates clean visual distinction from type names (`UpperCamelCase`) and constants (`CONSTANT_CASE`), reducing cognitive load while reading algorithms.

**Instructor Note:**
Choose descriptive names for your local variables rather than single-letter names, except for simple loop counters (`i`, `j`, `k`).

### MemberName

Non-static instance field names (member variables) must be written in `lowerCamelCase`.

#### Valid Examples

```java
public class Student {

    // Valid: lowerCamelCase instance variable names
    private String firstName;
    private String lastName;
    private int creditHours;
    private double gradePointAverage;

} // Student
```

#### Common Pitfalls & Invalid Examples

```java
public class Student {

    // Invalid: Uppercase starting letter
    private String FirstName;

    // Invalid: Snake_case with underscores
    private int credit_hours;

    // Invalid: Hungarian notation / leading prefix
    private String m_lastName;

} // Student
```

#### How to Fix

- Ensure instance fields start with a lowercase letter, use camelCase for subsequent words, and contain no underscores or prefix tags (such as `m_` or `s_`).

#### Rationale & Instructor Notes

**Rationale:**
Standardized field naming ensures that object attributes are easily readable and clearly distinguished from types and static constants.

**Instructor Note:**
Instance variables represent the internal state of an object. Keep names concise and self-descriptive in `lowerCamelCase`.

### MethodLength

The bodies of methods and constructors must not exceed **60 lines**.

This count includes the method header line with the opening curly brace `{`, all statements, comments, and blank lines within the method body, and the closing curly brace `}`. It does not include the method's preceding Javadoc comment block.

#### Valid Examples

```java
// Valid: Concise, focused method (well under 60 lines)
public double calculateTotalScore(double[] examScores, double labScore) {
    double total = 0.0;
    for (int i = 0; i < examScores.length; i++) {
        total += examScores[i];
    } // for
    double average = total / examScores.length;
    return (average * 0.7) + (labScore * 0.3);
} // calculateTotalScore
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Monolithic method exceeding 60 lines
public void processFullSemesterData(Scanner fileScanner) {
    // 65 lines of parsing, validation, database insertion, and report generation
} // processFullSemesterData
```

#### How to Fix

- Decompose monolithic methods into smaller, reusable private helper methods (functional decomposition).
- Extract repetitive logic into helper functions or loop constructs.
- Separate business logic from I/O parsing and UI formatting.

#### Rationale & Instructor Notes

**Rationale:**
Short, focused methods are easier to read, test, debug, and reason about. When a method exceeds 60 lines, it almost always violates the Single Responsibility Principle.

**Instructor Note:**
A good guideline is that an entire method should fit comfortably on your editor screen without scrolling. If a method is growing beyond 40-50 lines, start extracting helper methods.

### MethodName

Method names must be written in `lowerCamelCase`.

Method names are typically verbs or verb phrases that clearly describe the action performed (e.g., `calculateTotal`, `findById`, `isEmpty`, `printSummary`).

#### Valid Examples

```java
// Valid: lowerCamelCase method names
public double calculateAverage(int[] scores) {
    return 0.0;
} // calculateAverage

public boolean hasNext() {
    return false;
} // hasNext

public void printReport() {
} // printReport
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase starting letter (UpperCamelCase)
public double CalculateAverage(int[] scores) {
    return 0.0;
} // CalculateAverage
```

```java
// Invalid: Snake_case with underscores
public void print_report() {
} // print_report
```

#### How to Fix

- Start the method name with a lowercase letter and capitalize the first letter of each subsequent word without underscores.

#### Rationale & Instructor Notes

**Rationale:**
`lowerCamelCase` naming prevents methods from being visually confused with class constructors or type definitions.

**Instructor Note:**
Students coming from Python or C often write `calculate_average()` or from C# write `CalculateAverage()`. In Java, always use `calculateAverage()`.

### MethodParamPad

There must be no whitespace between a method, constructor, or annotation identifier and its opening parenthesis (`(`).

#### Valid Examples

```java
// Valid: Opening parenthesis directly adjacent to method name
public void calculateTotal(int count) {
    doSomething();
    String formatted = String.format("Count: %d", count);
} // calculateTotal
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Space before opening parenthesis in method declaration
public void calculateTotal (int count) {
    // Invalid: Space before opening parenthesis in method call
    doSomething ();
} // calculateTotal
```

#### How to Fix

- Remove the space between the method or constructor name and the opening parenthesis `(`.

#### Rationale & Instructor Notes

**Rationale:**
Placing `(` immediately adjacent to the identifier clearly distinguishes method calls and declarations from control flow statements (such as `if (...)` or `while (...)`), which *do* require a preceding space.

**Instructor Note:**
Rule of thumb: Keywords get a space before `(` (e.g. `if (x)`), but method names do NOT get a space (e.g. `foo(x)`).

### MethodTypeParameterName

Generic type parameter names for generic methods and constructors must conform to one of two formats:

1. A single uppercase letter optionally followed by a single digit (e.g., `T`, `E`, `K`, `V`, `T1`); or
2. An `UpperCamelCase` name ending with `T` or `Type` (e.g., `ResultT`, `ItemType`).

#### Valid Examples

```java
// Valid: Single uppercase letters on generic methods
public <T> T findFirst(List<T> list) {
    return list.isEmpty() ? null : list.get(0);
} // findFirst

// Valid: Descriptive names ending with T or Type
public <ResultT> ResultT executeQuery(String query, Class<ResultT> resultClass) {
    return null;
} // executeQuery
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Lowercase type parameter name
public <type> type getFirst(List<type> list) {
    return list.get(0);
} // getFirst

// Invalid: Multi-character name without T or Type suffix
public <Result> Result executeQuery(String query) {
    return null;
} // executeQuery
```

#### How to Fix

- Change method type parameters placed between `< >` before the return type to single uppercase letters (e.g., `<T>`) or `T`/`Type`-suffixed names (e.g., `<ResultT>`).

#### Rationale & Instructor Notes

**Rationale:**
Generic methods introduce scoped type variables. Conforming to the standard naming scheme ensures readers recognize that `<T>` denotes a generic type rather than a concrete return type.

**Instructor Note:**
In generic helper methods (e.g., sorting, searching, copying collections), `<T>` is universally understood.

### MissingJavadocMethod

All methods and constructors, except the `main` method, must have Javadoc documentation.

If a method is annotated with `@Override`, then it is assumed to have Javadoc documentation inherited from the method it is overriding. If an overriding method is not annotated with `@Override`, you must explicitly provide full Javadoc documentation to remain compliant.

#### Valid Examples

```java
/**
 * Calculates the total cost of all items in the shopping cart.
 *
 * @param taxRate the applicable decimal tax percentage
 * @return the total price including taxes
 */
public double calculateTotal(double taxRate) {
    // calculation logic
    return 0.0;
} // calculateTotal

/** {@inheritDoc} */
@Override
public String toString() {
    return "ShoppingCart instance";
} // toString

/**
 * Main entry point for testing. Javadoc is optional on the main method.
 *
 * @param args command-line arguments
 */
public static void main(String[] args) {
    System.out.println("Executing driver...");
} // main
```

When overriding a method from an external library or interface where source code is unavailable to the Javadoc tool, use:

```java
/**
 * Summary sentence.
 *
 * <p>
 * {@inheritDoc}
 */
@Override
public String toString() {
    return "StudentRecord";
} // toString
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Missing Javadoc documentation on helper method
private void initializeDatabase() {
    // database initialization
} // initializeDatabase
```

```java
// Invalid: Missing @Override annotation and missing Javadoc comment
public boolean equals(Object other) {
    return this == other;
} // equals
```

#### How to Fix

- Add a complete Javadoc block (`/** ... */`) above each method and constructor definition.
- Always annotate overridden methods with `@Override`. If you add a Javadoc comment to an overridden method, include `{@inheritDoc}`.
- Remember that `private` and `protected` helper methods also require Javadoc documentation in this style guide.

#### Rationale & Instructor Notes

**Rationale:**
Providing sufficiently detailed documentation makes code maintenance and bug identification much easier. It is critical for code that other developers will use without seeing the internal implementation.

**Instructor Note:**
Well-documented code is just as important as correctly working code. In fact, writing Javadoc *before* writing the method body is a proven technique known as **Test-Driven Development (TDD)**, used to clarify your algorithmic requirements before implementation.

### MissingJavadocType

All top-level and nested class, interface, record, enum, and annotation interface definitions must have Javadoc documentation summarizing their purpose and responsibility.

#### Valid Examples

```java
/**
 * Represents a student enrolled in a university course.
 *
 * <p>
 * This class tracks student demographic information, registered credit hours,
 * and academic standing.
 */
public class Student {
    // class members
} // Student

/**
 * Defines the contract for processing payments in the e-commerce system.
 */
public interface PaymentProcessor {
    // interface methods
} // PaymentProcessor

/**
 * Immutable record representing a two-dimensional geometric coordinate point.
 *
 * @param x the horizontal coordinate
 * @param y the vertical coordinate
 */
public record Point(double x, double y) {
} // Point

/**
 * Enumeration of available letter grade options for course evaluation.
 */
public enum Grade {
    A, B, C, D, F
} // Grade
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Missing Javadoc comment on class definition
public class GradeCalculator {
    // implementation
} // GradeCalculator
```

```java
// Single-line comments do not count as Javadoc
/* Block comments with one asterisk do not count as Javadoc either */
public class CourseScheduler {
    // implementation
} // CourseScheduler
```

#### How to Fix

- Add a Javadoc comment starting with `/**` (note the double asterisk) directly above the class, interface, record, or enum declaration.
- Provide at least one complete summary sentence ending with a period describing what the type represents.

#### Rationale & Instructor Notes

**Rationale:**
Type documentation provides essential high-level context about architecture, responsibilities, invariants, and intended usage. It is the primary overview prospective users of your library read first.

**Instructor Note:**
In CS2, every `.java` file you submit must include a class-level Javadoc comment. Make sure your opening comment starts with `/**` and not `/*` or `//`.

### ModifierOrder

When applying multiple modifier keywords to a class, field, constructor, or method, they must appear in the canonical order specified by the Java Language Specification, sections [8.1.1, 8.3.1, 8.4.3](https://docs.oracle.com/javase/specs/jls/se21/html/jls-8.html#jls-8.1.1), and [9.4](https://docs.oracle.com/javase/specs/jls/se21/html/jls-9.html#jls-9.4):

```java
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

#### Valid Examples

```java
// Valid: Correct canonical modifier ordering
public static final int MAX_LIMIT = 100;

public static void main(String[] args) {
} // main

protected abstract void processRecord();

private synchronized void updateState() {
} // updateState
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: 'final' before 'public static'
final public static int MAX_LIMIT = 100;

// Invalid: 'static' before 'public'
static public void main(String[] args) {
} // main

// Invalid: 'synchronized' before 'private'
synchronized private void updateState() {
} // updateState
```

#### How to Fix

- Reorder modifiers so visibility (`public`, `protected`, `private`) comes first, followed by `abstract` / `static`, followed by `final`, followed by concurrency/system modifiers (`synchronized`, `volatile`, etc.).

#### Rationale & Instructor Notes

**Rationale:**
Standard modifier ordering creates visual consistency across classes and libraries, making it easy for readers to quickly ascertain visibility and mutability.

**Instructor Note:**
Always remember: Visibility first (`public static final`), never `final static public`.

### MultipleVariableDeclarations

Each variable must be declared in its own separate statement on a distinct line. Declaring multiple variables in a single comma-separated statement is disallowed.

#### Valid Examples

```java
// Valid: Separate declaration statements on distinct lines
int count = 0;
int total = 0;
String studentName = "";
String courseId = "";
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Comma-separated variable declarations
int count = 0, total = 0;
```

```java
// Invalid: Comma-separated uninitialized declarations
double width, height, length;
```

#### How to Fix

- Split comma-separated declarations into separate statements, declaring the type on each line:

  ```java
  double width = 0.0;
  double height = 0.0;
  double length = 0.0;
  ```

#### Rationale & Instructor Notes

**Rationale:**
Declaring one variable per statement allows each variable to be documented independently, makes initial values explicit, and prevents common Java bugs where modifiers or type properties (such as array brackets or pointer-like semantics) are mistakenly assumed to apply to all variables in the list.

**Instructor Note:**
  Declaring one variable per line makes it much easier to track variable lifecycles, add inline comments, and refactor code without disturbing adjacent declarations.

### NeedBraces

Curly braces are required for all control flow statements (`if`, `else`, `for`, `do`, `while`, and `switch`), even when the body contains only a single statement or is empty.

#### Valid Examples

```java
// Valid: Single-statement 'if' with curly braces and closing comment
if (score >= 90) {
    grade = "A";
} // if

// Valid: 'for' loop with braces
for (int i = 0; i < items.length; i++) {
    System.out.println(items[i]);
} // for

// Valid: 'while' loop with braces
while (scanner.hasNextLine()) {
    processLine(scanner.nextLine());
} // while
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Missing curly braces around single-line 'if' body
if (score >= 90)
    grade = "A";
```

```java
// Invalid: Missing braces on 'while' loop
while (hasMoreTokens())
    nextToken();
```

#### How to Fix

- Always wrap the body of `if`, `else`, `for`, `do`, and `while` statements in curly braces `{ ... }`, placing the opening brace on the same line as the conditional header.
- Add an end-of-block trailing comment after the closing curly brace indicating the control construct (e.g., `} // if`, `} // for`, `} // while`).

#### Rationale & Instructor Notes

**Rationale:**
In Java, omitting curly braces causes only the immediately following single statement to be bound to the conditional. Adding a second statement later without adding braces creates a notorious logic bug ("dangling else" or unconditioned execution) that is often invisible at a glance.

**Instructor Note:**
One of the most frequent bugs in introductory and intermediate programming occurs when a student adds a `System.out.println(...)` or cleanup step under an unbraced `if` statement, expecting it to run conditionally. Always using curly braces prevents this entire class of bugs.

### NonEmptyAtclauseDescription

Every Javadoc block tag (such as `@param`, `@return`, and `@throws`) must include a meaningful, non-empty description.

#### Valid Examples

```java
/**
 * Searches for a student record by its unique academic identifier.
 *
 * @param studentId the unique integer identifier assigned to the student
 * @return the matching {@code Student} instance, or {@code null} if no match is found
 * @throws NoSuchElementException if no student matching {@code studentId} exists
 */
public Student findById(int studentId) {
    // lookup implementation
    return null;
} // findById
```

#### Common Pitfalls & Invalid Examples

```java
/**
 * Searches for a student record.
 *
 * @param studentId                             // Invalid: empty description for @param
 * @return                                      // Invalid: empty description for @return
 * @throws NoSuchElementException               // Invalid: empty description for @throws
 */
public Student findById(int studentId) {
    return null;
} // findById
```

```java
/**
 * Calculates grade average.
 *
 * @param scores scores                         // Pitfall: trivial placeholder duplicating tag name
 * @return result                               // Pitfall: lacks descriptive value
 */
public double calculateAverage(double[] scores) {
    return 0.0;
} // calculateAverage
```

#### How to Fix

- Ensure every `@param`, `@return`, and `@throws` tag is followed by at least one descriptive word explaining what the parameter is, what the method returns, or under what specific condition the exception is thrown.
- Avoid simply repeating the parameter name; explain what value the parameter represents and any constraints on its value.

#### Rationale & Instructor Notes

**Rationale:**
A Javadoc tag with an empty or redundant description provides no documentation beyond what is already visible in the method header. Clear descriptions convey expectations, constraints, and side effects.

**Instructor Note:**
Good documentation answers "what" and "why", not just "what type". For example, for `@return`, write `@return the total count of active enrollments` rather than `@return int`.

### OneStatementPerLine

Each Java statement must be placed on its own line. Combining multiple statements on a single line using semicolons is prohibited.

This rule applies to variable declarations, assignments, method invocations, loop constructs, `break`, `continue`, and `return` statements.

#### Valid Examples

```java
// Valid: Each statement on its own line
int count = 0;
count++;
System.out.println(count);
return count;
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Multiple assignment and print statements on a single line
int count = 0; count++; System.out.println(count);
```

```java
// Invalid: Placing 'if' condition and body statement on the same line
if (isDone) return;
```

```java
// Invalid: Multiple variable declarations on one line
int x = 10; int y = 20;
```

#### How to Fix

- Split combined statements across multiple lines, terminating each statement with a newline following the semicolon.
- Wrap single-line `if` statements with curly braces on multiple lines (as required by [`NeedBraces`](#needbraces) and [`LeftCurly`](#leftcurly)).

#### Rationale & Instructor Notes

**Rationale:**
Single-statement lines improve code readability, simplify visual code reviews, make git diffs precise, and ensure that debugger breakpoints can be placed accurately on individual operations.

**Instructor Note:**
In Java, statements are the fundamental unit of execution. Placing one statement per line keeps your code clean and easy to step through line-by-line in a debugger.

### OneTopLevelClass

Each top-level class, interface, record, or enum must reside in its own dedicated `.java` source file. Having multiple top-level type declarations within a single source file is prohibited.

#### Valid Examples

File: `StudentRecord.java`:

```java
// Valid: Single top-level record definition in StudentRecord.java
public record StudentRecord(String name, int id) {
} // StudentRecord
```

File: `GradeCalculator.java`:

```java
// Valid: Single top-level class definition in GradeCalculator.java
public class GradeCalculator {
    // class members
} // GradeCalculator
```

#### Common Pitfalls & Invalid Examples

File: `DataStructures.java`

```java
// Invalid: Multiple top-level classes in a single source file
public class DataStructures {
    ...
} // DataStructures

class HelperNode { // Invalid: Second top-level class in the same file
    ...
} // HelperNode
```

#### How to Fix

- Move each top-level class, record, interface, or enum into its own separate `.java` file whose name matches the type name.
- If a helper class is only used internally by one class, consider making it a `private static` nested class inside the enclosing class.

#### Rationale & Instructor Notes

**Rationale:**
Placing one top-level type per file aligns with Java compiler lookup rules, ensures that class files are easily discoverable in the filesystem, and prevents compilation issues when building with build tools.

**Instructor Note:**
Never declare two non-nested classes in one `.java` file. Create a separate `.java` file for every top-level class.

### OperatorWrap

When an expression wraps across multiple lines at an operator (e.g., `+`, `-`, `*`, `/`, `&&`, `||`, `==`, `!=`, `:`, or `::`), the operator must wrap to the **new line** (appearing at the beginning of the continuation line).

#### Valid Examples

```java
// Valid: Arithmetic operator wraps to start of continuation line
int total = value1 + value2
    + value3 + value4;

// Valid: String concatenation operator on continuation line
String message = "Header: "
    + "detail one, "
    + "detail two";

// Valid: Logical boolean operators on continuation lines
boolean isValid = hasValidId
    && isRegistered
    && !isSuspended;

// Valid: Method reference operator wraps to new line
Function<String, Integer> parser = Integer
    ::parseInt;
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Operator placed at the end of the previous line
int total = value1 + value2 +
    value3 + value4;

// Invalid: Trailing boolean operator
boolean isValid = hasValidId &&
    isRegistered &&
    !isSuspended;
```

#### How to Fix

- Move any operator at the end of a wrapped line to the beginning of the next continuation line, indented by 4 spaces.

#### Rationale & Instructor Notes

**Rationale:**
Placing operators at the beginning of continuation lines makes it immediately visually apparent that the line is continuing an ongoing expression rather than starting a new statement.

**Instructor Note:**
When splitting long `if` condition expressions across multiple lines, always place `&&` or `||` at the start of the next line.

### OuterTypeFilename

In any `.java` source file, the filename must exactly match the name of the outer top-level class, interface, record, or enum, including matching case.

#### Valid Examples

```java
// In file: src/cs1302/utility/MathOps.java
package cs1302.utility;

public class MathOps {
    ...
} // MathOps
```

#### Common Pitfalls & Invalid Examples

```java
// In file: src/cs1302/utility/mathops.java (all lowercase filename)
package cs1302.utility;

public class MathOps { // Invalid: Filename 'mathops.java' does not match 'MathOps'
    ...
} // MathOps
```

```java
// In file: src/cs1302/utility/Utilities.java
package cs1302.utility;

public class MathOps { // Invalid: Filename 'Utilities.java' does not match 'MathOps'
    ...
} // MathOps
```

#### How to Fix

- Rename the file on disk so that its basename exactly matches the declared public outer type name, respecting case sensitivity (e.g., rename `student.java` to `Student.java`).

#### Rationale & Instructor Notes

**Rationale:**
The Java compiler and classloader locate compiled types by matching fully qualified class names to filesystem directory and file names. Matching filenames prevent compilation failures on case-sensitive operating systems (such as Linux).

**Instructor Note:**
On macOS and Windows, filesystems are often case-insensitive, so `mathops.java` might compile locally, but fail when submitted to Linux-based grading servers (such as Odin). Always match casing exactly!

### PackageName

Package names must be written exclusively in lowercase ASCII letters and digits, with subpackages separated by a single period (`.`). Each package segment must begin with a lowercase letter and cannot start with a digit. Package names must not contain uppercase letters, underscores, or hyphens.

#### Valid Examples

```java
// Valid: All-lowercase dot-separated package declarations
package cs1302;
package cs1302.utility;
package cs1302.game;
package edu.uga.cs1302.collections;
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase letter in package segment
package cs1302.MyExample;
```

```java
// Invalid: Underscore in package segment
package cs1302_example;
```

```java
// Invalid: Hyphen in package segment
package cs1302-game;
```

#### How to Fix

- Convert all package identifier segments to lowercase letters.
- Ensure the directory hierarchy in your `src/` folder mirrors the exact package name in all-lowercase (e.g., `src/cs1302/utility/MathOps.java`).

#### Rationale & Instructor Notes

**Rationale:**
Lowercase package names prevent naming collisions with type names and ensure portability across different filesystems (e.g., case-sensitive Linux filesystems vs. case-insensitive macOS/Windows filesystems).

**Instructor Note:**
In CSCI 1302 projects, standard packages usually follow `cs1302.<projectname>` (e.g., `cs1302.gallery` or `cs1302.list`). Always use all-lowercase folder and package names.

### ParameterName

Method and constructor formal parameter names must be written in `lowerCamelCase`.

#### Valid Examples

```java
// Valid: lowerCamelCase formal parameters
public void setScore(int finalScore, String studentName) {
    // parameter assignment
} // setScore

public Course(String coursePrefix, int courseNumber) {
    // constructor initialization
} // Course
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase starting letter
public void setScore(int FinalScore, String studentName) {
} // setScore
```

```java
// Invalid: Snake_case with underscores
public void setScore(int finalScore, String student_name) {
} // setScore
```

#### How to Fix

- Ensure every formal parameter identifier begins with a lowercase letter and uses `lowerCamelCase` without underscores.
- Update any matching `@param` tags in your method Javadoc comments to reflect the corrected parameter name.

#### Rationale & Instructor Notes

**Rationale:**
Consistent parameter naming ensures clarity in API signatures, IDE auto-completion hints, and generated Javadoc pages across the entire codebase.

**Instructor Note:**
Parameter names should clearly communicate what information the method expects. Avoid vague single-letter names (like `x`, `y`, `s`) when a meaningful noun (like `targetElement`, `filePath`, `studentName`) clarifies the method's purpose.

### ParenPad

There must be no whitespace immediately following an opening parenthesis (`(`) or immediately preceding a closing parenthesis (`)`) in method calls, constructor calls, control flow expressions (`if`, `for`, `while`, `switch`), and type casts.

#### Valid Examples

```java
// Valid: No internal padding inside parentheses
if (score > 0) {
    String formatted = (String) rawObject;
    printReport(formatted, count);
} // if
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Space immediately following '(' and preceding ')'
if ( score > 0 ) {
    String formatted = ( String ) rawObject;
    printReport( formatted, count );
} // if
```

#### How to Fix

- Remove spaces directly adjacent to the inside of parentheses: write `(x)` instead of `( x )`.

#### Rationale & Instructor Notes

**Rationale:**
Internal padding inside parentheses adds unnecessary horizontal spacing and disrupts the visual grouping of expressions.

**Instructor Note:**
Keep spaces *outside* parentheses after keywords (e.g. `if (...)`), but keep the inside snug (`(condition)`).

### PatternVariableName

Pattern variable names introduced in `instanceof` pattern matching or switch pattern matching must be written in `lowerCamelCase` or declared as an unnamed pattern variable using a single underscore (`_`).

#### Valid Examples

```java
// Valid: lowerCamelCase pattern variable in instanceof
if (obj instanceof String stringVal) {
    System.out.println(stringVal.length());
} // if

// Valid: Unnamed pattern variable when the matched instance is unused
if (obj instanceof String _) {
    System.out.println("Object is a string instance");
} // if

// Valid: Pattern matching in switch expressions
String description = switch (shape) {
    case Circle circleShape -> "Circle with radius " + circleShape.radius();
    case Rectangle rectShape -> "Rectangle with area " + (rectShape.width() * rectShape.height());
    default -> "Unknown shape";
};
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase starting letter
if (obj instanceof String StringVal) {
    System.out.println(StringVal);
} // if

// Invalid: Snake_case with underscores
if (obj instanceof String string_val) {
    System.out.println(string_val);
} // if
```

#### How to Fix

- Ensure pattern variables use standard `lowerCamelCase`.
- If the pattern variable is not used inside the matching block, declare it as an unnamed pattern variable `_` (Java 22+).

#### Rationale & Instructor Notes

**Rationale:**
Pattern variables act as scoped local variables. Following `lowerCamelCase` maintains uniformity across all variable declarations in Java.

**Instructor Note:**
Pattern matching for `instanceof` (Java 16+) and `switch` (Java 21+) simplifies type casting. When you only need to verify a type without using the casted reference, the unnamed variable `_` makes your intention explicitly clear.

### RecordComponentName

Record component names declared in Java record headers must be written in `lowerCamelCase`.

#### Valid Examples

```java
// Valid: Record components in lowerCamelCase
public record StudentRecord(String firstName, String lastName, int studentId) {
    ...
} // StudentRecord

public record CourseEnrollment(String courseCode, int sectionNumber, boolean isWaitlisted) {
    ...
} // CourseEnrollment
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Uppercase start and underscore
public record StudentRecord(String FirstName, int student_id) {
} // StudentRecord
```

#### How to Fix

- Write all record components in `lowerCamelCase` without underscores.
- If you document record components in the class Javadoc with `@param`, ensure the `@param` tag names match the component names.

#### Rationale & Instructor Notes

**Rationale:**
In Java records, each record component automatically generates a `private final` instance field and a `public` method with the exact same name as the component (e.g., `firstName()`). Naming components in `lowerCamelCase` guarantees that these generated methods follow Java naming conventions.

**Instructor Note:**
Java records are a modern language feature (standard since Java 16) for creating transparent, immutable data carriers. Always name the components using `lowerCamelCase`.

### RecordTypeParameterName

Generic type parameter names for generic records must conform to one of two formats:

1. A single uppercase letter optionally followed by a single digit (e.g., `T`, `E`, `K`, `V`, `T1`); or
2. An `UpperCamelCase` name ending with `T` or `Type` (e.g., `ItemT`, `KeyType`, `ValueType`).

#### Valid Examples

```java
// Valid: Single uppercase generic type parameters
public record Pair<K, V>(K key, V value) {
    ...
} // Pair

// Valid: Descriptive names ending with T or Type
public record ResultHolder<DataT, ErrorType>(DataT data, ErrorType error) {
    ...
} // ResultHolder
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Lowercase type parameter names
public record Pair<key, value>(key k, value v) { }

// Invalid: Multi-character names without trailing T or Type
public record Entry<Key, Value>(Key k, Value v) { }
```

#### How to Fix

- Rename generic parameters declared on the record header to single uppercase letters (e.g., `<K, V>`) or suffix multi-character names with `T` or `Type` (e.g., `<KeyType, ValueType>`).

#### Rationale & Instructor Notes

**Rationale:**
Generic records serve as lightweight data carriers. Adhering to the type parameter naming convention keeps record headers clean and prevents type parameters from shadowing or resembling concrete classes.

**Instructor Note:**
When creating generic records (like key-value pairs or tuples), use `<K, V>` or `<T, U>`.

### RightCurly

Right curly braces (`}`) for single-part code blocks must appear on their own separate line, aligned with the start of the statement that opened the block.

For multi-block statements (such as `if`/`else if`/`else`, `try`/`catch`/`finally`, and `do`/`while`), the right curly brace must appear on the same line as the keyword that begins the next block (e.g., `} else {`, `} catch (...) {`, `} finally {`, `} while (...);`).

#### Valid Examples

```java
// Valid: Single block right curly brace on its own line
if (isValid) {
    process();
} // if

// Valid: Multi-block statements with right curly on the same line as next keyword
if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else {
    grade = "C";
} // if

// Valid: try-catch-finally multi-block alignment
try {
    readFile(filename);
} catch (IOException ioe) {
    handleError(ioe);
} finally {
    cleanup();
} // try

// Valid: do-while loop
do {
    count++;
} while (count < 10);
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Right curly brace separated from 'else' onto a different line
if (score >= 90) {
    grade = "A";
}
else {
    grade = "B";
} // if
```

```java
// Invalid: Right curly brace separated from 'catch'
try {
    readFile(filename);
}
catch (IOException ioe) {
    handleError(ioe);
} // try
```

#### How to Fix

- In `if-else` chains, place `} else {` and `} else if (...) {` on a single continuous line.
- In `try-catch-finally` constructs, place `} catch (...) {` and `} finally {` on the same line as the closing brace of the preceding block.
- In `do-while` loops, place `} while (...);` on the same line as the closing brace.

#### Rationale & Instructor Notes

**Rationale:**
Keeping related control flow clauses on the same line visually unifies the multi-part structure into a cohesive compound statement rather than disjoint blocks.

**Instructor Note:**
In CSCI 1302, it is customary, but not required, to place closing block comments (e.g., `} // if` or `} // try`) just after a final closing brace for a block to help with debugging and understanding the code. The comment should match the keyword that opens the block, and should be indented to align with the opening keyword for the block. This note applies to single-block and multi-block control flow structures alike.

### StaticVariableName

Static non-final field names (i.e., the names of static variables that are not final) must be written in `lowerCamelCase`.

#### Valid Examples

```java
public class Counter {

    // Valid: static mutable variables in lowerCamelCase
    private static int instanceCount = 0;
    private static String globalEnvironment = "production";

} // Counter
```

#### Common Pitfalls & Invalid Examples

```java
public class Counter {

    // Invalid: CONSTANT_CASE on non-final static variable
    private static int INSTANCE_COUNT = 0;

    // Invalid: Snake_case with underscores
    private static int instance_count = 0;

    // Invalid: UpperCamelCase
    private static int InstanceCount = 0;

} // Counter
```

#### How to Fix

- If a static variable is intended to be mutable and shared across instances, name it in `lowerCamelCase`.
- If a static variable was intended to be an immutable constant, add the `final` modifier and use `CONSTANT_CASE` as required by [`ConstantName`](#constantname).

#### Rationale & Instructor Notes

**Rationale:**
Static non-final fields represent mutable class state. Naming them in `lowerCamelCase` prevents them from being mistaken for compile-time constants.

**Instructor Note:**
Mutable static variables should be used sparingly. When they are used (such as for object ID generators or instance counters), ensure they follow `lowerCamelCase`.

### SummaryJavadoc

The first sentence of every Javadoc comment is its [summary sentence](https://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#firstsentence). It must be present, grammatically complete, and end with a period (`.`).

The only exception to this rule is when the first tag in the comment is `{@inheritDoc}`.

#### Valid Examples

```java
/**
 * Calculates the Euclidean distance between two coordinate points.
 *
 * @param p1 the starting coordinate point
 * @param p2 the ending coordinate point
 * @return the straight-line distance between {@code p1} and {@code p2}
 */
public double distance(Point p1, Point p2) {
    // calculation logic
    return 0.0;
} // distance

/** {@inheritDoc} */
@Override
public int hashCode() {
    return 42;
} // hashCode
```

#### Common Pitfalls & Invalid Examples

```java
/**
 * Calculates the Euclidean distance between points  // Invalid: Missing ending period
 *
 * @param p1 point one
 * @param p2 point two
 * @return distance
 */
public double distance(Point p1, Point p2) {
    return 0.0;
} // distance
```

```java
/**
 *                                                  // Invalid: Missing summary sentence completely
 * @return the maximum allowed value
 */
public int getMaxValue() {
    return 100;
} // getMaxValue
```

#### How to Fix

- Ensure the very first line of text in your Javadoc comment clearly summarizes the method or class, and end that sentence with a period (`.`).
- Avoid leading blank lines before the summary sentence.

#### Rationale & Instructor Notes

**Rationale:**
The Javadoc tool extracts the first sentence of each comment to populate the summary table at the top of generated API documentation. A missing or unpunctuated first sentence results in malformed or incomplete summary tables.

**Instructor Note:**
In English grammar and standard Javadoc style, summary sentences start with a capital letter and end with a period. In Java API documentation, it is conventional to write summary sentences in third-person declarative form (e.g., "Returns the element..." or "Calculates the total...").

### TypeName

Type names for classes, interfaces, records, enums, and annotation interfaces must be written in `UpperCamelCase` (PascalCase).

Such type names are typically nouns or noun phrases (e.g., `StudentRecord`, `LinkedList`, `GradeCalculator`). Interface names may also be nouns (e.g., `List`, `Map`) or adjectives describing capabilities (e.g., `Comparable`, `Readable`, `Iterable`).

#### Valid Examples

```java
// Valid: Classes and records in UpperCamelCase
public class GradeCalculator {
} // GradeCalculator

public record StudentRecord(String id, String name) {
} // StudentRecord

// Valid: Interfaces in UpperCamelCase
public interface DataFilter {
} // DataFilter

// Valid: Enums in UpperCamelCase
public enum Semester {
    FALL, SPRING, SUMMER
} // Semester
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Lowercase starting letter
public class gradeCalculator {
} // gradeCalculator
```

```java
// Invalid: Snake_case with underscores
public class Student_Record {
} // Student_Record
```

#### How to Fix

- Capitalize the first letter of each word in the type name and remove all underscores.
- Rename the `.java` file so that its filename exactly matches the public type name (as required by [`OuterTypeFilename`](#outertypefilename)).

#### Rationale & Instructor Notes

**Rationale:**
The `UpperCamelCase` convention immediately distinguishes type names from variables and methods (`lowerCamelCase`) and constants (`CONSTANT_CASE`), enabling developers to understand identifier roles instantly when scanning code.

**Instructor Note:**
In Java, naming a class `student` or `student_record` will cause Checkstyle errors. Remember to use `Student` or `StudentRecord`.

### WhitespaceAround

Operators, control keywords, and braces must be surrounded by appropriate whitespace.

Specifically:

* Binary and ternary operators (`+`, `-`, `*`, `/`, `=`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `&&`, `||`, `?`, `:`) must have a space on both sides.
* Control keywords (`if`, `for`, `while`, `switch`, `catch`, `synchronized`) must be followed by a space before the opening parenthesis `(`.
* Left curly braces `{` must be preceded by a space.
* Right curly braces `}` must be followed by a space when followed by keywords like `else`, `catch`, `finally`, or `while`.

Empty compact blocks (such as empty method, constructor, or interface declarations: `{}`) are exempt from requiring internal spaces.

#### Valid Examples

```java
// Valid: Spaces around operators, after keywords, and before braces
if (n == 0) {
    total = count + 1;
} else {
    total = count - 1;
} // if

while (n > 0) {
    n--;
} // while
```

#### Common Pitfalls & Invalid Examples

```java
// Invalid: Missing space around equality operator '=='
if (n==0) {
    ...
} // if

// Invalid: Missing space between 'while' and '('
while(n > 0) {
    ...
} // while

// Invalid: Missing space before opening brace '{'
if (n == 0){
    ...
} // if
```

#### How to Fix

* Insert a single space on each side of binary operators (e.g. `a + b`, `x = y`, `score >= 90`).

* Insert a single space between control flow keywords and parentheses (e.g. `if (...)`, `for (...)`).

#### Rationale & Instructor Notes

**Rationale:**
Adequate whitespace around tokens prevents visual crowding, making expressions,
assignments, and control structures much easier to read and parse.

**Instructor Note:**
A common mistake in beginner code is jamming expressions together (e.g.,
`for(int i=0;i<10;i++)`). Use proper spacing: `for (int i = 0; i < 10; i++)`.

## References

* <a id="ref-google-javaguide"/>Diamond, M. ([@dimo414](https://github.com/dimo414)). 2016. *Google Java Style Guide.* URL: <https://google.github.io/styleguide/javaguide.html>
* <a id="ref-tpop"/>Kernighan, B.W. and Pike, R. 1999. *The Practice of Programming.* Addison-Wesley Professional. ISBN: 9780133133448.

## Publication History

| DOI | Tag | Date | Description |
| ----- | ----- | ------ | ------------- |
| [10.5281/zenodo.3370471](https://doi.org/10.5281/zenodo.3370471) | NA | NA | All Versions |
| [10.5281/zenodo.21986989](https://doi.org/10.5281/zenodo.21986989) | `v2026su` | Aug 17, 2026 | Summer 2026 |
| [10.5281/zenodo.18100593](https://doi.org/10.5281/zenodo.18100593) | `v2025fa` | Dec 30, 2025 | Fall 2025 |
| [10.5281/zenodo.3579521](https://doi.org/10.5281/zenodo.3579521) | `v2019fa` | Dec 16, 2019 | Fall 2019 |
| [10.5281/zenodo.3370472](https://doi.org/10.5281/zenodo.3370472) | `v2019su` | Aug 18, 2019 | Summer 2019 |

<hr/>

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc/4.0/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3370471.svg)](https://doi.org/10.5281/zenodo.3370471)

<small>
Copyright &copy; Michael E. Cotterell, Bradley J. Barnes, and the University of Georgia.
This work is licensed under
a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
The content and opinions expressed on this Web page do not necessarily reflect the views of, nor are they endorsed by, the University of Georgia or the University System of Georgia.
</small>
