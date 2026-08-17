# CSCI 1302 Code Style Guide

![Approved for: Fall 2025](https://img.shields.io/badge/Approved%20for-Fall%202025-green)

Make sure you read through this document carefully. **In addition to describing why
code style is important and the code style guidelines for CSCI 1302, it also
describes how to use the `check1302` program on `Odin` to check your code as well
as Emacs and Vi configurations that, if used, will reduce the number of style issues
you have in your code moving forward.**


<!-- TOC_PLACEHOLDER -->

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
  This saves real-world time when it comes to fixing problems in your code.

* It is easier to extend and/or incorporate into other projects. This results in your
  code being more useful to others as well as your future self.

The list could go on. The important thing to remember is that **quality not only
refers to the output of a program but also its effect on the people who interact
with the code**. Rarely, in practice, are you the only one who will read and use
your code. If you're a software engineer, then it is very likely that *many*
people will interact with your code over time and that you will interact with *lots*
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

### Run Checkstyle

To check your Java source code for compliance, you can use a custom version
of the Checkstyle program on `Odin` called `check1302`. **This program is
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

```
$ emacs ~/.emacs
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

#### Show Style Guide Violations in the Editor (Optional)

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

