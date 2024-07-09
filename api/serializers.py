from rest_framework import serializers
from.models import Student


class StudentSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    names =  serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    

    def validate(self, attrs):
        names = attrs.get('names')
        email = attrs.get('email')
        address = attrs.get('address')
        phone = attrs.get('phone')
        age = attrs.get('age')
        
        errors = {}
        
        if len(names) <= 4:
            errors['names'] = ["names must be more than 4 characters."]
           
           
        if not email:
            errors['email'] = ["email is required."]
            
            
        if not address:
            errors['address'] = ["address is required."]
           
    
        if not phone:
            errors['phone'] = ["phone is required."]
            
            
        if not age:
            errors['age'] = ["age is required."]
            
        if errors:
            raise serializers.ValidationError(errors)
        
        return attrs

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        #print(validated_data, "validated data")
        print(vars(instance),"instance__dict__")#only work for instances with a __dict__ attribute
        #print(dir(instance), "instance dir()")#lists all attributes and method
        instance.names = validated_data.get("names",instance.names)
        instance.email = validated_data.get("email",instance.email)
        instance.address = validated_data.get("address",instance.address)
        instance.phone = validated_data.get("phone",instance.phone)
        instance.age = validated_data.get("age",instance.age)
        instance.save()
        return instance