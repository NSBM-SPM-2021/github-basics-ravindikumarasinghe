from django.test import TestCase, Client

# Create your tests here.
from .models import Post,User

class Test_Blog(TestCase):

    def setUp(self):
        #create User
        a = User.objects.create_user(username='testuser', password='12345')
        #create Blog
        b1 = Post.objects.create(title =  "A",slug="A", author=a , content="ABCD", status=0)
        b2 = Post.objects.create(title =  "B",slug="B", author=a , content="Sri lanka", status=1)
        b3 = Post.objects.create(title =  "C",slug="C", author=a , content="Blog", status=1)

    def test_index(self):
        """ Test index page """
        # Set up client to make requests
        c = Client()
        # Send get request to index page and store response
        response = c.get("/")
        # Make sure status code is 200
        self.assertEqual(response.status_code, 200)

    def test_live_post(self):
        count = 0
        for x in Post.objects.all():
            if x.status == 1:
                count+=1
        
        self.assertTrue(count==2)


