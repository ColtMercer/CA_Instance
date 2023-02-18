PLUGINS = ["ca_instance"]

# Add the following views to the API and GraphQL
API_EXTENSIONS = [
    "ca_instance.api.ComponentArchitecturesViewSet",
    "ca_instance.api.CATypeViewSet",
    "ca_instance.api.CAInstanceViewSet",
    "ca_instance.api.CAInstanceDeviceRelationshipViewSet",
    "ca_instance.api.CAInstanceComponentArchitectureRelationshipViewSet",
    "ca_instance.api.ObjectChangeLogCAInstanceViewSet",
]

# Add the following views to the API only
API_VIEWS = [
    "ca_instance.api.FieldChoicesAPIView",
]
