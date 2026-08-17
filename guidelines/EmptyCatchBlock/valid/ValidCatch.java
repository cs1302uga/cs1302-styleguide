package edu.uga.cs1302.example;

import java.io.IOException;

/**
 * Valid catch block.
 */
public class ValidCatch {

    /**
     * Process with handled exception.
     */
    public void process() {
        try {
            throw new IOException("error");
        } catch (IOException e) {
            System.err.println(e.getMessage());
        } // try
    } // process

} // ValidCatch
