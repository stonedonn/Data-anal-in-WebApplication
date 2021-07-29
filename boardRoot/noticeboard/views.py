from django.shortcuts import render, get_object_or_404
# Create your views here.
# 뷰는 웹(클라이언트) 요청을 받고, 전달받은 데이터들을 해당 어플리케이션의 로직으로 가공하여
# 그 결과를 템플릿에 보내준다. 데이터는 가공하는 처리를 해야한다 싶으면 뷰에서 함수를
# 작성하면 된다.

def intro(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글

    return render(request, 'noticeboard/intro.html')
    #사용자에게 두번째에 있는 html를 세번째에 있는 context를 가져와 rendering해줌

def main(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글

    return render(request, 'noticeboard/main.html')
    #사용자에게 두번째에 있는 html를 세번째에 있는 context를 가져와 rendering해줌


def corona(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글

    return render(request, 'noticeboard/corona.html')
    #사용자에게 두번째에 있는 html를 세번째에 있는 context를 가져와 rendering해줌

def correlation_tmp(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글

    return render(request, 'noticeboard/correlation_tmp.html')
    #사용자에게 두번째에 있는 html를 세번째에 있는 context를 가져와 rendering해줌
# Create your views here.
def tmp(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글

    return render(request, 'noticeboard/tmp.html')
    #사용자에게 두번째에 있는 html를 세번째에 있는 context를 가져와 rendering해줌
def pm10(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글

    return render(request, 'noticeboard/pm10.html')

def pm25(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글

    return render(request, 'noticeboard/pm25.html')

def correlation_dust10(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글

    return render(request, 'noticeboard/correlation_dust10.html')

def correlation_dust25(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글

    return render(request, 'noticeboard/correlation_dust25.html')

def dust10_yearly(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글

    return render(request, 'noticeboard/dust10_yearly.html')

def dust25_yearly(request):
    #장고의 ORM 투입!
    #writeDate로 sort해서 가져오기 최신글

    return render(request, 'noticeboard/dust25_yearly.html')


