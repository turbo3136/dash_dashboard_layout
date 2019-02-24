import dash_html_components as html


def create_header(sub_header_list=None):
    return html.Div(
        className='header',
        children=[
            html.Div(className='header-row', children='First Row'),
            html.Div(className='header-row', children='Second Row'),
        ]
    )
