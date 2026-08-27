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
