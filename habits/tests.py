from django.test import TestCase
from users.models import User
from rest_framework.test import APIClient
from .models import Habits


class HabitsCRUDTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@test.com', password='testpassword132')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_habit(self):
        habit_data = {
            'user': self.user.id,
            'place': 'Home',
            'time': '12:00',
            'action': 'Exercise',
            'nicehab': True,
            'relhab': 'Read a book',
            'periodic': 1,
            'time_to_act': 30,
            'is_public': False
        }
        response = self.client.post('/api/habits/', habit_data)
        self.assertEqual(response.status_code, 201)

    def test_read_habit(self):
        habit = Habits.objects.create(user=self.user, place='Home', time_to_act=30, time='12:00', action='Exercise',
                                      is_public=True)
        response = self.client.get(f'/api/habits/{habit.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['place'], 'Home')

    def test_update_habit(self):
        habit = Habits.objects.create(user=self.user, place='Home', time_to_act=30, time='12:00', action='Exercise')
        habit_data = {'place': 'Gym'}
        response = self.client.patch(f'/api/habits/{habit.id}/', habit_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['place'], 'Gym')

    def test_delete_habit(self):
        habit = Habits.objects.create(user=self.user, place='Home', time_to_act=30, time='12:00', action='Exercise')
        response = self.client.delete(f'/api/habits/{habit.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Habits.objects.filter(id=habit.id).exists())
