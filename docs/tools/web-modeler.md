# SysML v2 Web Modeler

The Web Modeler is a standalone Java web service for graphical rendering and textual
editing of SysML v2 models, against any [SysML v2 API](../services/sysmlv2.md) backend.
The browser talks only to the service, and the service talks to the API, so it can sit
behind JupyterLab or another proxy without the browser needing a route to the model
server.

- Repository: [Open-MBEE/sysmlv2-web-modeler](https://github.com/Open-MBEE/sysmlv2-web-modeler)

## Two views

| Path | View |
| --- | --- |
| `/` | The **graphical visualizer**: pick a project and branch, render diagrams |
| `/editor` | The **textual editor**: load a project as SysML v2 text, edit, validate, commit; create projects |

Behind them, HTTP endpoints cover rendering, textual load and readback, validation, full
replacement commits, parsed-JSON export from the bundled Pilot implementation, element list
download from the live API, and project and branch listing and creation.

## Deployment modes

- **standalone** — the user enters the backend URL and bearer token in the UI.
- **embedded** — for an iframe in JupyterLab or a similar shell; the backend URL and token
  come from environment variables and the UI hides the fields.

The Docker image bundles the Java server, the SysML v2 Pilot implementation jars, the
`sysml.library` standard library, and a Python runtime for the commit and project-creation
bridge scripts.
