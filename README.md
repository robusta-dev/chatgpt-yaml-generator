<div id="top"></div>

<div align="center">
  <img src="./screenshot.png" />

  <h2>ChatGPT Kubernetes YAML Plugin by <a href="https://home.robusta.dev/">Robusta</a></h2>
    <h3>A ChatGPT plugin to generate accurate Kubernetes manifests</h3>

  [![twitter robusta](https://img.shields.io/twitter/follow/RobustaDev?logo=twitter&color=blue&label=@RobustaDev&style=flat-square)](https://twitter.com/RobustaDev)
  [![slack robusta](https://img.shields.io/badge/Slack-Join-4A154B?style=flat-square&logo=slack&logoColor=white)](https://bit.ly/robusta-slack)
 <a href="https://www.linkedin.com/company/robusta-dev/"><img alt="LinkedIn" title="LinkedIn" src="https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white"/></a>
  <a href="https://www.youtube.com/channel/UCeLrAOI3anJAfO3BrYVB62Q"><img alt="Youtube" title="Youtube" src="https://img.shields.io/youtube/channel/subscribers/UCeLrAOI3anJAfO3BrYVB62Q?color=%23ff0000&label=Robusta%20Dev&logo=youtube&logoColor=%23ff0000&style=flat-square"/></a>

</div>

This plugin gives ChatGPT up-to-date knowledge of every Kubernetes resource and their complete specifications. It lets ChatGPT query the [Kubernetes OpenAPI (swagger) schema](https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json) to fetch resource definitions. Additionally, it provides ChatGPT with schema validation capabilities.

<a href="https://www.loom.com/share/ff472bbdb9494ef4aca1c3f23dee8742">
    <img src="https://cdn.loom.com/sessions/thumbnails/ff472bbdb9494ef4aca1c3f23dee8742-with-play.gif">
  </a>
  
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
4. Select "Develop your own plugin" (ChatGPT Plus is required right now)
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! Watch the video above for ideas on using the plugin.

## Getting help

Join the [Robusta Slack Community](https://bit.ly/robusta-slack) and ask for help.
