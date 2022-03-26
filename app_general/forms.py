from dataclasses import fields
from django import forms
from app_foods.models import Food
from .models import Subscription


# Custom field class
class FoodMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title
        

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=60, required=True, label='ชื่อ-นามสกุล')
    email = forms.EmailField(max_length=60, required=True, label='อีเมล')
    food_set = FoodMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'), 
        required = True, 
        label = 'เมนูที่สนใจ',
        widget=forms.CheckboxSelectMultiple
    )    
    accepted = forms.BooleanField(required=True, label='ข้อความยาว ๆ ที่หลายคนเคยเจอ อาจไม่ต้องอ่านก็ได้ แค่ยอมรับและเข้าใจก็พอ')

class SubscriptionModelForm(forms.ModelForm):
    food_set = FoodMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'), 
        required = True, 
        label = 'เมนูที่สนใจ',
        widget=forms.CheckboxSelectMultiple
    ) 
    accepted = forms.BooleanField(required=True, label='ข้อความยาว ๆ ที่หลายคนเคยเจอ อาจไม่ต้องอ่านก็ได้ แค่ยอมรับและเข้าใจก็พอ')
    
    class Meta: 
        model = Subscription
        fields = ['name', 'email', 'food_set', 'accepted']
        labels = {
            'name': 'ชื่อ-นามสกุล',
            'email': 'อีเมล',
            'food_set': 'เมนูที่สนใจ'
        }