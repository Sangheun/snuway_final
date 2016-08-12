from django import forms
from django.template.loader import render_to_string


class DaumMapWidget(forms.TextInput):
    def render(self, name, value, attrs):
        lat, lng = 37.4624015, 126.9520365

        if value:
            lat, lng = value.split(',')

        html=super().render(name, value, attrs)
        rendered = render_to_string('daum_map_widget.html', {
            'lat': lat,
            'lng': lng,
        })
        return html + rendered