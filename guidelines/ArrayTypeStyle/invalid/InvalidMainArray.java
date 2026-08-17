package edu.uga.cs1302.example;

/**
 * Example demonstrating invalid (C-style) array type declaration on method parameters.
 */
public class InvalidMainArray {

    /**
     * Main entry point using C-style array syntax.
     *
     * @param args command-line arguments
     */
    public static void main(String args[]) {
        String localArray[] = new String[0];
    } // main

} // InvalidMainArray
