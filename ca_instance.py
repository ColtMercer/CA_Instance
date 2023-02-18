from rest_framework import serializers, viewsets
from nautobot.dcim.models import Device
from nautobot.extras.models import Relationship
from nautobot.extras.api.views import (
    RelationshipViewSet,
    ObjectChangeLogViewSet,
)
from nautobot.extras.api.serializers import (
    RelationshipSerializer,
    ObjectChangeLogSerializer,
)
from nautobot.core.api.views import ModelViewSet
from nautobot.utilities.api import FieldChoicesViewSet

from .models import ComponentArchitectures, CAType, CAInstance


class ComponentArchitecturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentArchitectures
        fields = ["id", "name", "description", "gnast_standard"]


class ComponentArchitecturesViewSet(ModelViewSet):
    queryset = ComponentArchitectures.objects.all()
    serializer_class = ComponentArchitecturesSerializer


class CATypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAType
        fields = ["id", "name", "description", "abbreviation"]


class CATypeViewSet(ModelViewSet):
    queryset = CAType.objects.all()
    serializer_class = CATypeSerializer


class CAInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAInstance
        fields = ["id", "region", "site", "ca_type", "ca_instance_number", "batfish_snapshot", "netbrain_diagram"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["name"] = instance.name
        return data


class CAInstanceViewSet(ModelViewSet):
    queryset = CAInstance.objects.all()
    serializer_class = CAInstanceSerializer


class CAInstanceRelationshipSerializer(RelationshipSerializer):
    ca_instance = CAInstanceSerializer()

    class Meta(RelationshipSerializer.Meta):
        fields = ["id", "relationship", "ca_instance"]


class CAInstanceDeviceRelationshipViewSet(RelationshipViewSet):
    queryset = Relationship.objects.filter(type="ca_instance_device")
    serializer_class = CAInstanceRelationshipSerializer


class CAInstanceComponentArchitectureRelationshipViewSet(RelationshipViewSet):
    queryset = Relationship.objects.filter(type="ca_instance_componentarchitecture")
    serializer_class = CAInstanceRelationshipSerializer


class FieldChoicesAPIView(FieldChoicesViewSet):
    fields = [
        {
            "name": "catypes",
            "model": CAType,
            "field": "name",
        },
        {
            "name": "regions",
            "model": Device.region.field.related_model,
            "field": "name",
        },
        {
            "name": "sites",
            "model": Device.site.field.related_model,
            "field": "name",
        },
    ]


class ObjectChangeLogCAInstanceViewSet(ObjectChangeLogViewSet):
    """
    Retrieve the ObjectChangeLog for the CA Instance model
    """

    queryset = CAInstance.objects.all()
    serializer_class = ObjectChangeLogSerializer
