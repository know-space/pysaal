import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

project = "PySAAL"
copyright = f"2024-{date.today().year}, KnowSpace"
author = "Brandon Sexton"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.autosectionlabel",
    "sphinx_autodoc_typehints",
    "sphinx_markdown_builder",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
    "sphinx_gallery.gen_gallery",
    "sphinx.ext.viewcode",
]

html_show_sourcelink = False

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_extra_path = ["SGP4_Open_License.txt"]
html_baseurl = "https://know-space.github.io/pysaal/"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
add_module_names = False
todo_include_todos = True

# Gallery options
sphinx_gallery_conf = {
    "gallery_dirs": ["gallery"],
    "examples_dirs": ["../../examples"],
    "filename_pattern": "/*.py",
    "download_all_examples": False,
    "image_scrapers": ["matplotlib"],
    "matplotlib_animations": True,
    "thumbnail_size": (333, 250),
    "image_srcset": ["2x"],
}
