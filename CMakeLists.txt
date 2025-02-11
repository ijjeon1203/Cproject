cmake_minimum_required(VERSION 3.10)

project(
	RedEyeIE 
	LANGUAGES CSharp
	VERSION 1.0
)

file(GLOB_RECURSE SOURCES "src/*.cs" "src/Properties/AssemblyInfo.cs" "src/app.config")
file(GLOB_RECURSE RESX_FILES "src/Properties/*.resx")
# settings파일 추가 
file(GLOB_RECURSE SETTINGS_FILES "src/Properties/Settings.settings" )

# Settings.settings를 Settings.Designer.cs로 변환
foreach(SETTINGS_FILE ${SETTINGS_FILES})
    get_filename_component(SETTINGS_NAME ${SETTINGS_FILE} NAME_WE)
    add_custom_command(OUTPUT "src/Properties/${SETTINGS_NAME}.Designer.cs"
        COMMAND resgen ${SETTINGS_FILE} "Properties/${SETTINGS_NAME}.Designer.cs"
        DEPENDS ${SETTINGS_FILE}
    )
    list(APPEND GENERATED_SETTINGS "Properties/${SETTINGS_NAME}.Designer.cs")
endforeach()


# 리소스 파일 변환 (.resx -> .resources)
foreach(RESX_FILE ${RESX_FILES})
    get_filename_component(RESX_NAME ${RESX_FILE} NAME_WE)
    add_custom_command(OUTPUT "${RESX_NAME}.resources"
        COMMAND resgen ${RESX_FILE} ${RESX_NAME}.resources
        DEPENDS ${RESX_FILE}
    )
    list(APPEND RESOURCE_FILES "${RESX_NAME}.resources")
endforeach()



# 제일 하단으로 위치이동
# 전체 CMakeLists 보니까 위에 있네
add_executable(RedEyeIE ${SOURCES} ${RESOURCE_FILES} ${GENERATED_SETTINGS})

# Properties 폴더로 그룹화하여 .sln에 표시
source_group("Properties" FILES "Properties/AssemblyInfo.cs" "Properties/resources.resx" "Properties/Settings.settings" FILES "app.config" ${GENERATED_SETTINGS})


# dotnetframework 추가 
# 어셈블리참조 추가 위로 위치변경
set_property(TARGET RedEyeIE PROPERTY VS_DOTNET_TARGET_FRAMEWORK_VERSION "v4.7.2")


# System.Drawing 어셈블리 참조 추가
#set_property(TARGET RedEyeIE PROPERTY DOTNET_REFERENCES "System.Drawing;System.Windows.Forms")




#set_property(TARGET RedEyeIE PROPERTY DOTNET_REFERENCES "System.Drawing")
#set_property(TARGET RedEyeIE PROPERTY DOTNET_REFERENCES "System.Windows")
#set_property(TARGET RedEyeIE PROPERTY DOTNET_REFERENCES "System*")
#set_property(TARGET RedEyeIE PROPERTY DOTNET_REFERENCES "Microsoft.Csharp*")
#set_property(TARGET RedEyeIE PROPERTY DOTNET_REFERENCES "System.Core")

