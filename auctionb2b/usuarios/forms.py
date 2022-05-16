from django import forms 

class ImageUploadForm(forms.Form):
    n = [f'image_{i}'for i in range(8)]
    for i in range(len(n)):
        if i >= 3:
            n[i] = forms.ImageField(required=False)
        else:
            n[i] = forms.ImageField(required=True)

    
