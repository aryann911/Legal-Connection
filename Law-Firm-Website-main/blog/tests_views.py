from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from django.urls import reverse
from django.test.client import Client
from .forms import CommentForm


class TestBlogViews(TestCase):
    """
    A class for testing blog app views
    """
    def setUp(self):
        """
        Set Up function to create user, login user, post and comment
        """
        self.user = User.objects.create_user(
            username='Demi', email='demi@gmail.com',
            password='demidemi')
        self.user.save()
        self.client.login(username='Demi', password='demidemi')
        self.post = Post.objects.create(
            title='test',
            slug='test',
            author=self.user,
            status=1
        )
        self.post.save()
        self.comment = Comment.objects.create(
            post=self.post,
            name='Demi',
            body='Test comment body'
        )
        self.comment.save()

    def test_get_home(self):
        """
        test for open home page
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about_page(self):
        """
        test for open about page
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_open_post_detail(self):
        """
        test open post detail page
        """
        slug = self.post.slug
        self.post.likes.add(self.user)
        response = self.client.get(reverse('post_detail', args=[slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_post(self):
        """
        test post method for blog page
        """
        slug = self.post.slug
        self.post.likes.add(self.user)
        response = self.client.post(reverse('post_detail', args=[slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_can_comment(self):
        """
        test for comment functionality
        """
        slug = self.post.slug
        response = self.client.post(
            reverse('post_detail', args=[slug]), {
                'body': 'test comment'
            })
        self.assertEquals(response.status_code, 200)

    def test_can_like(self):
        """
        test for like functionality
        """
        slug = self.post.slug
        response = self.client.post(
            reverse('post_like', args=[slug]), {
            })
        self.assertEquals(response.status_code, 302)

    def test_can_unlike(self):
        """
        test for unlike
        """
        slug = self.post.slug
        self.post.likes.add(self.user)
        response = self.client.post(
            reverse('post_like', args=[slug]), {
            })
        self.assertEquals(response.status_code, 302)
