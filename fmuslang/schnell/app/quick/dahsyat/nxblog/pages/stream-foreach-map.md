---
title: forEach println map
date: 2017/08/21
description: Quick tip for processing stream and transforming List
tag: quick-tips, java-stream
author: Yusef
---

Just to put it here because I keep forgetting the syntax.

```
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

Map<String, Book> author_book_map = new HashMap<>();
author_book_map.put("Courtney Shaw", self_help_1);
author_book_map.put("Betty Douglas", wellness_1);
author_book_map.put("Betty Douglas", productivity_1);
// convert to Set to remove duplicates
Set<String> authors = author_book_map.keySet();
authors.stream().forEach(author -> System.out.println(author));
```

"Transformers" such as map, filter, etc work on List. While in Python or Javascript, we can directly use the transfomer's output, in Java, we need to collect and convert the output to List first.

```
System.out.println(Book.getListOfAuthors().stream()
    .map(author -> author.getFirstName() + " " + author.getLastName())
    .collect(Collectors.toList()));
```

For example, to get the oldest author, we can use something like:
```
    public Integer getOldestAuthor() {
        return getListOfAuthors().stream()
            .map(author -> author.getAge())
            .max(Comparator.comparing(Integer::intValue))
            .get();
    }
```

And to get the average age:
```
    public double getAverageAge() {
        return getListOfAuthors().stream()
            .map(author -> author.getAge())
            .mapToDouble(x -> x)
            .average()
            .orElse(Double.NaN);
    }
```

To get the total combined age of all authors (ofc this sounds too contrived)
```
int totalAge = getListOfAuthors().stream().mapToInt(author -> author.getAge()).sum();
```

Or we can get the same output using reduce
```
int totalAge = getListOfAuthors.stream()
    .map(author -> author.getAge())
    .reduce((a, b) -> a + b)
    .get();
```
This is fascinating.

