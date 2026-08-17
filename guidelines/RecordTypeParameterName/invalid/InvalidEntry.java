package edu.uga.cs1302.example;

/**
 * Invalid record type parameters.
 *
 * @param <Key> key type
 * @param <Value> value type
 * @param k the key
 * @param v the value
 */
public record InvalidEntry<Key, Value>(Key k, Value v) {
} // InvalidEntry
