import datetime

project = "An example of bulma sphinx theme without navbar"
author = "zclab"
year = str(datetime.date.today().year)
copyright = year + " " + author
master_doc = "index"
language = "en"  #'zh_CN'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinx_subfigure",
    # "myst_parser",
    # "ablog",
    # "jupyter_sphinx",
    "myst_nb",
    "matplotlib.sphinxext.plot_directive",
]


myst_enable_extensions = ["colon_fence", "deflist"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.9", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "markdown_it": ("https://markdown-it-py.readthedocs.io/en/latest", None),
}

templates_path = ["_templates"]

html_static_path = ["_static"]
html_theme = "bulma_sphinx_theme"
html_title = "An example of bulma sphinx theme without navbar"
html_favicon = "_static/favicon.png"
html_last_updated_fmt = ""
html_logo = "_static/logo.svg"
html_show_sourcelink = True

todo_include_todos = True

# https://github.com/hung1001/font-awesome-pro-v6
# html_css_files = [
#     "https://cdn.jsdelivr.net/gh/duyplus/fontawesome-pro/css/all.min.css",
# ]

html_theme_options = {
    "logo": {"text": "BST Demo", "logo": "_static/logo.svg"},
    "icon_links": [
        {
            "name": "Github",
            "url": "https://github.com/zclab/bst-nonavbar",
            "svg": "github",
        },
        {
            "name": "Pypi",
            "url": "https://pypi.org/project/bulma-sphinx-theme/",
            "svg": "package",
        },
    ],
    "source_repository": "https://github.com/zclab/bst-nonavbar",
    "source_branch": "main",
    "source_directory": "docs/",
    "use_edit_page_button": True,
    "information_panel": ["brand-logo.html", "search-button.html", "theme-swither.html", "icon-links.html"],
    "information_panel_include_directly":["brand-logo.html"],
    "have_top_navbar": False,
}

html_context = {"default_mode": "auto"}
