from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from twilio.base.exceptions import TwilioRestException
from rest_framework import filters
from utils.utils import user_detail
from .models import PhoneToken, User
from .serializers import (
    PhoneTokenCreateSerializer, PhoneTokenValidateSerializer, CheckUsernameAvailabilitySerializer, AddDetailsSerializer,
    SearchViewSerializer, ProfileSerializer
)


class GenerateOTP(CreateAPIView):
    """ generate otp or send otp for login """
    # queryset = PhoneToken.objects.all()
    serializer_class = PhoneTokenCreateSerializer

    def post(self, request, format=None, **kwargs):
        # Get the patient if present or result None.
        print('request', request.data)
        ser = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        if ser.is_valid():
            try:
                token = PhoneToken.create_otp_for_number(
                    request.data.get('phone_number')
                )
                if token:
                    phone_token = self.serializer_class(
                        token, context={'request': request}
                    )
                    data = phone_token.data
                    data['token_id'] = token.token_id
                    if getattr(settings, 'PHONE_LOGIN_DEBUG', False):
                        data['debug'] = token.otp
                    return Response(data)
                return Response({
                    'reason': "you can not have more than {n} attempts per day, please try again tomorrow".format(
                        n=getattr(settings, 'PHONE_LOGIN_ATTEMPTS', 10))}, status=status.HTTP_403_FORBIDDEN)
            except TwilioRestException as e:
                return Response({'reason': "Please enter a valid mobile no.", 'error': str(e)},
                                status=status.HTTP_200_OK, )
        return Response(
            {'reason': ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)


class ValidateOTP(CreateAPIView):
    """ validate otp """
    queryset = PhoneToken.objects.all()
    serializer_class = PhoneTokenValidateSerializer

    def post(self, request, format=None, **kwargs):
        # Get the patient if present or result None.
        ser = self.serializer_class(
            data=request.data, context={'request': request}
        )
        if ser.is_valid():
            token_id = request.data.get("token_id")
            otp = request.data.get("otp")
            try:
                user = authenticate(request, token_id=token_id, otp=otp)
                login(request, user)

                response = user_detail(user)
                return Response(response, status=status.HTTP_200_OK)
            except ObjectDoesNotExist as e:
                print("error => ",e)
                return Response(
                    {'reason': "OTP doesn't exist. Please enter valid OTP"},
                    status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
                )
        return Response(
            {'reason': ser.errors}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class CheckUsernameAvailability(CreateAPIView):
    """ check user name is available or not """
    serializer_class = CheckUsernameAvailabilitySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        # print('data', request.data)
        ser = self.serializer_class(
            data=request.data, context={'request': request}
        )
        if ser.is_valid():
            return Response(True, status=status.HTTP_200_OK)
        return Response(False, status=status.HTTP_226_IM_USED)


class AddUserDetailsView(CreateAPIView):
    """  only for first time login """
    """ it will add new user in user details table """
    permission_classes = [IsAuthenticated]
    serializer_class = AddDetailsSerializer
    queryset = User.objects.all()

    def post(self, request, **kwargs):
        # print('data', request.data)
        ser = self.serializer_class(
            data=request.data, context={'request': request}
        )
        if ser.is_valid() or True:
            user = User()
            user.username = request.data.get('username')
            user.name = request.data.get('name')
            profile_image = request.data.get('profile_image')
            profile_image.name = request.created_by.user_id + '.' + profile_image.name.split('.')[-1]
            user.profile_image = profile_image
            user.save()
            return Response(True, status=status.HTTP_200_OK)
        else:
            return Response(False, status=status.HTTP_226_IM_USED)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class SearchUserView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    search_fields = ['username', 'name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SearchViewSerializer
    pagination_class = StandardResultsSetPagination


class Profile(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request):
        data = User.objects.get(user=request.created_by)
        data = self.serializer_class(instance=data).data
        return Response(data)


class ViewProfile(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request, **kwargs):
        try:
            data = User.objects.get(username=kwargs['username'])
            data = self.serializer_class(instance=data).data
            # cache.set(cache_key, data, 120)
        except ObjectDoesNotExist as e:
            data = {'reason': "user not exist", 'error': str(e)}

        return Response(data)
