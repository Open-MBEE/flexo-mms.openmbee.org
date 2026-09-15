# Python

## SysML v2 Python client

A Python client for the [SysML v2 API](../services/sysmlv2.md), tested against Flexo.

- Repository: [Open-MBEE/sysmlv2-python-client](https://github.com/Open-MBEE/sysmlv2-python-client)

It covers the core of the standard:

| Resource | Operations |
| --- | --- |
| Projects | list, create, get |
| Commits | create (element create, update and delete in one change), get, list |
| Branches | list, create, get, delete |
| Tags | list, create, get, delete |
| Elements | get, list all at a commit, list owned by an element |
| Relationships | list for an element |

Authentication is a bearer token; errors surface as `SysMLV2Error`.

```python
from sysmlv2_client import SysMLV2Client

client = SysMLV2Client(base_url="http://localhost:8083",
                       bearer_token="Bearer …")

for project in client.get_projects():
    print(project["name"], project["@id"])

project = client.create_project({"@type": "Project", "name": "Example"})
```

The package is installed from the repository rather than PyPI.

## flexo_syside

[flexo_syside](https://github.com/Open-MBEE/flexo_syside) bridges SysML v2 **textual
notation** and Flexo through [SysIDE](https://sensmetry.com/syside/): it serialises a
`.sysml` file or string into a commit for a Flexo SysML v2 project, and deserialises
Flexo's JSON responses back into SysIDE Python objects — so a model can be read from Flexo,
navigated as objects or rendered as text, edited, and written back. It builds on the
Python client above and was contributed by
[Planetary Utilities Corp](https://www.planetaryutilities.com/). The repository's
`examples/basic_notebook.ipynb` is the tour.
