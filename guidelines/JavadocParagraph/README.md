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
