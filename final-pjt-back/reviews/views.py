from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ReviewSerializer, UpdateReviewSerializer, ReviewListSerializer, CommentSerializer, UpdateCommentSerializer, nameReviewSerializer
from .models import Review,Comment
from accounts.models import User
from rest_framework import status

@api_view(['POST'])
def create(request):
    if request.user.is_authenticated:
        review = request.data
        pk = int(review.get("movie"))
        title = review.get("title")
        content = review.get("content")
        point = review.get("point")
        user = request.user.pk
        data = { "title":title, "movie":pk, "content":content, "point":point, "user":user }
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    return Response(status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','DELETE','PUT'])
def detail(request):
    if request.user.is_authenticated:
        if request.method =='GET':
            pk = request.GET.get('pk')
            review = get_object_or_404(Review,pk=pk)
            writer_user = get_object_or_404(User, username=review.user)
            writer_pk = writer_user.pk
            serializer = nameReviewSerializer(review)
            return Response(serializer.data)

        pk = request.data.get("pk")
        review = get_object_or_404(Review,pk=pk)
        writer_user = get_object_or_404(User, username=review.user)
        writer_pk = writer_user.pk    
        if writer_pk == request.user.pk :
            if request.method =='DELETE':
                review.delete()
                data = {
                    'delete': f'데이터 {pk}번이 삭제되었습니다'
                }
                return Response(data,status=status.HTTP_204_NO_CONTENT)
            elif request.method == 'PUT':
                data = {
                    "title": request.data.get("title"),
                    "content": request.data.get("content"),
                    "point": request.data.get("point"),
                }
                serializer = UpdateReviewSerializer(review, data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def like(request):
    if request.user.is_authenticated:
        review_pk = request.data.get("review")
        review = get_object_or_404(Review, pk=review_pk)
        yourname = review.user
        you = get_object_or_404(User, username=yourname)
        you_pk = you.pk
        me = request.user.pk
        if you_pk != me:
            if review.like_users.filter(pk=me).exists():
                review.point -= 1
                review.save()
                review.like_users.remove(me)
                you.rank_point -= 1
                you.save()
                return Response(status=status.HTTP_200_OK)
            else:
                review.point += 1
                review.save()
                you.rank_point += 1
                you.save()
                review.like_users.add(me)
                return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def index(request):
    reviews = Review.objects.order_by('-pk')
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def create_comment(request):
    # if request.user.is_authenticated:
    if request.method == 'GET':
        comment = request.GET
        review = comment.get("review")
        comments = Comment.objects.filter(review=review)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
        
    if request.method == 'POST':
        comment = request.data
        review = comment.get("review")
        user = request.user.pk
        content = comment.get("content")
        data = { "review":review, "user":user, "content":content}
        serializer = CommentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    # return Response(status.HTTP_401_UNAUTHORIZED)

@api_view(['DELETE','PUT'])
def comment_detail(request):
    if request.method == 'DELETE':
        pk = request.GET.get('pk')
    else:
        pk = request.data.get("pk")
    comment = get_object_or_404(Comment,pk=pk)
    writer_user = get_object_or_404(User, username=comment.user)
    writer_pk = writer_user.pk
    
    if request.user.pk == writer_pk:
        if request.method =='PUT':
            data = {
                "content": request.data.get("content")
            }
            serializer = UpdateCommentSerializer(comment,data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        elif request.method == 'DELETE':
            comment.delete()
            data = {
                'delete': f'댓글 {pk}번이 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
    return Response(status.HTTP_406_NOT_ACCEPTABLE)