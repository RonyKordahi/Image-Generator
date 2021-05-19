from flask import Flask, request, render_template
import json
import flask_ipywidgets
import ipywidgets

# app = Flask("image_generator")
app = flask_ipywidgets.app()

@app.route('/', methods=['GET'])
def model_info():
    """
    Returns expected input format
    """    
    base_image_uploader = ipywidgets.FileUpload(accept="image/*", multiple=False)

    return render_template('example1.html', slider1=base_image_uploader, widgets=[base_image_uploader])

@app.route('/', methods=['POST'])
def model_computation_main():
    """
    Main Model server round trip method
    """
    try:
        return json.dumps({"result": 3})
    except ValueError as ex:  # failed schema/values validation
        return json.dumps({ "Incorrect JSON format:\n": str(ex)})
    except Exception as ex:
        return json.dumps({ "Server Error:\n": str(ex)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)