---
title: Functional Interface
date: 2021/10/07
description: Functional Interface
tag: functional-interface, java
author: Yusef
---

There are various structures in modern Java. 
They are Comparator, Consumer, Function, Optional, Predicate, and Supplier.

baca rationales utk FI.

//Comparators are well known from older versions of Java

//Consumers represent operations to be performed on a single input argument

//Functions accept one argument and produce a result

//Optionals are not functional interfaces, but a handy way to prevent NullPointerExceptions
//and remove the need for Null checks

//Predicates are boolean valued functions of one argument

//Suppliers produce a result of a given type, but don't accept arguments

```
import java.util.Comparator;
import java.util.Optional;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;

Comparator<Skill> skillComparator = (s1, s2) -> Integer.valueOf(s1.getSkillRank()).compareTo(s2.getSkillRank());
Skill skill1 = new Skill("Programmer", "Technology", 10);
Skill skill2 = new Skill("CTO", "Technology", 50);
System.out.println(skillComparator.compare(skill1, skill2)); //-1
System.out.println(skillComparator.reversed().compare(skill1, skill2)); //1

Consumer<Skill> skillWriter = (s) -> System.out.println("Hello, your skill is " + s.getSkillName());
skillWriter.accept(new Skill("Programmer", "Technology", 1));

Function<String, Integer> toIntger = (i) -> Integer.valueOf(i);
System.out.println(toIntger.apply("123"));        

Optional<String> optional = Optional.of("Kabam!");
System.out.println(optional.isPresent()); //true
System.out.println(optional.get()); //Kabam!
System.out.println(optional.orElse("Missing")); //Only if the String is null
optional.ifPresent((s) -> System.out.println(s)); //Print if present

Predicate<String> predicate = (s) -> s.length() > 1;
System.out.println(predicate.test("h")); //false;
System.out.println(predicate.test("hello")); //true
System.out.println(predicate.negate().test("h")); //true

Supplier<Car> carSupplier = Car::new;
Car myCar = carSupplier.get();
Car anotherCar = carSupplier.get();
```
