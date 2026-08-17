package edu.uga.cs1302.example;

/**
 * Valid record type parameters with Type suffix.
 *
 * @param <KeyType> key type
 * @param <ValueType> value type
 * @param key the key
 * @param val the val
 */
public record Entry<KeyType, ValueType>(KeyType key, ValueType val) {
} // Entry
