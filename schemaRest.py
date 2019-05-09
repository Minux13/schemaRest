from flask import Flask
from markupsafe import Markup, escape 
from jinja2 import Template  
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix 

app = Flask(__name__)
api = Api(app, version='1.0', title='Obras API',
    description='Sistema de Control de Gastos de Obras Publicas',
)

@api.route('/contratos')
class Contracts(Resource):
    def get(self):
        """
        Procedure to obtain part of contract list for the pagination
        Read the page from the query string /contratos?size=20&page=3
        """
        return {contracts: {}}

    def post(self):
        """Create the contract"""
        create_contract(**kwargs)


@api.route('/contrato/<int:contract_id>')
class Contract(Resource):

    def get(self, contract_id):
        """Get a dictionary of the contract fields and send them to the client"""
        return {contract: {}}

    def put(self, contract_id):
        """Edit the contract by Id"""
        edit_contract(**kwargs)

    def delete(self, contract_id):
        """Block the contract"""
        block_contract(contract_id)


@api.route('/proyectos')
class Projects(Resource):
    def get(self):
        """ 
        Procedure to obtain part of project list for the pagination
        Read the page from the query string /proyectos?size=20&page=3
        """
        return {projects: {}}

    def post(self):
        """Create the project"""
        create_project(**kwargs)


@api.route('/proyecto/<int:project_id>')
class Project(Resource):

    def get(self, project_id):
        """ Get a dictionary of the project fields and send them to the client"""
        return {project: {}}

    def put(self, project_id):
        """Edit the contract"""
        edit_project(**kwargs)

    def delete(self, project_id):
        """Block the project"""
        block_project(project_id)



if __name__ == '__main__':
    app.run(debug=True)
