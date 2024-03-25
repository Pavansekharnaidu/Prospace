from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import User, Class, Assignment, Question

User = get_user_model()

class UserModelTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.assertTrue(isinstance(user, User))
        self.assertFalse(user.is_teacher)

    def test_teacher_creation(self):
        teacher = User.objects.create_user(username='teacheruser', password='teacherpassword', is_teacher=True)
        self.assertTrue(isinstance(teacher, User))
        self.assertTrue(teacher.is_teacher)

class ClassModelTestCase(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher', password='teacherpassword', is_teacher=True)

    def test_class_creation(self):
        class_obj = Class.objects.create(name='Math', description='Mathematics class', teacher=self.teacher)
        self.assertTrue(isinstance(class_obj, Class))
        self.assertEqual(class_obj.teacher, self.teacher)

class AssignmentModelTestCase(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher', password='teacherpassword', is_teacher=True)
        self.class_obj = Class.objects.create(name='Math', description='Mathematics class', teacher=self.teacher)

    def test_assignment_creation(self):
        assignment = Assignment.objects.create(title='Math Assignment', description='Math assignment description', due_date='2024-04-01', teacher=self.teacher)
        assignment.classes.add(self.class_obj)
        self.assertTrue(isinstance(assignment, Assignment))
        self.assertEqual(assignment.teacher, self.teacher)
        self.assertEqual(assignment.classes.first(), self.class_obj)

class QuestionModelTestCase(TestCase):
    def test_question_creation(self):
        question = Question.objects.create(question_text='What is 2 + 2?')
        self.assertTrue(isinstance(question, Question))
