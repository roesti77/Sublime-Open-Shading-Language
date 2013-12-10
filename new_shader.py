import sublime, sublime_plugin
import os

shad = """#include "stdosl.h"

${1:shader} ${2:shadername}(
	$3
)

{
	$4
}
"""

noise = """#include "stdosl.h"

shader ${1:noise}(
	float Time = ${2:1.0},
	point Point = ${3:P},
	output float Cell = ${4:0.0},
	output color Perlin = ${5:0.8},
	output color UPerlin = ${6:0.8})
{   
	/* Cell Noise */
	Cell = noise("cell", Point);
	
    /* Perlin 4D Noise*/
    Perlin = noise("perlin", Point, Time);
   
    /* UPerlin 4D Noise*/
    UPerlin = noise("uperlin", Point, Time);
}
"""

ramp = """#include "stdosl.h"

shader ${1:node_ramp_bsdf}(
	float Exponent = ${2:10.0},
	color Color1 = color(${3:0.8}, ${4:0.0}, ${5:0.0}),
	color Color2 = color(${6:0.0}, ${7:0.8}, ${8:0.0}),
	color Color3 = color(${9:0.0}, ${10:0.0}, ${11:0.8}),
	color Color4 = ${12:0.1},
	color Color5 = ${13:0.2},
	color Color6 = ${14:0.3},
	color Color7 = ${15:0.4},
	color Color8 = ${16:0.5},
	normal Normal = ${17:N},
	output closure color Phong = ${18:0},
	output closure color Diffuse = ${19:0})
{
	color Color[8] = {Color1, Color2, Color3, Color4, Color5, Color6, Color7, Color8};

	Phong = phong_ramp(Normal, Exponent, Color);
	Diffuse = diffuse_ramp(Normal, Color);
}"""

temp = """#include "stdosl.h"

shader ${1:temperature_to_rgb}(
	float Kelvin = ${2:1200.0},
	output color Color = ${3:0.8})
{   
	/* Kelvin to RGB */
	Color = blackbody(Kelvin);
}"""

toon = """#include "stdosl.h"

shader ${1:node_toon_bsdf}(
	color Color = ${2:0.8},
	float Size = ${3:0.5},
	float Smooth = ${4:0.0},
	normal Normal = ${5:N},
	output closure color Diffuse = ${6:0},
	output closure color Specular = ${7:0})
{
	Diffuse = Color * diffuse_toon(Normal, Size, Smooth);
	Specular = Color * specular_toon(Normal, Size, Smooth);
}"""

wave = """#include "stdosl.h"

shader ${1:wavelength_to_rgb}(
	float Wavelength = ${2:500.0},
	output color Color = ${3:0.8})
{   
	/* Wavelength to RGB */
	Color = wavelength_color(Wavelength);
}"""

wire = """#include "stdosl.h"
#include "oslutil.h"

shader ${1:wireframe}(
    float Line_Width = ${2:2.0},
    int Raster = ${3:1},
    output float Wire = ${4:0.0})
{
    Wire = wireframe("triangles", Line_Width, Raster);
}"""

SYNTAX_DEF = 'Packages/Open Shading Language/osl.tmLanguage'


class NewShaderCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()
        v.settings().set('default_dir',
            os.path.join(sublime.packages_path(), 'User'))
        v.settings().set('default_extension', 'osl')
        v.set_syntax_file(SYNTAX_DEF)
        v.run_command("insert_snippet", {"contents": shad})



class NewNoiseShaderCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()
        v.settings().set('default_dir',
            os.path.join(sublime.packages_path(), 'User'))
        v.settings().set('default_extension', 'osl')
        v.set_syntax_file(SYNTAX_DEF)
        v.run_command("insert_snippet", {"contents": noise})


class NewRampShaderCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()
        v.settings().set('default_dir',
            os.path.join(sublime.packages_path(), 'User'))
        v.settings().set('default_extension', 'osl')
        v.set_syntax_file(SYNTAX_DEF)
        v.run_command("insert_snippet", {"contents": ramp})


class NewTempShaderCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()
        v.settings().set('default_dir',
            os.path.join(sublime.packages_path(), 'User'))
        v.settings().set('default_extension', 'osl')
        v.set_syntax_file(SYNTAX_DEF)
        v.run_command("insert_snippet", {"contents": temp})


class NewToonShaderCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()
        v.settings().set('default_dir',
            os.path.join(sublime.packages_path(), 'User'))
        v.settings().set('default_extension', 'osl')
        v.set_syntax_file(SYNTAX_DEF)
        v.run_command("insert_snippet", {"contents": toon})

class NewWaveShaderCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()
        v.settings().set('default_dir',
            os.path.join(sublime.packages_path(), 'User'))
        v.settings().set('default_extension', 'osl')
        v.set_syntax_file(SYNTAX_DEF)
        v.run_command("insert_snippet", {"contents": wave})


class NewWireShaderCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()
        v.settings().set('default_dir',
            os.path.join(sublime.packages_path(), 'User'))
        v.settings().set('default_extension', 'osl')
        v.set_syntax_file(SYNTAX_DEF)
        v.run_command("insert_snippet", {"contents": wire})
