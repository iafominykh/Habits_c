

from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тест привычек"""

    def setUp(self) -> None:
        """Создание тестовой привычки"""

        self.user = User.objects.create(
            email='test@test.com',
            password='test',
            is_superuser=True,
            is_staff=True,
            telegram_username="test",
        )

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place="home",
            time="10:00:00",
            action="test",
            is_pleasant=False,
            frequency=1,
            execution_time="00:02:00",
            is_publication=True
        )


    def test_1_create_habit(self):
        """ Тестирование создания привычки """

        data = {
            'user': self.user.pk,
            'place': "test",
            'time': "10:00",
            'action': "test2",
            'is_pleasant': False,
            'frequency': 1,
            'execution_time': "00:02:00",
            'is_publication': False
        }
        response = self.client.post('/habits/create/', data=data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_2_list_habit(self):
        """ Тестирование вывода списка привычек """

        Habit.objects.create(
            user=self.user,
            place="test3",
            time="10:00:00",
            action="test5",
            is_pleasant=True,
            frequency=1,
            execution_time="00:02:00",
        )

        response = self.client.get('/habits/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_3_list_public_habit(self):
        """ Тестирование вывода списка привычек c флагом публикации """

        response = self.client.get('/habits/public/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_4_retrieve_habit(self):
        """Тестирование вывода одной привычки """

        response = self.client.get(f'/habits/detail/{self.habit.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_4_update_put_habit(self):
        """" Тестирование patch обновление привычки"""

        data = {
            'user': self.user.pk,
            'place': 'test',
            'time': '01:00:00',
            'action': 'test',
            'frequency': 1,
            'execution_time': "00:02:00"
        }

        response = self.client.patch(f'/habits/update/{self.habit.pk}/',
                                     data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["place"], 'test')

    def test_6_destroy_habit(self):
        """ Тестирование удаления привычки """

        response = self.client.delete(f'/habits/delete/{self.habit.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.all().exists())
        self.assertEqual(Habit.objects.all().count(), 0)