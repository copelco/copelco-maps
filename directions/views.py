from django.views import generic


class Directions(generic.TemplateView):
    template_name = 'directions/view.html'


directions = Directions.as_view()
