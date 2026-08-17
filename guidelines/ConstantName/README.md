### ConstantName

Constant names must use `CONSTANT_CASE`: all uppercase letters, with each word separated
from the next by a single underscore. A _constant_ is a `static` and `final` field or an
interface/annotation field, except `serialVersionUID` and `serialPersistentFields`.

**Note:** A field that is `final` but not `static` is sometimes referred
to as an *instance constant* or *constant instance member* because it looks
like an instance variable that is also declared `final`. Despite being `final`, an
instance constant is not considered a "constant" under the definition
provided by this [`ConstantName`](#constantname) guideline -- the definition requires that it also be
`static` -- and should follow the same naming convention as instance variables as
described in the [`MemberName`](#membername) guideline.

**Rationale:**
This naming convention for constants is pervasive among Java programmers and is even
the same convention used by Oracle and Google. This specific convention allows most
programmers to easily identify a constant when used in source code.
