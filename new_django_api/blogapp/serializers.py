from rest_framework import serializers
from django.contrib.auth import get_user_model    # You can also import the exact name of your models.py CustomUser as well I believe


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()   # This was called "CustomUser" but he seems to be using so it intuitively knows which model or something
        fields = ["id", "email", "username", "first_name", "last_name", "password"]   # These are the default fields that django auth comes with, we might need to research if we can add more fields. Or he may have added them via another models.py class
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):     #These are apparently saying that the inputed data is equal to its field
        email = validated_data["email"]
        username = validated_data["username"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        password = validated_data["password"]

        user = get_user_model()    #This seems to just be getting and storing the user that just registered. Uses the get_user_model function to correctly pick which models.py to use
        new_user = user.objects.create(email=email, username=username, first_name=first_name, last_name=last_name)

        new_user.set_password(password)    #I guess sets the users password to whatever password they entered
        new_user.save()
        return new_user
