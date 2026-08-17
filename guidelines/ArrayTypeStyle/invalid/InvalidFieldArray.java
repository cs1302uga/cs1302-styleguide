package edu.uga.cs1302.example;

/**
 * Example demonstrating invalid (C-style) array type declaration on field.
 */
public class InvalidFieldArray {

    private String someVar[];

    /**
     * Default constructor.
     */
    public InvalidFieldArray() {
        this.someVar = new String[0];
    } // InvalidFieldArray

    /**
     * Accessor for someVar using C-style array return type.
     *
     * @return the array of strings
     */
    public String getSomeVar()[] {
        return this.someVar;
    } // getSomeVar

} // InvalidFieldArray
