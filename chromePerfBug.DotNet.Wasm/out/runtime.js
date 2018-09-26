
var Module = { 
	onRuntimeInitialized: function () {
		MONO.mono_load_runtime_and_bcl (
			"managed",
			"managed",
			0,
			[ "Benchmark.dll","mscorlib.dll","System.dll","Mono.Security.dll","System.Xml.dll","System.Core.dll","WebAssembly.Bindings.dll" ],
			function () {
				Module.mono_bindings_init ("[WebAssembly.Bindings]WebAssembly.Runtime");
				App.init ();
			});
	},
};
