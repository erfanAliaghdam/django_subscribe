from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status, mixins, permissions, exceptions
from rest_framework.decorators import action
from .serializers import PlanSerializer, SubscribeSerializer
from rest_framework.response import Response
from plan.models import Plan, Subscribe

class PlanViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Plan.objects.all().filter(is_active = True)
    serializer_class = PlanSerializer

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def subscribe(self, request, pk):
        plan = self.get_object()
        if plan.is_active == True:
            user = request.user
            #! JUST FOR PLANS WITH 0 PRICE -> free trial :)
            if plan.price == 0:
                try:
                    sub, created = Subscribe.objects.get_or_create(plan=plan, user=user)
                    if not created:
                        return Response({'error': 'you have subscribed this plan.'}, status=status.HTTP_403_FORBIDDEN) 
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)
                return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
            else: 
                # TODO this section is for non free plans which will redirect to ....
                return Response({'error': 'This plan is not free, endpoint will be created later'})
        else: raise exceptions.ValidationError({'error': 'this plan is not active'})


    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        user = request.user
        try:
            sub = Subscribe.objects.filter(user=user).all()
            ser = SubscribeSerializer(sub, many=True)
        except Exception as e:
            return Response({'error': str(e)})
        return Response({'subscribes':ser.data}, status=status.HTTP_200_OK)
