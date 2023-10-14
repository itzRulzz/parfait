from django.shortcuts import render
from recipe_parser import link_parser

def home_page(request):
    if request.method == 'POST':
        users_query = request.POST.get('search_bar', '')
        parser_results = link_parser(users_query)
        return render(request, 'home.html', {'results': parser_results})
    
    return render(request, 'home.html')
