import json
import os

cur_dir = os.getcwd()
project_path = input("Wrire the path to project: ")
if project_path: cur_dir = project_path

exe_path = input("Wrire a relative path to executable file: ")
if exe_path[0] != '/' or exe_path[0] != '\\': exe_path = '\\' + exe_path

os.makedirs(cur_dir + "/.vscode", exist_ok=True)
tasks_file_path = '.vscode/tasks.json'
launch_file_path = '.vscode/launch.json'

#CHANGE VARIABLES TO YOURS
vars = {
    "VS_PATH": "E:/apps/VS2022/VC/Tools/MSVC/14.41.34120",
    "SDK_INCLUDE_PATH": "E:/Windows Kits/10/Include/10.0.26100.0",
    "SDK_LIB_PATH": "E:/Windows Kits/10/Lib/10.0.26100.0",
    "MSVC_PATH": "E:/apps/VS2022/VC/Tools/MSVC/14.41.34120",
    "CXX_VERSION": "std:c++17"
}

for key, item in vars.items():
    if item: continue

    info = input(f"Write the variable -> '{key}': ")
    if info: 
        vars[key] = info
    else:
        print(f"You haven't specified '{key}'")
        exit()

tasks = {'version': '2.0.0', 'tasks': [{'type': 'shell', 'label': 'msvc build', 'command': f"{vars['MSVC_PATH']}/bin/Hostx64/x64/cl.exe", 'args': [f"/I\"'{vars['SDK_INCLUDE_PATH']}/um'\"",f"/I\"'{vars['SDK_INCLUDE_PATH']}/ucrt'\"",f"/I\"'{vars['SDK_INCLUDE_PATH']}/shared'\"",f"/I\"'{vars['SDK_INCLUDE_PATH']}/winrt'\"",f"/I\"'{vars['SDK_INCLUDE_PATH']}/cppwinrt'\"",f"/I\"{vars['MSVC_PATH']}/atlmfc/include\"",f"/I\"{vars['MSVC_PATH']}/include\"",f"/I\"{vars['VS_PATH']}/VC/Auxiliary/VS/include\"","/EHsc",f"/Fe:\"{cur_dir}{exe_path}\"",f"/{vars['CXX_VERSION']}","/GA", "/MT","${file}","/link",f"/LIBPATH:\"'{vars['SDK_LIB_PATH']}/um/x64'\"",f"/LIBPATH:\"'{vars['SDK_LIB_PATH']}/ucrt/x64'\"",f"/LIBPATH:\"{vars['MSVC_PATH']}/atlmfc/lib/x64\"",f"/LIBPATH:\"{vars['MSVC_PATH']}/lib/x64\"",f"/LIBPATH:\"{vars['VS_PATH']}/VC/Auxiliary/VS/lib/x64\"",], 'problemMatcher': ['$msCompile'], 'group': {'kind': 'build', 'isDefault': True}, 'detail': 'msvc build'}]}
launch = {'version': '0.2.0', 'configurations': [{'name': 'Build with MSVC and Debug', 'type': 'cppvsdbg', 'request': 'launch', 'program': f"{cur_dir}{exe_path}", 'args': [], 'stopAtEntry': False, 'cwd': '${fileDirname}', 'environment': [], 'console': 'externalTerminal', 'preLaunchTask': 'msvc build'}, {'name': 'C/C++ Runner: Debug Session', 'type': 'cppdbg', 'request': 'launch', 'args': [], 'stopAtEntry': False, 'externalConsole': True, 'cwd': 'e:/Cpp/vscode-msvc/src', 'program': 'e:/Cpp/vscode-msvc/src/build/Debug/outDebug', 'MIMode': 'gdb', 'miDebuggerPath': 'gdb', 'setupCommands': [{'description': 'Enable pretty-printing for gdb', 'text': '-enable-pretty-printing', 'ignoreFailures': True}]}]}

with open(tasks_file_path, 'w') as file:  json.dump(tasks, file, indent=4)
with open(launch_file_path, 'w') as file: json.dump(launch, file, indent=4)