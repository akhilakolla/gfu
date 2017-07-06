from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from giftsapp.models import Occassion, Gift_mapping, Gifts, Quest, Gender, Agegroup, Personality
from django.contrib.auth.decorators import login_required

qgender = 'h'
qage = 'h'
qpersonality = 'h'


@login_required
def output(request):
    return render(request, 'giftsapp/output.html')

def odiwali(request, pagename):
    if pagename == '1':
        id_o = Occassion.objects.get(occassion_type = "diwali")
        id_map = Gift_mapping.objects.get(focassid = id_o.id)
        id_gifts = Gifts.objects.get(id = id_map.id)
    return render(request, 'giftsapp/diwali.html', {'prop' : id_gifts})
    #return HttpResponse(rendered)

def anniversary(request, pagename):
    if pagename == '2':
        id_o = Occassion.objects.get(occassion_type = "Anniversary")
        id_map = Gift_mapping.objects.get(focassid = id_o.id)
        id_gifts = Gifts.objects.get(id = id_map.id)
    rendered = render(request, 'giftsapp/anniversary1.html', {'prop' : id_gifts})
    return HttpResponse(rendered)

def quest(request, pagename):
   if pagename == '3':
       return render(request, 'giftsapp/quest_main.html')

def quest1(request, pagename, par):
   global qgender
   if pagename == '4':
       if par == '1':
           qgender = 'M'
       elif par == '2':
           qgender = 'F'
       elif par == '3':
           qgender = 'B'
       elif par == '4':
           qgender = 'G'
       return render(request, 'giftsapp/quest1.html')
       
def quest2(request, pagename, par):
   global qage
   if pagename == '5':
       if par == '1':
           qage = 20
       elif par == '2':
           qage = 40
       elif par == '3':
           qage = 80
       return render(request, 'giftsapp/quest2.html')

def teen_images(request, pagename, par1, par2):
   global qpersonality
   if pagename == '6':
       if par1 == '1':
           if par2 == '1':
               qpersonality = 'SPORTSMAN'
           elif par2 == '2':
               qpersonality = 'FITNESS GUY'
           elif par2 == '3':
               qpersonality = 'TRAVELLER'
           f = Quest(gender = qgender, age = qage, personality = qpersonality)
           f.save()
           gen = Gender.objects.get(gender = qgender)
           per = Personality.objects.get(personality = qpersonality)
           age = Agegroup.objects.get(start_age = qage)
           t = Gift_mapping.objects.get(fpersonality = per.id, fgender = gen.id, fage = age.id)
           det = Gifts.objects.filter(giftsid = t.fgiftsid)
       return render(request, 'giftsapp/quest4.html', {'prop' : det})
       

