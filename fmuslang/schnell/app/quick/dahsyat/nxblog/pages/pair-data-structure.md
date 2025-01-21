---
title: Pair data structure
date: 2021/01/28
description: Pair data structure in various perspectives
tag: pair
author: Yusef
---

A pair (key-value or left-right) is a very useful data structure. Most dynamic programming languages and modern functional languages support the type. In Python, it's natural to use a tuple.

In Java, I usually create something like this:
```
public class Pair<K, V> {
    private final K first;
    private final V second;

    public Pair(K first, V second) {
        this.first = first;
        this.second = second;
    }

    public K getLeft() {
        return this.first;
    }

    public V getRight() {
        return this.second;
    }

    @Override
    public String toString() {
		return "(" + first + ", " + second + ")";
    }
}
```

Kotlin has a built-in function for this type:
```
val capitol = "USA" to "New York" // this is deliberate
// or 
// val capitol = Pair("USA", "New York")

println(capitol.first)
println(capitol.second)
```
And we can destructure the type:
```
val (country, capital) = capitol
println(country)
println(capital)
```
