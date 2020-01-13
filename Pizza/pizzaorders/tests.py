from django.test import TestCase



#TESETCASE on orders list
class orderIndexViewTests(TestCase):
    def test_no_orders(self):
        """
        If no Orders exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('pizzaorders:orders-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Orders are available.")
        self.assertQuerysetEqual(response.context['Orders_list'], [])
