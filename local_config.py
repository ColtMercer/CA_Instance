PLUGINS = ["my_plugin"]

# Add the following views to the API and GraphQL
API_EXTENSIONS = [
    "my_plugin.api.ComponentArchitecturesViewSet",
    "my_plugin.api.CATypeViewSet",
    "my_plugin.api.CAInstanceViewSet",
    "my_plugin.api.CAInstanceDeviceRelationshipViewSet",
    "my_plugin.api.CAInstanceComponentArchitectureRelationshipViewSet",
    "my_plugin.api.ObjectChangeLogCAInstanceViewSet",
]

# Add the following views to the API only
API_VIEWS = [
    "my_plugin.api.FieldChoicesAPIView",
]
