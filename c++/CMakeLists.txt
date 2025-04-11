cmake_minimum_required(VERSION 3.10)

project(
	Cproject 
	LANGUAGES C
	VERSION 1.0
)

file(GLOB_RECURSE SOURCES "src/*.cpp" "src/*.h" )

# C++ 표준 설정
# set(CMAKE_CXX_STANDARD 17)
# set(CMAKE_CXX_STANDARD_REQUIRED True)

set(CMAKE_GENERATOR_TOOLSET v142)


# 설정값

set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT Cproject)

# 실행파일 추가 
add_executable(Cproject ${SOURCES} ${RESOURCE_FILES} ${GENERATED_SETTINGS})



# CSharp
# set_property(TARGET RedEyeIE PROPERTY VS_DOTNET_TARGET_FRAMEWORK_VERSION "v4.7.2")

