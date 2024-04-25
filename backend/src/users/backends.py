from rest_framework_simplejwt.authentication import JWTAuthentication

class CookieJWTAuthentication(JWTAuthentication):
    """
    JWT authentication class that extracts the JWT token from the request's cookies.

    Attributes:
        user_model: The user model class associated with the authentication.
    """

    def authenticate(self, request):
        """
        Authenticates the user based on the JWT token extracted from the request's cookies.

        Args:
            request: The HTTP request object.

        Returns:
            Tuple containing the user object and the validated JWT token if authentication succeeds,
            otherwise returns None.
        """
        header = self.get_header(request)
        if header is None:
            raw_token = request.COOKIES.get('accessToken')  # This fetches the JWT token from the cookie
            if raw_token is None:
                return None
            validated_token = self.get_validated_token(raw_token)
            if validated_token:
                user_id = validated_token.get("user_id")  
                if user_id:
                    user = self.user_model.objects.get(id=user_id)  # Fetch user by user_id
                    return (user, validated_token)
        return super().authenticate(request)


