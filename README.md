You can see example in .vscode/tasks.json

tasks.json 
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
          "/I\"${workspaceFolder}\\dependencies\\include\"",
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
