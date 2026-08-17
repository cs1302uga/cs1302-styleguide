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
  spaces does not appear differently depending on how the program used
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

**Fix using Emacs:**
If you are an Emacs user who has set up the
[recommended Emacs configurations](#recommended-emacs-configurations), then you
can fix individual lines that violate `FileTabCharacter` by moving to the start
of an offending line and using the following command: `M-x untabify RET`
(i.e., type `M-x`, the entire word `untabify`, then the
return key). To fix an entire file, move to the beginning of the file and use the
following command: `C-u M-x untabify`.

**Rationale:**
The use of tabs instead of spaces may result in different text editors displaying
the same file in different ways, depending on the tab width configured for the
given editor. Developers should not need to configure the tab width of their
text editors in order to be able to read source code.
