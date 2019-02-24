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

    # create the sidebar and content
    sidebar_and_content_object = html.Div(className=sidebar_and_content_class_name)
    wrapper_children.append(sidebar_and_content_object)

    return html.Div(className=page_wrapper_class_name, children=wrapper_children)
