from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests


    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=20&API_KEY=73F23A1D-13D9-4140-A273-884F0FE593A3")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Erro..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Qualidade do ar está satisfatória, e a poluição do ar apresenta nenhum ou pouco risco"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Qualidade do ar está aceitavel, e a poluição do ar apresenta um risco para pessoas que são sensiveis a poluição do ar"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups": 
            category_description = "(101 - 150) Qualidade do ar está não esta satisfaroia pára pessoas com problemas pulmonares, idosos e crianças"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy": 
            category_description = "(151 - 200) Todas as pessoas sentiram efeitos na saude"
            category_color = "unhealthy"
        elif api[0]['Category']['Name']== "Very Unhealthy":
            category_description = "(201 - 300) Alerta de saude: todos podem sentir problemas mais graves de saude"
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous": 
            category_description = "(301 - 500) Extremamente perigoso. Toda a população vai ser afetada"
            category_color = "hazardous"
        

        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color':category_color})
    
    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=20&API_KEY=73F23A1D-13D9-4140-A273-884F0FE593A3")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Erro..."

    if api[0]['Category']['Name'] == "Good":
        category_description = "(0 - 50) Qualidade do ar está satisfatória, e a poluição do ar apresenta nenhum ou pouco risco"
        category_color = "good"
    elif api[0]['Category']['Name'] == "Moderate":
        category_description = "(51 - 100) Qualidade do ar está aceitavel, e a poluição do ar apresenta um risco para pessoas que são sensiveis a poluição do ar"
        category_color = "moderate"
    elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups": 
        category_description = "(101 - 150) Qualidade do ar está não esta satisfaroia pára pessoas com problemas pulmonares, idosos e crianças"
        category_color = "usg"
    elif api[0]['Category']['Name'] == "Unhealthy": 
        category_description = "(151 - 200) Todas as pessoas sentiram efeitos na saude"
        category_color = "unhealthy"
    elif api[0]['Category']['Name']== "Very Unhealthy":
        category_description = "(201 - 300) Alerta de saude: todos podem sentir problemas mais graves de saude"
        category_color = "veryunhealthy"
    elif api[0]['Category']['Name'] == "Hazardous": 
        category_description = "(301 - 500) Extremamente perigoso. Toda a população vai ser afetada"
        category_color = "hazardous"
    

    return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color':category_color})

  


def about(request):
    return render(request, 'about.html', {})

