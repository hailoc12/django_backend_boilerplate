from requests import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response



# class FreeViberBotCallbackView(APIView): 
#     permission_classes = [AllowAny]

#     def post(self, request):
#         viber_bot = get_viber_bot_from_callback_request(request)
#         if viber_bot: 
#             free_viber_bot = FreeViberBot(
#                 viber_bot.bot_name, 
#                 viber_token=viber_bot.auth_token, 
#                 bot_model = viber_bot.bot_model
#             )

#             result = free_viber_bot.execute_request(request)
#         else:
#             print("Warning: can't detect where callback request come from")

#         return Response(200)

# free_viber_bot_callback_view = FreeViberBotCallbackView.as_view()

