import json
import requests
import yaml
from jsonschema import validate, ValidationError

import quart
import quart_cors
from quart import request

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

# Store the schema here after fetching
_SCHEMA = None

def fetch_schema_from_url():
    response = requests.get('https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json')
    return response.json()

def fetch_official_kubernetes_schema():
    global _SCHEMA
    if _SCHEMA is None:
        _SCHEMA = fetch_schema_from_url()
    return _SCHEMA

def fetch_resource_names(resourceName):
    schema = fetch_official_kubernetes_schema()
    resourceNames = [k for k in schema['definitions'].keys() if resourceName.lower() in k.lower()]
    return resourceNames

def fetch_schema_for_resource(resourceType):
    schema = fetch_official_kubernetes_schema()
    if resourceType in schema['definitions']:
        return schema['definitions'][resourceType]
    else:
        return None

def validate_yaml(resourceType, yml):
    try:
        data = yaml.safe_load(yml)
        validate(instance=data, schema=fetch_official_kubernetes_schema())
        return {"isValid": True, "error": None}
    except ValidationError as e:
        return {"isValid": False, "error": str(e)}

@app.get("/schemas/search/<string:resourceName>")
async def find_schema_names(resourceName):
    resourceNames = fetch_resource_names(resourceName)
    return quart.Response(response=json.dumps(resourceNames), status=200)

@app.get("/schemas/resource/<string:resourceType>")
async def get_schema(resourceType):
    schema = fetch_schema_for_resource(resourceType)
    return quart.Response(response=json.dumps(schema), status=200)

@app.post("/validate-yaml")
async def validate_yaml_route():
    request_data = await quart.request.get_json(force=True)
    resourceType = request_data["resourceType"]
    yaml = request_data["yml"]
    result = validate_yaml(resourceType, yaml)
    return quart.Response(response=json.dumps(result), status=200)

@app.get("/kubernetes-logo.png")
async def plugin_logo():
    filename = 'kubernetes-logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()