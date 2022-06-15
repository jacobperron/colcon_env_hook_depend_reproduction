cmake_minimum_required(VERSION 3.8)
project(bar)

find_package(ament_cmake REQUIRED)

if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
  ament_add_pytest_test(bar_test "test/test_bar.py")
endif()

ament_package()
