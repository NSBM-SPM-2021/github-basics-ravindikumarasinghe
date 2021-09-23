from django.test import TestCase, Client

# Create your tests here.

from .models import Post
class BlogTestCase(TestCase):
    def setUp(self):
        # Create posts.
        a1 = Post.objects.create(title="New", slug="a", intro="this", body="New York")
        a2 = Post.objects.create(title="Even", slug="b", intro="Hi", body="Reset")
        a3 = Post.objects.create(title="Set", slug="d", intro="Wook", body="Settings")
        a4 = Post.objects.create(title="View", slug="d", intro="Text", body="Aviation")

    def test_slug(self):
        slug =[]
        y = bool
        for x in Post.objects.all():
            if x.slug not in slug:
                slug.append(x.slug)
            else:
                print(f"Slug Error on {x.title} Post")
           

    def test_index(self):
        # Set up client to make requests
        c = Client()
        # Send get request to index page and store response
        response = c.get("/")
        # Make sure status code is 200
        self.assertEqual(response.status_code, 200)



