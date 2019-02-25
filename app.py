import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import layout
from config import GAPMINDER_PATH


app = dash.Dash(__name__)


df = pd.read_csv(GAPMINDER_PATH)
# geo, time, children_per_woman_total_fertility, working_hours_per_week
df = df[['geo', 'children_per_woman_total_fertility', 'working_hours_per_week']]
df = df[(df['working_hours_per_week'].notnull()) & (df['children_per_woman_total_fertility'].notnull())]

filter_options = [{'label': i, 'value': i} for i in df['geo'].unique()]
filter_options.insert(0, {'label': 'All', 'value': None})  # we add a filter with None value
filter_object = dcc.Dropdown(id='geo-filter', options=filter_options, style={'color': '#000'})

content_object = dcc.Graph(id='graph')

header_logo_dict = {
    'filename': '/static/SB_Logo_analytics.png',
    'width': 138.08,
}
header_links = [
    {'name': 'Pacing', 'href': '/pacing', 'className': 'header-link'},
    {'name': 'A/B Testing', 'href': '/abtesting', 'className': 'header-link'},
]
sub_header_links = [
    {'name': 'Details', 'href': '/abtesting/details', 'className': 'sub-header-link'},
    {'name': 'Funnel', 'href': '/abtesting/funnel', 'className': 'sub-header-link'},
]

header_class_name = 'header'
header_row_class_name = 'header-row'
header_links_class_name = 'header-links'
sub_header_row_class_name = 'sub-header-row'
sub_header_links_class_name = 'sub-header-links'
sidebar_and_content_class_name = 'sidebar-and-content'
sidebar_filters = [filter_object]
content_objects = [content_object]

app.layout = layout.create_layout(
    page_wrapper_class_name='dashboard-wrapper',
    header_class_name=header_class_name,
    header_row_class_name=header_row_class_name,
    header_logo_dict=header_logo_dict,
    header_links=header_links,
    header_links_class_name=header_links_class_name,
    sub_header_row_class_name=sub_header_row_class_name,
    sub_header_filters=None,
    sub_header_links=sub_header_links,
    sub_header_links_class_name=sub_header_links_class_name,
    sidebar_and_content_class_name=sidebar_and_content_class_name,
    sidebar_class_name='sidebar',
    sidebar_filters=sidebar_filters,
    sidebar_filter_headers=None,
    sidebar_filter_headers_class_name=None,
    sidebar_filter_wrapper_class_name=None,
    content_class_name='content',
    content_objects=content_objects,
)


@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('geo-filter', 'value')]
)
def filter_and_graph(geo_input):
    filtered_df = df
    geo_input = geo_input
    if geo_input is not None:
        filtered_df = filtered_df[filtered_df['geo'] == geo_input]

    x = filtered_df['working_hours_per_week']
    y = filtered_df['children_per_woman_total_fertility']

    return go.Figure(
        data=[
            go.Scatter(x=x, y=y)
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=True)
