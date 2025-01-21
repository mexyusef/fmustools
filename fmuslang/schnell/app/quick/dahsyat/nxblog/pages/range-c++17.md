---
title: range in C++17
date: 2018/10/28
description: 
tag: c++17, range
author: Yusef
---


```
#include <range/v3/all.hpp>

#include <string>
#include <algorithm>
#include <iostream>

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
void test_range_01()
{
    std::cout << "*** test 01 ***" << std::endl;

    std::vector<int> v{1,6,2,7,3,8};
    for (int i : v)
        std::cout << i << ", ";
    std::cout << std::endl;

    ranges::sort(v);
    ranges::for_each(v,
        [] (auto i) {std::cout << i << ", ";});
    std::cout << std::endl;

    auto rng = v | ranges::view::remove_if([](int i){return i % 2 == 1;})
                 | ranges::view::transform([](int i){return std::to_string(i);});
    for (std::string i : rng)
        std::cout << i << ", ";
    std::cout << std::endl;

}

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
void test_range_01a()
{
    std::cout << "*** test 01a ***" << std::endl;

    std::vector<int> v{1,6,2,7,3,8};
    for (int i : v)
        std::cout << i << ", ";
    std::cout << std::endl;

    std::sort(v.begin(), v.end());
    for (int i : v)
        std::cout << i << ", ";
    std::cout << std::endl;

    std::vector<int> vi;
    std::copy_if(v.begin(), v.end(),
        std::back_inserter(vi), [](int i){return i % 2 == 0;});

    std::vector<std::string> vs;
    std::transform(vi.begin(), vi.end(),
        std::back_inserter(vs), [](int i){return std::to_string(i);});

    for (std::string i : vs)
        std::cout << i << ", ";
    std::cout << std::endl;
}

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
void test_range_02()
{
    std::cout << "*** test 02 ***" << std::endl;

    auto range_int = ranges::view::ints(1, ranges::unreachable)
                | ranges::view::transform([](int i) {return i*i;})
                | ranges::view::take(10);

    for (int i : range_int)
        std::cout << i << ", ";
    std::cout << std::endl;

    const int sum = ranges::accumulate(range_int, 0);
    std::cout << "sum = " << sum;
    std::cout << std::endl;

}

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
void test_range_03()
{
    std::cout << "*** test 03 ***" << std::endl;

    auto range_int = ranges::view::ints(5, ranges::unreachable)
                | ranges::view::transform([](int i) {return 2*i;})
                | ranges::view::take(100);

    auto i = std::begin(range_int);
    std::cout << *(++i) << std::endl;
}

int main()
{
    test_range_01();
    test_range_01a();
    test_range_02();
    test_range_03();

    return 0;
}
```



In our cmake file, we utilize range library from https://github.com/ericniebler/range-v3.
```
cmake_minimum_required (VERSION 3.11.0)
project (latihan)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)


include(FetchContent)
FetchContent_Declare(
    ranges
    GIT_REPOSITORY "https://github.com/ericniebler/range-v3.git"
    GIT_TAG 50ef05324f880569436c424d0c33ba4de36fb6d9
)
FetchContent_GetProperties(ranges)
if(NOT ranges_POPULATED)
    FetchContent_Populate(ranges)
endif()
set(RANGES_PATH ${ranges_SOURCE_DIR})
include_directories(${RANGES_PATH}/include)


add_executable(hasil01 utama.cpp)
```


Here's the output
```
*** test 01 ***
1, 6, 2, 7, 3, 8,
1, 2, 3, 6, 7, 8,
2, 6, 8,
*** test 01a ***
1, 6, 2, 7, 3, 8,
1, 2, 3, 6, 7, 8,
2, 6, 8,
*** test 02 ***
1, 4, 9, 16, 25, 36, 49, 64, 81, 100,
sum = 385
*** test 03 ***
12
```
