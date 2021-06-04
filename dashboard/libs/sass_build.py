import sass
import os
import hashlib


class SassBuild:
    mtime = None
    s256 = None

    def sass_load(self, path):
        sass_dir = 'dashboard/app/assets/scss'
        dest_dir = 'dashboard/app/static/sass_build'

        css = path.replace('.scss', '.css')
        css_path = os.path.join(dest_dir, css)
        sass_path = os.path.join(sass_dir, path)

        if not os.path.isfile(css_path):
            if not os.path.isfile(sass_path):
                return 'file_not_found'
            else:
                sass.compile(
                    dirname=(sass_dir, dest_dir),
                    output_style='compressed'
                )

        mtime = int(os.path.getmtime(css_path))

        if self.mtime != mtime:
            sass.compile(
                dirname=(sass_dir, dest_dir),
                output_style='compressed'
            )
            self.mtime = mtime
            self.s256 = hashlib.sha256(
                str(mtime).encode('utf-8')
            ).hexdigest()

        url = '/static/sass_build/' + css + '?v=' + self.s256

        return url
