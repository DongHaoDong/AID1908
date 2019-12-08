from django import forms


class MyRegForm(forms.Form):
    # 限定username必须大于等于6个字符
    username = forms.CharField(max_length=30, label='请输入用户名')
    password = forms.CharField(max_length=30, label='请输入密码',widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, label='请再次输入密码',widget=forms.PasswordInput)

    def clean_username(self):
        '''此方法限定username必须大院等于6个字符'''
        username = self.cleaned_data['username']
        if len(username) < 6:
            raise forms.ValidationError("用户名太短")
        return username
    def clean(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError("两次密码不一致")
        return self.cleaned_data
    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     if len(password) == 0:
    #         raise forms.ValidationError("密码不能为空")
    #     return password


