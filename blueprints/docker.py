
import flask
import docker 


blueprint = flask.Blueprint('docker', __name__)

connection = docker.DockerClient()

@blueprint.route('/docker', methods=[ 'GET' ])
def get_docker(): 

    container = connection.containers.get('42c3f08aa98d')   

    context = {
        'page': 'docker',
        'route': {
            'is_public': False
        },
        'container': container
    }

    return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/start', methods=[ 'GET' ])
def start_docker():
    
    container = connection.containers.get('42c3f08aa98d')

    if not container:
        flask.flash('Container não encontrado', 'danger')
    elif container.status != 'running':
        container.start()
        flask.flash('Container iniciado', 'success')
    else:
        flask.flash('Container já está iniciado', 'info')

    
    return flask.redirect('/docker')

@blueprint.route('/docker/stop', methods=[ 'GET' ])
def stop_docker():

    
    container = connection.containers.get('42c3f08aa98d')

    if not container:
        flask.flash('Container não encontrado', 'danger')
    elif container.status != 'running':
        container.stop()
        flask.flash('Container parado', 'success')
    else:
        flask.flash('Container já está iniciado', 'info')

    
    return flask.redirect('/docker')

