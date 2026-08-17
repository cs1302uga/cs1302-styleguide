### OuterTypeFilename

In any given `.java` file, the outer type name and the file name must match.
For example, the class `Foo` must be in a file named `Foo.java`.

**Rationale:** Although this is only technically required by the Java Language
Specification when the outer type is declared with `public` visibility, we
stick to this convention for other visibilities as well. In any case, most of
the time your outer type will be declared as `public`.
