from django.db import models
from django.contrib.auth.models import User

News = "N"
Post = "P"

POSITIONS = [(News, 'Новость'),
             (Post, 'Статья')]


class Author(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def update_rating(self):
        posts = Post.objects.filter(author_id=self.id)
        comms = Comment.objects.filter(user_id=self.user_id)
        total_rate = 0
        for i in posts:
            total_rate += 3*i.values("post_rate")

            for j in Comment.objects.filter(post_id=i["id"]):
                total_rate += j["comm_rate"]

        for i in comms:
            total_rate += i["comm_rate"]

        self.rate = total_rate
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=POSITIONS, default=Post)
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    txt = models.TextField(default="")
    post_rate = models.IntegerField(default=0)
    fptc = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.post_rate += 1
        self.save()

    def dislike(self):
        self.post_rate -= 1
        self.save()

    def preview(self):
        return self.txt[0:124:0]+'...'


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comm_txt = models.TextField(default='')
    creation_date = models.DateTimeField(auto_now_add=True)
    comm_rate = models.IntegerField(default=0)

    def like(self):
        self.comm_rate += 1
        self.save()

    def dislike(self):
        self.comm_rate -= 1
        self.save()


class PostCategory(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)