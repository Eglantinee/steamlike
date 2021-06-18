from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Profile
from books.models import BookHasUser, Comment
from django.contrib.auth.password_validation import validate_password as check_password
from books.serializers import BookInfoSerializer
import datetime


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_password(self, password):
        check_password(password)
        return password

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {"email": {'required': True, 'allow_null': False}}


class UserBuildInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_login', 'date_joined', 'email')


class UserInfoSerializer(serializers.ModelSerializer):
    user = UserBuildInfoSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'nickname', 'sex', 'birthday', 'balance',)


class UserUpdateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class ProfileUpdateInfoSerializer(serializers.ModelSerializer):
    user = UserUpdateInfoSerializer()

    def update(self, instance, validated_data):
        try:
            user_data = validated_data.pop('user')
            user = instance.user
            user.email = user_data.get('email', user.email)
            user.save()
        except KeyError:
            pass

        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()
        return instance

    class Meta:
        model = Profile
        exclude = ('balance',)


class UserStoredBooksSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data.update({"date": datetime.datetime.now(), "price": validated_data['book'].price})
        return BookHasUser.objects.create(**validated_data)

    class Meta:
        model = BookHasUser
        fields = '__all__'


class UserLibrarySerializer(serializers.ModelSerializer):
    book = BookInfoSerializer(read_only=True)

    class Meta:
        model = BookHasUser
        fields = '__all__'


class ChangeUserBalanceSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance

    class Meta:
        model = Profile
        fields = ('balance',)


class ProfileNicknameSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return Profile.objects.filter(user=value)[0].nickname


class CommentSerializer(serializers.ModelSerializer):
    user = ProfileNicknameSerializer(read_only=True)

    def create(self, validated_data):
        validated_data.update({"date": datetime.datetime.now()})
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.date = datetime.datetime.now()
        instance.save()
        return instance

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {"text": {'required': True, 'allow_null': False}}
