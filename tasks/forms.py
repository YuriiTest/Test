from django.forms import ModelForm, ValidationError
from tasks.models import Information, ImageUpload
from tasks.widgets import DatePickerWidget


class InformationForm(ModelForm):
    """Information model form"""
    class Meta:
        model = Information
        fields = '__all__'
        widgets = {
            'birth_date': DatePickerWidget(
                params="dateFormat: 'yy-mm-dd', changeYear: true, changeMonth: true",
                attrs={'class': 'datepicker'})
        }


class ImageUploadForm(ModelForm):
    """ImageUpload model form"""
    class Meta:
        model = ImageUpload
        fields = '__all__'

    def clean_photo(self):
        image = self.cleaned_data.get('photo', False)
        if image:
            if image._size > 5*1024*1024:
                raise ValidationError("Image file too large (maximum 5mb)")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")
