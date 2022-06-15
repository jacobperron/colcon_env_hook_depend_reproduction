cmake_minimum_required(VERSION 3.8)
project(foo)

find_package(ament_cmake REQUIRED)
ament_environment_hooks(${CMAKE_CURRENT_SOURCE_DIR}/env_hook/popcorn.dsv)
ament_package()
