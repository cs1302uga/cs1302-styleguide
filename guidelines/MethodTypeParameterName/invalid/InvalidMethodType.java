package edu.uga.cs1302.example;

import java.util.List;

/**
 * Invalid method type parameter.
 */
public class InvalidMethodType {

    /**
     * Get first item with lowercase generic.
     *
     * @param <type> element type
     * @param list the list
     * @return the first element
     */
    public <type> type getFirst(List<type> list) {
        return list.get(0);
    } // getFirst

} // InvalidMethodType
