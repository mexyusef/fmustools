---
title: Flatmap in Java and Javascript
date: 2017/02/11
description: The idea of flatmap
tag: flatmap, java, functional-programming
author: Yusef
---

In my view, the best way to think if flatmap, is by associating a map with a list of list of 1 item, and the equivalent flatmap of that map with a list of those items.

There are several G10 countries where a G10 is a grouping of 10 countries. We want to combine all the groupings.

```
List<String> G10A = Arrays.asList("Hungary", "French Guiana", "Germany", "Solomon Islands", "Isle of Man", "Iran", "Liechtenstein", "Reunion", "Ethiopia", "Uganda");

List<String> G10B = Arrays.asList("Cote d'Ivoire", "Jersey", "Sweden", "Bosnia and Herzegovina", "Bulgaria", "Sri Lanka", "Yemen", "Micronesia", "Australia", "Macao");

List<String> G10C = Arrays.asList("Papua New Guinea", "Congo", "Guadeloupe", "China", "Swaziland", "Turks and Caicos Islands", "Estonia", "Saint Barthelemy", "Dominican Republic", "Cote d'Ivoire");

List<String> G10D = Arrays.asList("Samoa", "Congo", "Pitcairn Islands", "Mayotte", "Argentina", "Macao", "Pakistan", "Singapore", "Malta", "Kazakhstan");

List<List<String>> fourG10s = new ArrayList<>();
fourG10s.add(G10A);
fourG10s.add(G10B);
fourG10s.add(G10C);
fourG10s.add(G10D);

fourG10s.stream()
    .flatMap(g10 -> g10.stream())
    .forEach(country -> System.out.println(country));
```

Another approach, where we want to make sure that every item is unique in the combined result.
Supposed that EliteForce has a `Set<String>` member internally.

```
EliteForce force1 = new EliteForce();
force1.addSoldier("George Owen");
force1.addSoldier("Tyler Barrera");
force1.addSoldier("Daniel Carter");
force1.addSoldier("James Bond");

EliteForce force2 = new EliteForce();
force2.addSoldier("Jason Berry");
force2.addSoldier("Sally Martin DVM");
force1.addSoldier("James Bond");

List<EliteForce> platoon = new ArrayList<>();
platoon.add(force1);
platoon.add(force2);

List<String> collect = platoon.stream()
        .map(x -> x.getBooksOnLoan())
        .flatMap(x -> x.stream())
        .distinct()
        .collect(Collectors.toList());

collect.forEach(x -> System.out.println(x));
```
