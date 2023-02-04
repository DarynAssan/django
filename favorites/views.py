from django.shortcuts import render, redirect
# from .models import Main


# Create your views here.
def favorites_list(request):
    context = ()
    return render(request, 'favorites/favorites-list.html', context=context)


def add_to_favorites(request, id):
    if request.method == 'Post':
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
        else:
            request.session['favorites'] = list(request.session['favorites'])

        item_exist = next((item for item in request.session['favorites'] if item["type"] == request.Post.get('type') and item["id"] == id), False)

        add_data ={
            'type': request.Post.get('type'),
            'id': id,
        }

        if not item_exist:
            request.session['favorites'].append(add_data)
            request.session.modified = True
    return redirect(request.Post.get('url_from'))


def remove_from_favorites(request, id, item=None):
    if item in request.method == 'Post':

        for item in request.session['favorites']:
            if item['id'] == id and item['type'] == request.Post.get('type'):
                item.clear()

        while {} in request.session['favorites']:
            request.session['favorites'].remove({})

        if not request.session['favorites']:
            del request.session['favorites']

        request.session.modified =True
    return redirect(request.Post.get('url_from'))


def delete_favorites(request):
    if request.session.get('favorites'):
        del request.session['favorites']

    return redirect(request.Post.get('url_from'))

'''
def blog_list(request):
    contex = {
        "blog_posts": Main.objects.all()[:4],
        "favorites_list": request.session.get('favorites'),
    }
    return render(request, 'favorites/blog-list.html', context=contex)


def blog_details(request, id):
    context = {
        "blog_post": Main.objects.get(pk=id)
    }
    return render(request, 'favorites/blog-details.html', context=context)
'''