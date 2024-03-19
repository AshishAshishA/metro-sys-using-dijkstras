from django import forms

station_choices = [
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
    ('d', 'd'),
    ('e', 'e'),
    ('f', 'f'),
]

class stationForm(forms.Form):
    src = forms.CharField(
        label='Select Source Station',
        widget=forms.Select(choices=station_choices)
    )

    dest = forms.CharField(
        label='Select Destination Station',
        widget=forms.Select(choices=station_choices)
    )