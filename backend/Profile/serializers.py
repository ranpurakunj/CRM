from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Profile
import re


def phone_validator(value):
    if value is None:
        return value
    reg_ex= '^(\+\d{1,3})?,?\s?\d{8,13}$' 
    if not re.match(reg_ex,value):
        raise serializers.ValidationError(f"{value} is not a valid phone number")
    return value

class ProfileSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name="profile-detail",
        lookup_field='pk'
        )
    first_name=serializers.CharField(max_length=30, allow_blank=True)
    last_name =serializers.CharField(max_length=30, allow_blank=True)
    email=serializers.EmailField(allow_blank=True)
    phone=serializers.CharField(validators=[phone_validator], allow_blank=True)
    class Meta:
        model = Profile
        fields=[
        "url",
        "edit_url",
        "pk",
        "first_name", 
        "last_name", 
        "birth_date", 
        "address1", 
        "address2", 
        "city", 
        "county", 
        "state", 
        "zipcode", 
        "phone",
        "email",
        ]
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("profile-edit", kwargs={"pk": obj.pk}, request=request)

    def validate(self, data):
        constraint1 = (data['first_name']=="" or data['last_name']=="") 
        constraint2 = data['email']==""
        constraint3 = data['phone']==""
        if constraint1 and constraint2 and constraint3:
            print("1",constraint1)
            print("2",constraint2)
            print("3",constraint3)
            raise serializers.ValidationError(f"Please enter one of the following:" 
            f"1. First and Last Name."
            f"2. Your email address."
            f"3. Your Phone number.")
        if not data['first_name'].isalpha():
            raise serializers.ValidationError(f"Please Enter valid First Name")
        if not data['last_name'].isalpha():
            raise serializers.ValidationError(f"Please Enter valid Last Name")
        if not (all(idx.isdigit() for idx in data['zipcode'])):
            raise serializers.ValidationError(f"Please Enter valid zipcode")
        return data
    
