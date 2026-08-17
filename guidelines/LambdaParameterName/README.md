### LambdaParameterName

Parameter names declared in lambda expressions must be written in `lowerCamelCase`.

```java
list.forEach(elementItem -> System.out.println(elementItem)); // valid style
Comparator<String> comp = (firstStr, secondStr) -> firstStr.compareTo(secondStr); // valid style
```

```java
list.forEach(ElementItem -> System.out.println(ElementItem)); // invalid style
Comparator<String> comp = (first_str, second_str) -> first_str.compareTo(second_str); // invalid style
```

**Rationale:**
Lambda parameters are local identifiers and must conform to the standard `lowerCamelCase` naming convention used for all Java parameters and local variables.
