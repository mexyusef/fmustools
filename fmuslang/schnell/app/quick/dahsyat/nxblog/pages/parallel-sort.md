---
title: Parallel Sort
date: 2019/03/02
description: Parallel Sort
tag: parallel-sort, function-programming, java, stream
author: Yusef
---


Here we create a list of 10M UUIDs. We will try compare the sorting time for the sequential approach and the parallel approach.

I tried this on my Galaxy Note 8 phone using termux.

```
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

public class ParallelSortStream {
    public static void main(String args[]) throws ExecutionException, InterruptedException {
        List<String> values = getListOfUUIDs(10000000);
        sequentialSort(values);
        parallelSort(values);
        maxParallelSort(values, 8);
    }

    private static void maxParallelSort(List<String> values, int threads) throws ExecutionException, InterruptedException {
        long t0 = System.nanoTime();
        ForkJoinPool forkJoinPool = new ForkJoinPool(threads);
        List<String> sorted = forkJoinPool.submit(() ->
            values.parallelStream().sorted().collect(Collectors.toList())
        ).get();

        System.out.println(sorted.get(10));
        long t1 = System.nanoTime();
        long millis = TimeUnit.NANOSECONDS.toMillis(t1 - t0);
        System.out.println(String.format("Max parallel sort took: %d ms", millis));
    }

    private static void parallelSort(List<String> values) {
        long t0 = System.nanoTime();
        List<String> sorted = values.parallelStream().sorted().collect(Collectors.toList());
        System.out.println(sorted.get(10));
        long t1 = System.nanoTime();
        long millis = TimeUnit.NANOSECONDS.toMillis(t1 - t0);
        System.out.println(String.format("parallel sort took: %d ms", millis));
    }

    private static void sequentialSort(List<String> values) {
        long t0 = System.nanoTime();
        List<String> sorted = values.stream().sorted().collect(Collectors.toList());
        System.out.println(sorted.get(10));
        long t1 = System.nanoTime();
        long millis = TimeUnit.NANOSECONDS.toMillis(t1 - t0);
        System.out.println(String.format("sequential sort took: %d ms", millis));
    }

    private static List<String> getListOfUUIDs(int listSize) {
        List<String> values = new ArrayList<>(listSize);
        for (int i = 0; i < listSize; i++) {
            UUID uuid = UUID.randomUUID();
            values.add(uuid.toString());
        }
        return values;
    }
}
```

Here are the result, the parallel version was 4x faster than the sequential one, which is not surprising.

```
~/work/blogging 03:17:41$ java ParallelSortStream
000016a0-d980-4140-b9ac-0b40a5579683
sequential sort took: 41298 ms
000016a0-d980-4140-b9ac-0b40a5579683
parallel sort took: 10384 ms
000016a0-d980-4140-b9ac-0b40a5579683
Max parallel sort took: 9879 ms
```

