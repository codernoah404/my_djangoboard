from django.shortcuts import render
from django.http import HttpResponse
from .models import Board, Comment
# Create your views here.
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import BoardForm, CommentForm

def index(request):
    req_li = {}
    for att in dir(request):
        req_li[att] = getattr(request, att)
    
    
    return render(request, 'board/index.html', {'name':'유저'})


def board_list(request):
    board_li = Board.objects.all()
    # coment_cnt = {}
    # for i in board_li:
    #     coment_cnt[i.id] = len(i.comment_set.all())

    # print(coment_cnt)

    return render(request, 'board/board_list.html', {'board':board_li})#, "comment":coment_cnt})

def board_detail(request,board_id):
    detail = Board.objects.prefetch_related('comment_set').get(id=board_id)
    comment = detail.comment_set.all()
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment(
                content=data['content'],
                board_id=board_id
            ).save()
            return redirect(reverse('board:detail', kwargs={'board_id':board_id}))

    resp = render(request, 'board/board_detail.html', {'detail':detail, "comment":comment, 'form':form})

    return resp
def comment_list(request):
    comment_li = Comment.objects.all()
    resp = ["<ul>"]
    for i in comment_li:
        resp.append(f"<li>{i.id}|{i.content}|{i.board}</li>")

    resp.append("</ul>")

    return HttpResponse(resp)

def create(request):
    form = BoardForm()
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('board:main',))
    
    return render(request, 'board/create.html', {'form':form})

def board_edit(request, board_id):
    board = Board.objects.get(id=board_id)
    form = BoardForm(initial={
        'title':board.title,
        'content':board.content,
    })
    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            board.title = form.cleaned_data['title']
            board.content = form.cleaned_data['content']
            board.save()
            return redirect(reverse('board:detail', kwargs={
                'board_id':board_id
            }))

    return render(request, 'board/edit.html', {'board_id':board_id, "form":form})

# def create(request):
#     if request.method == "POST":
#         data = request.POST
#         title, content = data['title'], data['content']
#         board = Board.objects.create(title=title, content=content)
#         return redirect(reverse('board:main',))
    
#     return render(request, 'board/create.html')