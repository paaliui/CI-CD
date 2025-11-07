cmake_minimum_required(VERSION 3.16)
project(ci_cd_lab5 LANGUAGES CXX)

# Use C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Library with geometry code
add_library(geometry src/rectangle.cpp)
target_include_directories(geometry PUBLIC include)

# Sample application (not used in tests)
add_executable(app src/main.cpp)
target_link_libraries(app PRIVATE geometry)

# ---- Tests ----
enable_testing()

# Triangle tests
add_executable(test_triangle tests/test_triangle.cpp)
target_link_libraries(test_triangle PRIVATE geometry)
add_test(NAME triangle_tests COMMAND test_triangle)

# Circle tests
add_executable(test_circle tests/test_circle.cpp)
target_link_libraries(test_circle PRIVATE geometry)
add_test(NAME circle_tests COMMAND test_circle)
