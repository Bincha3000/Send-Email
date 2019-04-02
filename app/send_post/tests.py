from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post
from .forms import PostForm
from user.forms import UserRegisterForm


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(
            email='test@sneakers.com',
            password='Qwerty12',
            username='Vasya'
            )
        Post.objects.create(
            author=user,
            title='Testtitle',
            text='Testtext',
            status=True
            )

    def test_title_name_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_author_name_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_text_name_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_status_message(self):
        post = Post.objects.get(id=1)
        status = post._meta.get_field('status')
        self.assertTrue(status)

    def test_string_representation(self):
        post = Post(title="My post title")
        self.assertEqual(str(post), post.title)


class ViewsTests(TestCase):

    def test_home_page_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_register_page_view(self):
        response = self.client.get('/user/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/register.html')

    def test_login_view(self):
        response = self.client.get('/user/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')

    def test_send_post_page_view(self):
        response = self.client.get('/user/login/send_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'send_post/post.html')

    def test_success_view(self):
        response = self.client.get('/user/login/send_post/success/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'send_post/success.html')


class FormTest(TestCase):

    def test_form_post_valid(self):
        title = 'title title title'
        text = 'Text text text'
        form = PostForm(data={'title': title, 'text': text})
        self.assertTrue(form.is_valid())

    def test_form_registration(self):
        username = 'Petya'
        email = 'testmails@twix.com'
        password1 = 'Drugoiparol12'
        password2 = 'Drugoiparol12'
        form = UserRegisterForm(data={'username': username,
                                      'email': email,
                                      'password1': password1,
                                      'password2': password2
                                      })
        self.assertTrue(form.is_valid())
