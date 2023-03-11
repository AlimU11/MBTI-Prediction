import pkgutil

import dash
import dash_bootstrap_components as dbc

import pages
from utils.shared_callbacks import *

app = dash.Dash(
    __name__,
    pages_folder='',
    use_pages=True,
    external_stylesheets=[dbc.icons.FONT_AWESOME, dbc.themes.BOOTSTRAP],
)

for module in pkgutil.iter_modules(pages.__path__):
    module = getattr(pages, module.name)
    module_name = module.__name__.replace('pages.', '')
    dash.register_page(
        module_name,
        path='/' + module_name if module_name != 'index' else '/',
        layout=module.layout,
    )

app.layout = dash.page_container

if __name__ == '__main__':
    app.run_server(debug=True)
