package edu.uga.cs1302.example;

import java.util.Comparator;
import java.util.List;

/**
 * Valid lambda parameter names.
 */
public class ValidLambdaParam {

    /**
     * Demonstrate valid lambda parameter names.
     *
     * @param list sample list
     */
    public void demo(List<String> list) {
        list.forEach(elementItem -> System.out.println(elementItem));
        Comparator<String> comp = (firstStr, secondStr) -> firstStr.compareTo(secondStr);
    } // demo

} // ValidLambdaParam
