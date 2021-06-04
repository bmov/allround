from dashboard.libs.sass_build import SassBuild
from dashboard.libs.render import render

sass = SassBuild()


def index():
    global sass
    index_tpl = render('default/index')

    reset_css = '/static/css/reset.css'
    index_css = sass.sass_load('index.scss')

    css_files = [
        {
            "css_href": reset_css
        },
        {
            "css_href": index_css
        }
    ]

    return render('default/_default', default_body=index_tpl,
                  head_css_files=css_files)
