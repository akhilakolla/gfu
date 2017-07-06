class Quiz(Forms.form):
    gender = forms.CharField(max_length=2)
    age = forms.CharField(max_length=2)
    personality = forms.CharField(max_length=50)
