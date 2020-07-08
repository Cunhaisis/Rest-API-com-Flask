from flask_restful import  Resource

habilidades = ['Python', 'Java', 'Flask', 'Jquery']
class Habilidades(Resource):
    def get(self):
        return habilidades