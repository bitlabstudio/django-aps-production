"""Tests for the models of the aps_production app."""
from django.test import TestCase

from . import factories


class ErrorTestCase(TestCase):
    """Tests for the ``Error`` model class."""
    longMessage = True

    def test_instantiation(self):
        error = factories.ErrorFactory()
        self.assertTrue(error.pk)


class ErrorBinTestCase(TestCase):
    """Tests for the ``ErrorBin`` model class."""
    longMessage = True

    def test_instantiation(self):
        errorBin = factories.ErrorBinFactory()
        self.assertTrue(errorBin.pk)


class OrderTestCase(TestCase):
    """Tests for the ``Order`` model class."""
    longMessage = True

    def test_instantiation(self):
        order = factories.OrderFactory()
        self.assertTrue(order.pk)


class OrderLineTestCase(TestCase):
    """Tests for the ``OrderLine`` model class."""
    longMessage = True

    def test_instantiation(self):
        orderLine = factories.OrderLineFactory()
        self.assertTrue(orderLine.pk)


class OrderRunTestCase(TestCase):
    """Tests for the ``OrderRun`` model class."""
    longMessage = True

    def test_instantiation(self):
        orderRun = factories.OrderRunFactory()
        self.assertTrue(orderRun.pk)


class ShipmentTestCase(TestCase):
    """Tests for the ``Shipment`` model class."""
    longMessage = True

    def test_instantiation(self):
        shipment = factories.ShipmentFactory()
        self.assertTrue(shipment.pk)
