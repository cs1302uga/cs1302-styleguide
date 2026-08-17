package edu.uga.cs1302.example;

/**
 * Invalid record type parameters.
 *
 * @param <key> key type
 * @param <value> value type
 * @param k the key
 * @param v the value
 */
public record InvalidPair<key, value>(key k, value v) {
} // InvalidPair
