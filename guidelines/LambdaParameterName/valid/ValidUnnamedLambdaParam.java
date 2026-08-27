package edu.uga.cs1302.example;

import java.util.Map;

/**
 * Valid unnamed lambda parameter names.
 */
public class ValidUnnamedLambdaParam {

    /**
     * Demonstrate valid unnamed lambda parameter names.
     *
     * @param map sample map
     */
    public void demo(Map<String, String> map) {
        map.forEach((key, _) -> System.out.println(key));
    } // demo

} // ValidUnnamedLambdaParam
