package edu.uga.cs1302.example;

import java.util.Comparator;
import java.util.List;

/**
 * Invalid lambda parameter names.
 */
public class InvalidLambdaParam {

    /**
     * Demonstrate invalid lambda parameter names.
     *
     * @param list sample list
     */
    public void demo(List<String> list) {
        list.forEach(ElementItem -> System.out.println(ElementItem));
        Comparator<String> comp = (first_str, second_str) -> first_str.compareTo(second_str);
    } // demo

} // InvalidLambdaParam
