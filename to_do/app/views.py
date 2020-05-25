from django.shortcuts import render
from .models import Article, Comment

# Create your views here.

def index_defined_in_view (request):
    index_due = Article.objects.all().order_by("due_date")
    return render (request, 'index.html', {'id': index_due})

    # ★★ 아래 코드 써서, 그 콘텐트들별로 데드라인 순서대로 쓰려면? 

    # coding_order = Article.objects.filter(category="coding").order_by(★)
    # toefle_order = Article.objects.filter(category="toefle").order_by(★)
    # excel_order = Article.objects.filter(category="excel").order_by(★)
    # return render (request, index.html, {'co':coding_order, 'to':toefle_order, 'eo':excel_order})

def detail_defined_in_view(request, pk_i_clicked):
    article = Article.objects.get(pk=pk_i_clicked)
    return render (request, detail.html, {'a_article':article})

    # get(pk=)까지만 스스로 적음
    # 그 이후 위에 request 옆에 같이 pk 추가! 

def new_defined_in_view (request): 
    if request.method == 'POST'
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title']
            content = request.POST['content']
            due_date = request.POST['due_date']
        )

        return redirect('detali.html', pk_i_clicked=new_article.pk)
    else:
        return render(request, 'new.html')

    # if url == 'POST'
    #     print request () 까지 적은게 지금 안보고 할 수 있는 정도
    # 어디에 담기 = (모델명).objects.create(

    # )

    # ★ 특히 pk_i_clicked가 무슨 뜻인지. 
    # 새롭게 작성해준 글들의 pk...? 

    # edit, delete은 이곳에 적는게 아니라 맨 마지막에 따로 작성해준다

    # ★★질문★★
    # 1) new 함수가 2개라는게 무슨 의미인지 
    # ㅡ 그냥 : new.html에서 글 쓰도록 하는 것
    # ㅡ post : 쓴 글이 저장되도록 하는 것
    # 2) 저 위에 return과 redirect의 의미가 무엇인지

    # -> 다른 사람거 들어가서 '네트워크 들어가서 f12' 가서 직접 해보기 

    
def edit(request, pk_i_clicked):
    edit_article = Article.objects.get(pk=pk_i_clicked)
    if request.method == "POST":
        Article.objects.filter(pk=pk_i_clicked).update(
            title = request.POST['title'],
            content = request.POST['content'],
            due = request.POST['due']
        )
        return redirect ('detail.html', pk_i_clicked)
    return render(request, 'edit.html', {'edit_article' : edit_article})

# 교안 보고 수식대로 썼으나.....
# 1) 여기서는 왜 return이 2번인지. 
# 2) return 위치 다른건 어떤 의미? 


def delete(request, pk_i_clicked):
    delete_article = Article.objects.get(pk=pk_i_clicked)
    delete_article.delete()
    return redirect('index_i_will_use_in_html')

    # ㅡㅡㅡㅡㅡㅡㅡㅡ 이건 list 별 우선 순위 세우는 방법 알 때 ㅡㅡㅡㅡㅡㅡㅡ 

# def coding_in_view (request):
#     coding_list=Article.objects.filter(category='coding')
#     return render (request, 'coding.html', {'cl':coding_list})

# def toefle_in_view (request): 
#     toefle_list=Article.objects.filter(category='toefle')
#     return render (request, 'toefle.html', {'tl':toefle_list})

# def excel_in_view (request): 
#     excel_list=Article.objects.filter(category='excel')
#     return render (request, 'excel.html', {'el':excel_list})

def detail(request, pk_i_clicked):
    comment_article = Article.objects.get(pk=pk_i_clicked)
    if request.method == "POST":
        Comment.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect ('detail.html', pk_i_clicked)
    return render(request, 'edit.html', {'comment_article' : comment_article})

# 왜 이름을 detail로 받지? 
# 왜 위에서는 Article에서 pk 받더니, 아래는 Comment에서... ?

def delete_comment(request, article_pk, comment_pk)
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail.html', article_pk)