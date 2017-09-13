from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedIdentityField, 
    SerializerMethodField
    )

from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =[
            #'id',
            'title',
            #'slug',
            'content',
            'publish',
            'user',
        ]


post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
)

class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Post
        fields =[
            'url',
            'id',
            'title',
            'slug',
            'content',
            'publish',
            'user',
            'image',
        ]
    
    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    '''    url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
    )
    delete_url = HyperlinkedIdentityField(
        view_name='posts-api:delete',
        lookup_field='slug'
    )'''
    class Meta:
        model = Post
        fields =[
            'url',
            'user',
            'title',
            'slug',
            'content',
            'publish',
            #'delete_url',
        ]

    def get_user(self, obj):
        return str(obj.user.username)
