import dash_html_components as html


def create_links(link_wrapper_class_name, links_list):
    links_inner = []
    for link_dict in links_list:
        links_inner.append(
            html.A(  # the A object is the link that contains our Div with the text
                href=link_dict['href'],
                children=[html.Div(className=link_dict['className'], children=link_dict['name'])]
            )
        )

    # create the wrapper around our links and return
    return html.Div(className=link_wrapper_class_name, children=links_inner)


"""
create_header
it, uh, creates the header. Its inputs are:
    header_logo_dict={
        'filename': filepath (e.g. /static/filename.png) or url,
        'width': img width,
    },
    header_links=[
        {
            'name': text that will appear,
            'href': link,
            'className': class_name for Div object, 
        },
        {}, ...
    ],
    sub_header_filters=[  <-- these should come pre-loaded with class info and all that jazz
        filter_object (dash_core_components object for the filter),
        ...
    ],
    sub_header_links=[
        {
            'name': text that will appear,
            'href': link,
            'className': class_name for Div object, 
        },
        {}, ...
    ]
"""


def create_header(
        header_class_name=None,
        header_row_class_name=None,
        header_logo_dict=None,
        header_links=None,
        header_links_class_name=None,
        sub_header_row_class_name=None,
        sub_header_filters=None,
        sub_header_links=None,
        sub_header_links_class_name=None,
):
    header_objects_list = []  # list for the first row of our header
    sub_header_objects_list = []  # list for the second row of our header
    include_sub_header = False
    header_children = []

    if header_logo_dict:  # if we want a logo, add it to the list
        header_objects_list.append(html.Img(src=header_logo_dict['filename'], width=header_logo_dict['width']))

    if header_links:  # if we want header links, add them. This requires a wrapper around the links
        links = create_links(link_wrapper_class_name=header_links_class_name, links_list=header_links)
        header_objects_list.append(links)

    # add the header's first row
    header_children.append(html.Div(className=header_row_class_name, children=header_objects_list))

    if sub_header_filters:  # if we want filters in the sub header, add them
        include_sub_header = True
        sub_header_objects_list.extend(sub_header_filters)

    if sub_header_links:
        include_sub_header = True
        links = create_links(link_wrapper_class_name=sub_header_links_class_name, links_list=sub_header_links)
        sub_header_objects_list.append(links)

    if include_sub_header:  # if we have any sub header objects, add them to the second row
        header_children.append(html.Div(className=sub_header_row_class_name, children=sub_header_objects_list))

    return html.Div(className='header-wrapper', children=html.Div(className=header_class_name, children=header_children))
