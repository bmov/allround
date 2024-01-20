from flask_restx import Resource, Namespace

ApiRoot = Namespace('ApiRoot')


@ApiRoot.route('/hello')
class HelloIndex(Resource):
    def get(self):
        """
        Testing activity
        """

        return {
            'hello': 'hello world from api_v1'
        }
