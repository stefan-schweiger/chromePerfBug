
# Performace regression between Chrome versions

WebAssembly performance between Version 65 and 69 has been declined.
For the two very simple programs in this repository these are the results:

**C.Wasm**
Chromium 65.0.3325.0: 7334.00
Chrome 69.0.3497.100: 8658.00

x1.2 slower

**DotNet.Wasm**
Chromium 65.0.3325.0: 7,711.00
Chrome 69.0.3497.100: 22,164.80

x2.9 slower

To compile the sample projects following dependencies where used

* emcc 1.38.12
* csc 2.7.0.62620 (Microsoft (R) Visual C# Compiler) from mono 5.14.0 
* mono WASM_SDK commit c211324 ([Download link](https://jenkins.mono-project.com/job/test-mono-mainline-wasm/label=ubuntu-1804-amd64/1034/Azure/))