---
title: Functional with java stream
date: 2021/3/19
description: Deskripsi kita bicara soal kuda
tag: java, java-stream, functional-programming
author: Yusef
---

Let's talk about functional programming (FP) in Java here.

The allure of FP as compared to OOP is that they look beautiful and easy to read. Look at this method to generate a List of doubles from a given length.
```
import java.util.List;
import java.util.Random;

...
    public static List<Double> getListOfDoubles(int length) {
        return new Random().doubles().limit(length).boxed().collect(Collectors.toList());
    }
...
```

This is what's called a fluent interface.
Back in the days, I like to create this chain type builder methods, albeit generally slower in terms of performance, the beauty of the code makes up for the disadvantage.

In Python, we can convert a list to another through the map function
```
input_sequence = (1,2,3,4)
output_sequence = list(map(lambda n: n*n, input_sequence))
```

Similarly in Javascript/ES6:
```
input_output_list.map((item, index) => { 
	return item*item
})
```

In Java, we can do something similar like this:
```
import java.util.function.Function;
import java.util.stream.Collectors;
...
    public static <T, G> List<T> convertList(List<G> inputList, Function<G, T> mapper) {
        return inputList.stream()
            .map(value -> mapper.apply(value))
            .collect(Collectors.toList());
    }
...
```
The "callback" mapper is a custom function which acts as a converter.

If we want to change the item type of a list, in Python we could do:
```
output_sequence = list(map(lambda number_item: str(number_item), input_sequence))
```
or better yet:
```
output_sequence = [str(number_item) for number_item in input_sequence]
```

To do something similar in Java using stream:
```
    public static <T extends Number> List<String> numberToString(List<T> inputList) {
        return inputList.stream()
            .map(value -> value.toString())
            .collect(Collectors.toList());
    }
```

Furthermore, we can also play around with sorting and casting (T -> U) such as:
```
    public static <T extends Number, U extends Number> List<U> sortAndCast(List<T> numbers) {
        return numbers.stream()
            .sorted()
            .map(value -> (U) value)
            .collect(Collectors.toList());
    }
```

# Filtering data

Let us create a list of 1000 random ints between 1 and 1000, then we filter out only even numbers.
```
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;

    private static int randomValue(int Low, int High) {
        Random r = new Random();
        return r.nextInt(High - Low) + Low;
    }

    private static List<Integer> listOfRandomValues(int length) {
        List<Integer> values = new ArrayList<>(length);
        for (int i = 0; i < length; i++) {
            values.add(randomValue(1, 1000));
        }
        return values;
    }
...
List<Integer> listOfRandoms = listOfRandomValues(1000);
List<Integer> collect = listOfRandoms.stream()
    .filter(value -> value % 2 == 0)
    .collect(Collectors.toList());

System.out.println("100th member would be an even number, since we've filtered them out: " + collect.get(100));
```

