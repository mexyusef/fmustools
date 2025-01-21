---
title: Data Mapping
date: 2018/04/02
description: Data Mapping
tag: java, functional-programming
author: Yusef
---

Content:

```
import java.util.Arrays;
import java.util.List;

public class MappingData {
    public static void main(String args[]) {
        List<Double> numbers = Arrays.asList(-44208693909464.4, -4.1546783069715, 417792.444174063, -77542297662826.1, -8.10341864991204, 60785753.9379771, 52387217213.2856, 28814529784.22, 2.88541388947086, 6182.3320862153);

//        numbers.stream()
//            .map(number -> number +=1)
//            .map(number -> number *= 5)
//            .map(number -> number /= 2)
//            .map(number -> new DoubleValueHolder(number))
//            .map(number -> number.getStringValue())
//            .forEach(number -> System.out.println(number));

        numbers.parallelStream()
            .map(number -> number += 1)
            .map(number -> number *= 5)
            .map(number -> number /= 2)
            .map(number -> new DoubleValueHolder(number))
            .map(number -> number.getStringValue())
            .forEach(number -> System.out.println(number));
    }

    static class DoubleValueHolder {
        Double value;

        DoubleValueHolder(Double value) {
            this.value = value;
        }

        String getStringValue() {
            return Double.toString(value);
        }
    }
}
```
