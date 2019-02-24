import dash
import layout


app = dash.Dash(__name__)

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
)

if __name__ == '__main__':
    app.run_server(debug=True)
