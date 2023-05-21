# ChatGPT Kubernetes Generation Plugin

This plugin gives ChatGPT up-to-date knowledge of every Kubernetes resource and their full specification. It lets ChatGPT query the [official Kubernetes OpenAPI (swagger) schema](https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json) to lookup resources and see how to define them. It also provides ChatGPT with a schema validation function for every Kubernetes resource.

# Key Features
1. **Schema Lookup:** The `GET /schemas/search/{resourceName}` endpoint retrieves fully-namespaced names for Kubernetes resources. For instance, a search for 'Container' will yield 'io.k8s.api.core.v1.Container'.

2. **Schema Retrieval:** The `GET /schemas/resource/{resourceType}` endpoint fetches the latest OpenAPI schemas for Kubernetes resources using fully-namespaced resource names.

3. **YAML Validation:** The `POST /validate-yaml` endpoint validates generated Kubernetes YAML manifests, guaranteeing their accuracy.

## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a question like "What is on my todo list" and then try adding something to it as well! 

## Getting help

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
