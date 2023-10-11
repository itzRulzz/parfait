from django.shortcuts import render, redirect

def home_page(request):
    if request.method == 'POST':
        users_query = request.POST.get('search_bar', '')
        return render(request, 'home.html', {'ten': [users_query for x in range(10)]})
    
    return render(request, 'home.html')
