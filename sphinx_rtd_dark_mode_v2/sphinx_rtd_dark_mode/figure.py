from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from  docutils import utils

import os
from PIL import Image

from sphinx.directives.patches import Figure


class DarkFigure(Figure):

    has_content = True
    option_spec = Figure.option_spec.copy()

    def run(self):

        self.options['class'] = ['light-figure']
        (light_figure_node,) = Figure.run(self)
        

        if isinstance(light_figure_node, nodes.system_message):
            return [light_figure_node]


        source = self.state_machine.input_lines.source(
        self.lineno - self.state_machine.input_offset - 1)
        source_dir = os.path.dirname(os.path.abspath(source))
        path = directives.path(self.arguments[0])
        if path.startswith('<') and path.endswith('>'):
            path = os.path.join(self.standard_include_path, path[1:-1])
        path = os.path.normpath(os.path.join(source_dir, path))
        path = utils.relative_path(None, path)
        path = nodes.reprunicode(path)

        img = Image.open(path)
        img = img.convert("RGBA")
        
        new_img = []

        for pixel in img.getdata():
            if pixel[0] == pixel[1] == pixel[2] and pixel[3] >= 90:
                new_img.append((255-pixel[0], 255-pixel[1], 255-pixel[2], 255))
            else:
                new_img.append(pixel)

        img.putdata(new_img)
        new_path = path.replace(".png", "_dark.png")
        if os.path.exists(new_path):
            os.remove(new_path)
        

        img.save(new_path)

        self.options['classes'] = ['dark-figure']
        self.arguments[0] = self.arguments[0].replace(".png", "_dark.png")
        
        (dark_figure_node,) = Figure.run(self)
        

        if isinstance(dark_figure_node, nodes.system_message):
            return [dark_figure_node]

        light_figure_node = nodes.figure('', light_figure_node)
        dark_figure_node = nodes.figure('', dark_figure_node)

        return [light_figure_node, dark_figure_node]