cmake_minimum_required(VERSION 3.10)

project(
	cppProject 
	LANGUAGES CXX
	VERSION 1.0
)

file(GLOB_RECURSE SOURCES "src/*.cpp" "src/*.h" )

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)


add_compile_options("$<$<CXX_COMPILER_ID:MSVC>:/utf-8>")


# Visual Studio 빌드 시 도구 집합 설정 (Windows일 경우)
set(CMAKE_GENERATOR_TOOLSET v142 CACHE STRING "")


# 시작 프로젝트 설정 (Visual Studio 한정)
set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT cppProject)

# 실행파일 추가 
add_executable(cppProject ${SOURCES} ${RESOURCE_FILES} ${GENERATED_SETTINGS})
