from django.db import models

# Create your models here.


class UserInfo(models.Model):
    # 用户表
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    avatar = models.ImageField()
    create_time = models.DateTimeField(auto_now_add=True)

    fans = models.ManyToManyField(to='UserInfo', through='UserFans', through_fields=('user', 'follower'))


class UserFans(models.Model):
    # 互粉关系表
    user = models.ForeignKey(to='UserInfo', related_name='users')
    follower = models.ForeignKey(to='UserInfo', related_name='followers')

    class Meta:
        unique_together = [
            ('user', 'follower'),
        ]


class Blog(models.Model):
    # 博客信息表
    title = models.CharField(max_length=64)
    site = models.CharField(max_length=32, unique=True)
    theme = models.CharField(max_length=32)

    user = models.OneToOneField(to='UserInfo', related_name='blog')


class Article(models.Model):
    # 博客文章表
    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=255)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    blog = models.ForeignKey(to='Blog', related_name='articles')
    category = models.ForeignKey(to='Category', related_name='articles', null=True)

    type_choices = [
        (1, "Python"),
        (2, "Linux"),
        (3, "OpenStack"),
        (4, "GoLang"),
    ]

    article_type = models.IntegerField(choices=type_choices, default=None)

    tags = models.ManyToManyField(
        to="Tag",
        through='Article2Tag',
        through_fields=('article', 'tag'),
    )


class ArticleDetail(models.Model):
    # 文章详细表
    content = models.TextField()

    article = models.OneToOneField(to='Article', related_name='detail')


class Tag(models.Model):
    # 博客标签表
    title = models.CharField(max_length=32)
    blog = models.ForeignKey(to='Blog', related_name='tags')


class Article2Tag(models.Model):
    # 文章标签关系表
    article = models.ForeignKey(to="Article")
    tag = models.ForeignKey(to="Tag")

    class Meta:
        unique_together = [
            ('article', 'tag'),
        ]


class Category(models.Model):
    # 博主个人文章分类表
    title = models.CharField(max_length=32)

    blog = models.ForeignKey(to='Blog', related_name='categories')


class UpDown(models.Model):
    # 文章顶或踩
    up = models.BooleanField()

    article = models.ForeignKey(to='Article')
    user = models.ForeignKey(to='UserInfo')

    class Meta:
        unique_together = [
            ('article', 'user'),
        ]


class Comment(models.Model):
    # 评论表
    content = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)

    reply = models.ForeignKey(to='self', related_name='back', null=True)
    article = models.ForeignKey(to='Article', related_name='comments')
    user = models.ForeignKey(to='UserInfo', related_name='comments')
