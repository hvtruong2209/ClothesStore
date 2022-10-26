from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        get_user = {
            'email': user.email,
            'name': user.name,
        }
        # role
        token['user'] = get_user
        return token