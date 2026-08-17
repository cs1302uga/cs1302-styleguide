package edu.uga.cs1302.example;

import java.util.List;

/**
 * Valid method type parameters.
 */
public class ValidMethodType {

    /**
     * Get first item.
     *
     * @param <T> element type
     * @param list the list
     * @return the first element
     */
    public <T> T getFirst(List<T> list) {
        return list.get(0);
    } // getFirst

    /**
     * Process item.
     *
     * @param <ReturnType> return type
     * @param item the item
     * @return the item
     */
    public <ReturnType> ReturnType process(ReturnType item) {
        return item;
    } // process

} // ValidMethodType
