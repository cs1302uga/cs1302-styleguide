package edu.uga.cs1302.example;

/**
 * Example demonstrating valid array type style on field declarations.
 */
public class ValidFieldArray {

    private String[] someVar;

    /**
     * Default constructor.
     */
    public ValidFieldArray() {
        this.someVar = new String[0];
    } // ValidFieldArray

    /**
     * Accessor for someVar.
     *
     * @return the array of strings
     */
    public String[] getSomeVar() {
        return this.someVar;
    } // getSomeVar

} // ValidFieldArray
