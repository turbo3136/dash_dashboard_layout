import dash_html_components as html
from building_blocks import header


def create_layout(
        page_wrapper_class_name,
        header_class_name=None,
        header_row_class_name=None,
        header_logo_dict=None,
        header_links=None,
        header_links_class_name=None,
        sub_header_row_class_name=None,
        sub_header_filters=None,
        sub_header_links=None,
        sub_header_links_class_name=None,
        sidebar_and_content_class_name=None,
        sidebar_class_name=None,
        sidebar_filters=None,  # list of dcc filter objects
        sidebar_filter_headers=None,  # optional headers for the filters
        sidebar_filter_headers_class_name=None,
        sidebar_filter_wrapper_class_name=None,
        content_class_name=None,
        content_objects=None,
):
    wrapper_children = []  # this is the list of objects for our overall page wrapper

    # create the header
    header_object = header.create_header(
        header_class_name=header_class_name,
        header_row_class_name=header_row_class_name,
        header_logo_dict=header_logo_dict,
        header_links=header_links,
        header_links_class_name=header_links_class_name,
        sub_header_row_class_name=sub_header_row_class_name,
        sub_header_filters=sub_header_filters,
        sub_header_links=sub_header_links,
        sub_header_links_class_name=sub_header_links_class_name,
    )
    wrapper_children.append(header_object)

    sidebar_and_content_children = []  # here's where we'll stuff the sidebar and content objects

    # create the sidebar if we listed any filters
    if sidebar_filters:
        if sidebar_filter_headers:  # if we have filters and headers, create a wrapper around the filters
            sidebar_objects = [  # comprehend the headers and filters
                html.Div(
                    className=sidebar_filter_wrapper_class_name,
                    children=[
                        html.Div(className=sidebar_filter_headers_class_name, children=sidebar_filter_headers[index]),
                        sidebar_filters[index],
                    ]
                )
                for index, element in enumerate(sidebar_filters)
            ]
        else:  # if we don't have any headers, just use the filters without headers
            sidebar_objects = sidebar_filters

        # then wrap the objects in the wrapper class
        sidebar = html.Div(className=sidebar_class_name, children=sidebar_objects)
        sidebar_and_content_children.append(sidebar)

    # create the content
    content = html.Div(className=content_class_name, children=content_objects)
    sidebar_and_content_children.append(content)

    # create the sidebar and content, filling in the sidebar and content objects
    sidebar_and_content_object = html.Div(
        className=sidebar_and_content_class_name,
        children=sidebar_and_content_children,
    )
    wrapper_children.append(sidebar_and_content_object)

    return html.Div(className=page_wrapper_class_name, children=wrapper_children)
