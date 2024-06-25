from django.test import SimpleTestCase # type: ignore

# Create your tests here.
class SimpleTests(SimpleTestCase):
   def test_home_page_status_code(self):
     response = self.client.get('/')
     self.assertEqual(response.status_code, 200)
                      
   def test_patients_page_status_code(self):
     response = self.client.get('/patients/')
     self.assertEqual(response.status_code, 200)

   def test_schedules_page_status_code(self):
     response = self.client.get('/schedules/')
     self.assertEqual(response.status_code, 200)
   
   def test_appointments_page_status_code(self):
     response = self.client.get('/appointments/')
     self.assertEqual(response.status_code, 200)  

   def test_users_page_status_code(self):
     response = self.client.get('/users/')
     self.assertEqual(response.status_code, 200)   