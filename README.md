# CSCI 1302 Code Style Guide

![Approved for: Spring 2023](https://img.shields.io/badge/Approved%20for-Spring%202023-magenta)

Make sure you read through this document carefully. **It addition to describing why
code style is important and what the code style guidelines are for CSCI 1302, it also
describes how to use the `check1302` program on `odin` to check your code code as well
as Emacs and Vi configurations that, if used, will reduce the number of style issues
you have in your code moving forward.**

## Table of Contents

* [Compliance](#compliance)
* [Motivation](#motivation)
* [When and How to Check](#when-and-how-to-check)
   * [When to Check](#when-to-check)
   * [Run Checkstyle](#run-checkstyle)
   * [Multiple Files](#multiple-files)
   * [Output Examples](#output-examples)
* [Recommended Emacs Configurations](#recommended-emacs-configurations)
   * [Additional Emacs Configurations](#additional-emacs-configurations)
      * [Automatically Update Emacs Packages](#automatically-update-emacs-packages)
      * [Show Style Guide Violations in the Editor](#show-style-guide-violations-in-the-editor)
* [Recommended Vi Configurations](#recommended-vi-configurations)
* [Specific Guidelines](#specific-guidelines)
   * [ArrayTypeStyle](#arraytypestyle)
   * [ConstantName](#constantname)
   * [EmptyBlock](#emptyblock)
   * [EmptyCatchBlock](#emptycatchblock)
   * [EmptyLineSeparator](#emptylineseparator)
   * [FileTabCharacter](#filetabcharacter)
   * [Indentation](#indentation)
   * [JavadocMethod](#javadocmethod)
   * [LeftCurly](#leftcurly)
   * [LineLength](#linelength)
   * [MemberName](#membername)
   * [MethodName](#methodname)
   * [MethodLength](#methodlength)
   * [MissingJavadocMethod](#missingjavadocmethod)
   * [MissingJavadocType](#missingjavadoctype)
   * [ModifierOrder](#modifierorder)
   * [NeedBraces](#needbraces)
   * [OneStatementPerLine](#onestatementperline)
   * [OneTopLevelClass](#onetoplevelclass)
   * [OuterTypeFilename](#outertypefilename)
   * [RightCurly](#rightcurly)
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
"check1302 audit" are be used to remind you to check your code for compliance
with this style guide.

We also recognize that the terminal-based text editors used in this course are
new for many students. That is why we include recommendations for how to configure
those editors to help you stay in compliance. These recommendations will not
fix all code style violations, but they should help you avoid writing code that
violates some of the guidelines that are annoying to spot by hand and even more
annoying to fix.

Finally, we also include information about how to use the `check1302` program
on `odin` to check your code for compliance. This is the same tool that graders
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

In the preface to *The Practice of Programming* [[TPOP](#ref-tpop)] by
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
> style--the *practice* of programming--are not usually the focus of
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
  This saves real world time when it comes to fixing problems in your code.

* It is easier to extend and/or incorporate into other projects. This results in your
  code being more useful to others as well as your future self.

The list could go on. The important thing to remember is that **quality not only
refers to the output of a program but also its effect on the people who interact
with the code**. Rarely, in practice, are you the only one who will read and use
your code. If you're a software engineer, then it is very likely that *many*
people will interact your code over time and that you will interact with *lots*
of code written by others as well.

## When and How to Check

Here is a fair and honest warning: if you wait until you are nearly done
writing some code before checking its style, then do not be surprised if
you significantly increases the overall amount of time you need
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
fewer and fewer violations. This happens because you start to write code
code in good style. It's a pretty neat way to learn.

If you don't check your code for compliance early and often, then not only
are you dooming yourself to the miserable time sink of "not fun" activities
described earlier, you are actively avoiding learning.

### Run Checkstyle

To check your Java source code for compliance, you can use a custom version
of the Checkstyle program on `odin` called `check1302`. **This program is
only guaranteed to work if your code compiles**, so if you encounter a
crash, then check to make sure your code compiles before proclaiming
defeat.

To run the `check1302` program on an individual file, say `src/cs1302/Test.java`,
you can execute the command below:

```
$ check1302 src/cs1302/Test.java
```

In the program output, any warnings that appear relate directly
to style guidelines presented elsewhere in this document. For example:

```
[ERROR] src/cs1302/Test.java:2: Missing a Javadoc comment. [MissingJavadocType]
```

Here, we see that the [`MissingJavadocType`](#missingjavadoctype) guideline was
not met on line `2` in `src/cs1302/Test.java`. The output even gives a short
description of what it thinks is wrong. If the short description is not sufficient
to determine what the issue is, then you should consult the section for that
guideline [here](#specific-guidelines) for more information.

To avoid needless
scrolling, we recommend using the table of contents near the beginning of this
style guide or your browser's "find text" feature whenever you want to find
the section for a specific guideline.

### Multiple Files

You might want to check all the files in some `src` directory. To do this, you can
pass the entire directory to `check1302` as in the following command:

```
$ check1302 src
```

### Output Examples

Here is some example output for an **invalid file**:

```
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

```
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
`.emacs.txt`). If you do not have a `~/.emacs` file, then check to to see
if either `~/.emacs.el` or `~/.emacs.d/init.el` exist; if so, then use one
of those files instead. If none of these files exist, then we recommend that
you create `~/.emacs` and store your configuration settings there.

Let's assume that you want to store your settings in `~/.emacs`.
You can open that file with Emacs, even if it does not yet exist -- it
will get created when you save. Once open, add the lines we present below
to the end of the file (could be the top if it's empty), then save the
file and exit Emacs. If you did this correctly, then the settings will
take effect the next time you launch Emacs. One quick way to see if you
got it working is to open a `.java` in Emacs and see if it shows line
numbers; if so, then you should be good to go!

**If you do not understand what file you need to create or edit,
then please ask your instructor or a TA!**

Below are the lines you should add to your configuration file. We recommend copying
and pasting the text below into your `~/.emacs` at the very bottom of the file. If there
are closing parenthesis at the end, paste this below them. **We do not not recommend typing
this out manually** as a single error can cause it not to work. If you are having trouble
pasting the text into Emacs on Odin, right-click and hit paste instead of using keyboard
shortcuts.


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

### Additional Emacs Configurations

If you followed the instructions provided by your instructor to enable the
CSCI 1302 shell profile on `odin`, then the Emacs that you have access to
is pre-configured to let you use additional Emacs packages using
[use-package](https://github.com/jwiegley/use-package). If you include
`use-package` declarations in your Emacs configuration file, then Emacs
may need to download and install some things the next time it runs in order
to make things work -- such installations may take several seconds to
complete, but they only happen once unless package updates are installed.

**NOTE:** If you want to use `use-package` declarations in an Emacs configuration
file on another machine (e.g., your local machine), then you will need to install
and setup [use-package](https://github.com/jwiegley/use-package)
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

#### Show Style Guide Violations in the Editor

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
got it working is to open a `.java` in Vi and see if it shows line
numbers; if so, then you should be good to go!

**If you do not understand what file you need to create or edit,
then please ask your instructor or a TA!**

Here are the lines that you should add to your Vi configuration
file:

```
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

You must use the Java style for array type declarations and not the C style.
The Java style places the square brackets (i.e., the `[]`) to the left of the
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
An array is a type of object in Java. While the C style presented above is
syntactically correct in Java (i.e., it will compile), Oracle advises that,
"convention discourages this form; the brackets identify the array type and
should appear with the type designation." When declaring a variable
that refers to an array object, the Java style results in a declaration that
is consistent with how variables to other, non-array types of objects are
declared.

### ConstantName

Constant names must use `CONSTANT_CASE`: all uppercase letters, with each word separated
from the next by a single underscore. A _constant_ is a `static` and `final` field or an
interface/annotation field, except `serialVersionUID` and `serialPersistentFields`.

**Note:** A field that is `final` but not `static` is sometimes referred
to as an *instance constant* or *constant instance member* because it looks
like an instance variable that is also declared `final`. Despite being `final`, an
instance constant is not considered a "constant" under the definition
provided by this `[ConstantName]` guideline -- the definition requires that it also be
`static` -- and should follow the same naming convention as instance variables as
described in the [`[MemberName]`](#membername) guideline.

**Rationale:**
This naming convention for constants is pervasive among Java programmers and is even
the same convention used by Oracle and Google. This specific convention allows most
programmers to easily identify a constant when used in source code.

### EmptyBlock

Empty code blocks are not allowed.

**Rationale:**
Code blocks are for code. If, for some reason, you believe that you need an empty code
block, then take a step back and rework your control flow.

**Note:** If the `checkstyle` tool reports this for an empty `catch` block, then please
see the [[EmptyCatchBlock]](#emptycatchblock) policy.

### EmptyCatchBlock

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
directly, then explore the possibility of propagating the exception up
using `throws` in the method signature.

**Note:** Depending on the parsing behavior of the `checkstyle` program,
an empty `catch` block may trigger the `EmptyBlock` policy instead.

### EmptyLineSeparator

You should ensure that empty line separators are present after header,
package, all import declarations, fields, constructors, methods, nested classes,
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
  violates the `FileTabCharacter` guideline by using single `TAB`
  character in the whitespace just before the declaration of
  `private int x = 1;`:

  ```
  $ echo -e "public class One {\n\tprivate int x = 1;\n}\n" > One.java
  ```
  ```
  $ cat -T One.java
  public class One
  ^Iprivate int x = 1;
  }
  ```

  Since a `TAB` (`\t`) is used in the whitespace, the line with the `TAB`
  may appear differently depending on how the program used to view the
  file is configured. We can simulate that here:

  ```
  $ tabs 3; cat One.java
  public class One
	 private int x = 1;
  }
  ```
  ```
  $ tabs 5; cat One.java
  public class One
	   private int x = 1;
  }
  ```
  ```
  $ tabs 9; cat One.java
  public class One
	       private int x = 1;
  }
  ```

* Use the command below to generate `Two.java`, a small class where
  four spaces are used before the declaration of `private int y = 2;`:

  ```
  $ echo -e "public class Two {\n\tprivate int y = 2;\n}\n" > Two.java
  ```
  ```
  $ cat -T Two.java
  public class Two
      private int y = 2;
  }
  ```

  Since no `TAB` (`\t`) is used in the whitespace, the line with four
  spaces do not appear differently depending on how the program used
  to view the file is configured. We can simulate that here:

  ```
  $ tabs 3; cat Two.java
  public class Two
      private int y = 2;
  }
  ```
  ```
  $ tabs 5; cat Two.java
  public class Two
      private int y = 2;
  }
  ```
  ```
  $ tabs 9; cat Two.java
  public class Two
      private int y = 2;
  }
  ```

When you go to write the inside / body of a class or method, you likely press the
`TAB` key on your keyboard. Most text editors implement this by placing the
following directly in the contents of the code file where you pressed the
`TAB` key:

1. One `\t` (single tab character); or
1. Multiple ` ` (single whitespace character).

This policy specifically forbids the first of these two approaches.
If you use the [recommended Emacs configurations](#recommended-emacs-configurations)
or [recommended Vi configurations](#recommended-vi-configurations), then
you will be to avoid _future_ non-conformance of this policy.

**Fix using Emacs:**
If you are an Emacs user who has setup the
[recommended Emacs configurations](#recommended-emacs-configurations), then you
can fix individual lines that violate `FileTabCharacter` by moving to the start
of an offending line and using the following command: `M-x untabify RET`
(i.e., type `M-x`, the entire word `untabify`, then the
return key). To fix an entire file, move to the beginning of the file and use the
following command: `C-u M-x untabify`.

**Rationale:**
Use of tabs instead of spaces may result in different text editors displaying
same file in different ways, depending on the tab width configured for the
given editor. Developers should not need to configure the tab width of their
text editors in order to be able to read source code.

### Indentation

The following indentation rules must be followed:

| Property                  | Description                                                                 | Spaces |
|---------------------------|-----------------------------------------------------------------------------|--------|
| `basicOffset`             | how far new indentation level should be indented when on the next line      | 4      |
| `braceAdjustment`         | how far a braces should be indented when on the next line 	                | 0      |
| `caseIndent`              | how far a case label should be indented when on next line 	                | 0      |
| `throwsIndent` 	          | how far a throws clause should be indented when on next line                | 4      |
| `arrayInitIndent`         | how far an array initializer list item should be indented when on next line | 4      |
| `lineWrappingIndentation` | how far continuation line should be indented when line-wrapping is present  | 4      |

Sometimes, indentation rules are a little hard to parse when parentheses and
curly braces are involved, as is sometimes the case with multi-line inline lambda
expressions. An inline lambda expression is a lambda expression that is used as
a parameter to a method. Here is an example:

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

### JavadocMethod

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

### LeftCurly

Left curly braces (`{`) for code blocks must always be on the end of the line.
For example:

```java
if (condition) {
    ...
```

**Rationale:**
This convention for curly braces is pervasive among Java programmers and
is even the same convention used by companies like Google.

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

### MemberName

Instance variable names must be written in `lowerCamelCase`.

**Rationale:**
This naming convention for instance variables is pervasive among Java programmers and
is even the same convention used by Oracle.

### MethodName

Method names must be written in `lowerCamelCase`.

**Rationale:**
This naming convention for methods is pervasive among Java programmers and
is even the same convention used by Oracle.

### MethodLength

The bodies of methods and constructors should never exceed 60 lines.
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
Well documented code is just as important as correctly working code.

### MissingJavadocType

All class, enum, interface, and annotation interface definitions must have Javadoc
documentation.

**Rationale:**
Just like methods, type documentation is also important. Oftentimes class and interface
documentation provide important high-level details about implementation, naming
conventions, etc. In some cases, even code examples are provided directly in the
documentation to make things easier for programmers who wish to use the code.

**Instructor Note:**
Well documented code is just as important as correctly working code.

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

**Rationale:**
This ordering convention for methods is pervasive among Java programmers and
is even the same convention used by Oracle and Google.

### NeedBraces

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

**Rationale:**
This convention for curly braces is pervasive among Java programmers and
is even the same convention used by companies like Google.

### SummaryJavadoc

In Javadoc comments, the
[summary sentence](https://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#firstsentence)
should always be present and correctly punctuated.
The only exception to this rule is when the first statement in the comment
is `{@inheritDoc}`.

**Rationale:**
The first sentence of a Javadoc comment is the text that appears in the
summary lists of a generated Javadoc website. Failure to either include a summary
or correctly punctuate the summary can result in poor output.

### TypeName

Type names for classes, interfaces, enums, and annotations must be written in _UpperCamelCase_.
Class names are typically nouns or noun phrases. For example, `Character` or `ImmutableList`.
Interface names may also be nouns or noun phrases (for example, `List`), but may sometimes be
adjectives or adjective phrases instead (for example, `Readable`).

**Rationale:**
This convention for type names is pervasive among Java programmers and
is even the same convention used by companies like Oracle and Google.

### WhitespaceAround

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

## References

* <a id="ref-google-javaguide"/>Diamond, M. ([@dimo414](https://github.com/dimo414)). 2016. *Google Java Style Guide.* URL: https://google.github.io/styleguide/javaguide.html
* <a id="ref-tpop"/>Kernighan, B.W. and Pike, R. 1999. *The Practice of Programming.* Addison-Wesley Professional. ISBN: 9780133133448.

## Publication History

| DOI | Tag | Date | Description |
|-----|-----|------|-------------|
| [10.5281/zenodo.3370471](https://doi.org/10.5281/zenodo.3370471) | NA        | NA           | All Versions |
| [10.5281/zenodo.3579521](https://doi.org/10.5281/zenodo.3579521) | `v2019fa` | Dec 16, 2019 | Fall 2019    |
| [10.5281/zenodo.3370472](https://doi.org/10.5281/zenodo.3370472) | `v2019su` | Aug 18, 2019 | Summer 2019  |

<hr/>

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc/4.0/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3370471.svg)](https://doi.org/10.5281/zenodo.3370471)

<small>
Copyright &copy; Michael E. Cotterell, Bradley J. Barnes, and the University of Georgia.
This work is licensed under
a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
The content and opinions expressed on this Web page do not necessarily reflect the views of nor are they endorsed by the University of Georgia or the University System of Georgia.
</small>
