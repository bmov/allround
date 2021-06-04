import htmlmin
from flask_stache import render_template


def render(template, **context):
    return htmlmin.minify(render_template(template, **context),
                          remove_comments=False, remove_empty_space=False,
                          remove_all_empty_space=False,
                          reduce_empty_attributes=True)
