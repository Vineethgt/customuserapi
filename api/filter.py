import django_filters
from api.models import Profile, Education, Experience

class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields =['bio','city']

class EducationFilter(django_filters.FilterSet):
    start_year__gt = django_filters.DateFilter(field_name='start_date', lookup_expr='year__gte')
    end_year__lt = django_filters.DateFilter(field_name='end_date', lookup_expr='year__lte')
    end_year__lt = django_filters.DateRangeFilter

    class Meta:
        model = Education
        fields = {
            'university','degree',
        }

class ExperienceFilter(django_filters.FilterSet):
    class Meta:
        model = Experience
        fields = {
            'title', 'company',
        }