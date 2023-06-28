from rest_framework import serializers

from play_store.models import AppPackage, AppDetails, AppComments


class AppPackageListSerializer(serializers.ModelSerializer):
    """
    Serializer to  list App Packages
    """
    class Meta:
        model = AppPackage
        fields = ["id", "package_name"]

class AppCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppComments
        fields = "__all__"


class AppDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer to  list App Packages
    """
    comments = serializers.SerializerMethodField()

    class Meta:
        model = AppDetails
        fields= ['id','title','description','developerAddress','summary','installs','install_count','score',
                 'ratings','reviews','developerId','version','video','icon','developerWebsite','privacyPolicy',
                 'genre','developer','free','price','comments']

    def get_comments(self,obj):
        return AppCommentsSerializer(obj.app_details.all(),many=True).data