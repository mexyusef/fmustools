---
title: constexpr in C++17
date: 2017/09/03
description: 
tag: c++17, constexpr
author: Yusef
---

content

```

#include <string>
#include <iostream>
#include <cassert>

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
constexpr double harmonic_mean(int a, int b)
{
    double ret_val = 0.0;
    ret_val = 2.0 * a * b / (a + b);

    return ret_val;
}

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
void harmonic_mean_compile_time()
{
    std::cout << "*** harmonic mean of two numbers at compile time ***" << std::endl;

    const int a = 3;
    constexpr int b = 5;

    constexpr double hm = harmonic_mean(a, b);
    static_assert(hm == 3.75);

    std::cout << "Value computed at compile time: " << hm << std::endl;
}

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
void harmonic_mean_run_time()
{
    std::cout << "*** harmonic mean of two numbers at run time ***" << std::endl;

    int a = 3;
    const int b = 5;

    const double hm = harmonic_mean(a, b);
    assert(hm == 3.75);

    std::cout << "Value computed at run time: " << hm << std::endl;
}

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
int main (int argc, char *argv[])
{

    harmonic_mean_compile_time();
    harmonic_mean_run_time();
    return 0;
}
```

CMake file to build the code
```
cmake_minimum_required (VERSION 3.11.0)
project (blogging)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(main.exe main.cpp)
```



Here's the output
```
*** harmonic mean of two numbers at compile time ***
Value computed at compile time: 3.75
*** harmonic mean of two numbers at run time ***
Value computed at run time: 3.75
```
