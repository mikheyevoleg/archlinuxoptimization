# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ARU'
copyright = 'ARU 2018 - 2022, Pavel Priluckiy, Vasiliy Stelmachenok and contributors'
author = 'Pavel Priluckiy, Vasiliy Stelmachenok and contributors'

# The full version, including alpha/beta/rc tags
release = '2022.01.30'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.githubpages']

master_doc = 'index'
root_doc = master_doc

source_suffix = { '.rst': 'restructuredtext' }

# Closes:
# https://github.com/ventureoo/ARU/issues/3
# https://github.com/ventureoo/ARU/pull/4
smartquotes = False

highlight_language = 'shell'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ru'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

html_title = 'Руководство по оптимизации Arch Linux'

html_theme_options = {
    'github_user': 'ventureoo',
    'github_repo': 'ARU',
    'donate_url': 'https://www.donationalerts.com/r/pavel_priluckiy',
    'github_type': 'star',
    'github_banner': True,
    'show_powered_by': False,
}

# Misc
html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (root_doc, 'ARU', 'Arch Linux Optimization Guide (RU)',
     [author], 1)
]

# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'xelatex'

latex_elements = {
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'extraclassoptions': 'openany'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (root_doc, 'ARU.tex', 'Arch Linux Optimization Guide (RU)',
     'Arch Linux Optimization Guide (RU)', 'manual'),
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (root_doc, 'ARU', 'Arch Linux Optimization Guide (RU)',
     author, 'ARU', 'Arch Linux Optimization Guide (RU)',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False

# If false, do not generate in manual @ref nodes.
#
# texinfo_cross_references = False
