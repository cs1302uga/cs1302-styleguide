package edu.uga.cs1302.example;

import java.io.IOException;

/**
 * Invalid empty catch block.
 */
public class InvalidCatch {

    /**
     * Process with empty catch block.
     */
    public void process() {
        try {
            throw new IOException("error");
        } catch (IOException e) {
        } // try
    } // process

} // InvalidCatch
