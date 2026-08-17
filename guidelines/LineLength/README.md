### LineLength

You should limit the number of characters, including whitespace, on any given
line to 100 characters. Except as noted below, any line that would exceed this
limit must be manually line-wrapped in a consistent manner. Exceptions to the
column limit include:
* lines where obeying the column limit is not possible (for example, a long URL
  in Javadoc, or a long JSNI method reference);
* package and import statements; and
* command-line input examples in a comment that may be cut-and-pasted into a shell.

**Rationale:** Long lines are hard to read in printouts or if developers have
limited screen space for the source code, e.g., if the editor displays additional
information like line numbers, multiple files, project tree, class hierarchy, etc.
