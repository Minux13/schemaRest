from markupsafe import Markup, escape 
from jinja2 import Template  
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix 

@api.route('/providers')
class ProviderList(Resource):
    def get(self):
        """ 
        Procedure to obtain part of provider list for the pagination
        Read the page from the query string /providers?size=20&page=3
        """
        return {providers: {}}

    def post(self):
        """Create the provider"""
        create_provider(**kwargs)


@api.route('/providers/<int:provider_id>')
class Provider(Resource):

    def get(self, provider_id):
        """ Get a dictionary of the provider fields and send them to the client"""
        return {provider: {}}

    def put(self, provider_id):
        """Edit the provider"""
        edit_provider(**kwargs)

    def delete(self, provider_id):
        """Block the provider"""
        block_provider(provider_id)

