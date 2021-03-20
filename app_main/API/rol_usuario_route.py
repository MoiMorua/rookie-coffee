from flask import Blueprint
from flask import jsonify, request
from nucleo.controlador import controlador_rol_usuario

rol_usuario_route = Blueprint("rol_usuario_route", __name__,url_prefix='/rol-usuario')


@rol_usuario_route.route('/agregar', methods=['POST'])
def agregar():
    try:
        if controlador_rol_usuario.agregar(
                request.json["nombre"],
                request.json["descripcion"]
            ):
            return jsonify({
                    "estado" : "OK",
                    "mensaje": "Rol registrado correctamente"
                })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al agregar el registro! Por favor verificalo con un administrador o revisa tu solicitud"    
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })

    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al agregar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })


@rol_usuario_route.route('/modificar', methods=['POST'])
def modificar():
    try:
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de rol para modificar"
            })
        if controlador_rol_usuario.modificar(
                request.json["_id"],
                request.json["nombre"],
                request.json["descripcion"]
            ):
            return jsonify({
                    "estado" : "OK",
                    "mensaje": "Rol modificado correctamente"
                })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"    
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })

    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })

@rol_usuario_route.route('/desactivar', methods = ["POST"])
def desactivar():
    try:    
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de rol para desactivar"
            })
        if controlador_rol_usuario.desactivar(request.json["_id"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Rol desactivado correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al desactivar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })

@rol_usuario_route.route('/reactivar', methods = ["POST"])
def reactivar():
    try:    
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de rol para reactivar"
            })
        if controlador_rol_usuario.reactivar(request.json["_id"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Rol reactivado correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al reactivado el registro! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al reactivado el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })


@rol_usuario_route.route('/consultar', methods=['POST'])
def consultar():
    estado = "OK"
    mensaje = "Información consultada correctamente"

    try:
        print(request.json)
        print("_id" not in request.json)

        if "_id" not in request.json or request.json["_id"] == 0:
            print("test")
            roles = controlador_rol_usuario.consultar(0)
            if len(roles)>0:
                roles_json = []
                for rol in roles:
                    rol_dictionary = rol.__dict__
                    del rol_dictionary['_sa_instance_state']
                    roles_json.append(rol_dictionary)
                return jsonify(roles_json)            
        else:
            rol = controlador_rol_usuario.consultar(request.json["_id"])
            if rol is None:
                return jsonify({
                    "estado" : "ADVERTENCIA",
                    "mensaje": "No se encontro un rol con el id especificado"
                })
            rol_dictionary = rol.__dict__
            del rol_dictionary['_sa_instance_state']

            return jsonify(rol_dictionary)

            
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion": str(e)
        })

