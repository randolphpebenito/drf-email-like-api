from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
class FileUploadTests(TestCase):

    def _open_image_file(self):
        f = open('/home/randolph/Pictures/weed.jpg', 'rb')
        return f

    def _create_test_file(self, path):
        f = open(path, 'w')
        f.write('test123\n')
        f.close()
        f = open(path, 'rb')
        return {
            'doc': f,
        }

    def test_upload_file(self):
       url = reverse('task-list')
       data = self._create_test_file('/tmp/test_upload')
       data['task_name'] = 't1'
       data['task_desc'] = 'test'
       data['image'] = self._open_image_file()
       print data
       response = self.client.post(url, data, format='multipart')
       print response.status_code
       print response.content

      # # assert authenticated user can upload file
      # token = Token.objects.get(user__username='test')
      # client = APIClient()
      # client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
    
