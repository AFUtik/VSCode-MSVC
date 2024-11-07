Hi, this repository is needed to build Projects   with MSVC compiler and its libraries in VSCode. Because VSCode is more performant compared to Visual Studio and more convenient due to its useful extensions.

First off, you have to install Visual Studio to obtain MSVC compiler and Windows SDK. There're important libraries from Windows SDK and Visual Studio Tools. Without them some libraries can't work properly.

You need to specify the paths instead of those variables that you see under this text and make it work. You can see my example how to specify these paths in '.vscode/tasks.json'. After you've specified the paths you can add your libs with '.lib' to the end of args or include folder via '"/I\"{include_folder}""'.

I recommend to use extension C++/C Debugger to test the application fast. Don't forget change the path to exe file in '.vscode/launch.json' afterwards.

```json
{
    "version": "2.0.0",
    "tasks": [
      {
        "type": "shell",
        "label": "msvc build",
        "command": "{PATH_TO_MSVC_COMPILER}",
        "args": [
          "/I\"'{WINDOWS_SDK_INCLUDE_PATH}/um'\"",
          "/I\"'{WINDOWS_SDK_INCLUDE_PATH}/ucrt'\"",
          "/I\"'{WINDOWS_SDK_INCLUDE_PATH}/shared'\"",
          "/I\"'{WINDOWS_SDK_INCLUDE_PATH}/winrt'\"",
          "/I\"'{WINDOWS_SDK_INCLUDE_PATH}/cppwinrt'\"",
          "/I\"{MSVC_PATH}/atlmfc/include\"",
          "/I\"{MSVC_PATH}/include\"",
          "/I\"{VS_PATH}/VC/Auxiliary/VS/include\"",
          "/I\"{YOUR INCLUDES...}"",
          "/EHsc",
          "/Fe:\"{PATH_TO_EXE_FILE}\"",
          "/std:c++17",
          "/GA", 
          "/MT",
          "${file}",
          "/link",
          "/LIBPATH:\"'{WINDOWS_SDK_LIB_PATH}/um/x64'\"",
          "/LIBPATH:\"'{WINDOWS_SDK_LIB_PATH}/ucrt/x64'\"",
          "/LIBPATH:\"{MSVC_PATH}/atlmfc/lib/x64\"",
          "/LIBPATH:\"{MSVC_PATH}/lib/x64\"",
          "/LIBPATH:\"{VS_PATH}/VC/Auxiliary/VS/lib/x64\"",
          "{YOUR LIBS...}" 
        ],
        "problemMatcher": ["$msCompile"],
        "group": {
          "kind": "build",
          "isDefault": true
        },
        "detail": "msvc build"
      }
    ]
}
```
