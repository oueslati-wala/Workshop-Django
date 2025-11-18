from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from sessionApp.models import Session
from .serializers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.select_related('conference').all()
    serializer_class = SessionSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'topic', 'room']
    ordering_fields = ['session_day', 'start_time', 'end_time', 'title']

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.query_params
        conf_id = params.get('conference_id')
        if conf_id:
            qs = qs.filter(conference_id=conf_id)
        from_date = params.get('from_date')
        to_date = params.get('to_date')
        if from_date and to_date:
            qs = qs.filter(session_day__range=[from_date, to_date])
        room = params.get('room')
        if room:
            qs = qs.filter(room__icontains=room)
        return qs
