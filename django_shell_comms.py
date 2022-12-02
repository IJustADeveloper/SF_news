from news.models import Author, Post, Category, PostCategory, Comment
from django.contrib.auth.models import User

User.objects.create_user('Виталий Кузнецов')
User.objects.create_user('Анатолий Воробьев')

Author.objects.create(user_id_id=1)
Author.objects.create(user_id_id=2)

Category.objects.create(name='медицина')
Category.objects.create(name='программирование')
Category.objects.create(name='наука')
Category.objects.create(name='туториал')

Post.objects.create(author_id_id=1, type='P', title="Типы данных в SQL", txt='Типы данных бывают разные: зеленые, синие, красные. Здесь будет еще много несвязного текста оатпоатпотаоптаотпоатпотаоптаотпоатоптаотпоатпотаоптаоптаотптапоатпоатпотао')
Post.objects.create(author_id_id=1, type='P', title="Фреймворки на python", txt='Есть 2 стула: Flask и Django.')
Post.objects.create(author_id_id=2, type='N', title="Изобретение новой вакцины", txt='Новая вакцина была изобретена британскими учеными.')


PostCategory.objects.create(post_id_id=1, category_id_id=2)
PostCategory.objects.create(post_id_id=1, category_id_id=4)
PostCategory.objects.create(post_id_id=2, category_id_id=2)
PostCategory.objects.create(post_id_id=2, category_id_id=4)
PostCategory.objects.create(post_id_id=3, category_id_id=1)
PostCategory.objects.create(post_id_id=3, category_id_id=3)

Comment.objects.create(post_id_id=1, user_id_id=2, comm_txt="топ тутор!")
Comment.objects.create(post_id_id=1, user_id_id=1, comm_txt="спасибо")
Comment.objects.create(post_id_id=2, user_id_id=1, comm_txt="а я думал, что есть 2 табуретки")
Comment.objects.create(post_id_id=3, user_id_id=1, comm_txt="а че за вакцина то?")

Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).dislike()

Post.objects.get(id=2).like()
Post.objects.get(id=2).dislike()
Post.objects.get(id=2).dislike()

Post.objects.get(id=3).like()

Comment.objects.get(id=1).like()

Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).dislike()

Comment.objects.get(id=4).dislike()

Author.objects.get(id=1).update_rating()
Author.objects.get(id=2).update_rating()

print(User.objects.get(id=Author.objects.order_by('-rate')[:1][0].user_id_id).username,
      Author.objects.order_by('-rate')[:1][0].rate)

best_post = Post.objects.order_by("-post_rate")[:1][0]
print(best_post.creation_date, ' | ', User.objects.get(id=Author.objects.get(id=best_post.author_id_id).user_id_id).username, ' | ',
      best_post.post_rate, ' | ', best_post.title, ' | ', best_post.preview())

comms = Comment.objects.filter(post_id_id=best_post.id)
for i in comms:
    print(i.creation_date, ' | ', User.objects.get(id=i.user_id_id).username, ' | ', i.comm_rate, ' | ', i.comm_txt)
