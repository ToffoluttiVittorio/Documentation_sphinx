# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Plateforme cartographique OLE'
copyright = '2024, Vittorio Toffolutti'
author = 'Vittorio Toffolutti'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    # autres extensions...
]

templates_path = ['_templates']
exclude_patterns = []
html_show_sourcelink = False
language = 'fr'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

# The name of an image file (relative to this directory) to place at the top of the sidebar 
html_logo = 'images/logo.png'

# Add cutom css and space after an image
html_static_path = ['_static']
