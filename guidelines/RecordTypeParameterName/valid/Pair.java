package edu.uga.cs1302.example;

/**
 * Valid record type parameters.
 *
 * @param <K> key type
 * @param <V> value type
 * @param key the key
 * @param value the value
 */
public record Pair<K, V>(K key, V value) {
} // Pair
