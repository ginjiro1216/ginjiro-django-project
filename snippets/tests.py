from django.test import TestCase, Client, RequestFactory
from django.urls import resolve

from snippets.models import Snippet
from snippets.views import snippet_new, snippet_detail, snippet_edit, top

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get('/')
        self.assertContains(response, 'Djangoスニペット', 200)

    def test_top_returns_expected_content(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "snippets/top.html")


class CreateSnippetTest(TestCase):
    def test_should_resolve_snippets_new(self):
        found = resolve('/snippets/new/')
        self.assertEqual(snippet_new, found.func)


class SnippetDetailTest(TestCase):
    def test_should_resolve_snippets_detail(self):
        found = resolve('/snippets/1/')
        self.assertEqual(snippet_detail, found.func)


class EditSnippetTest(TestCase):
    def test_should_resolve_snippets_edit(self):
        found = resolve('/snippets/1/edit/')
        self.assertEqual(snippet_edit, found.func)


class TopPageRenderSnippetsTest(TestCase):
    def setup(self):
        self.user = UserModel.objects.crate(
            username='test_user',
            email='test@example.com',
            password="top_secret_pass0001"
        )
        self.snippet = Snippet.objects.create(
            title='title1',
            code='print("hello")',
            description='description1',
            created_by=self.user,
        )

    def test_should_return_snippet_title(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippet.title)

    def test_should_return_username(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)
