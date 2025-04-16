from .factory import CProductA, CProductB, CFabricA, CFabricB


def test_cproduct_a_operation():
    product = CProductA()
    assert product.operation() == "Result of Concrete Product A"


def test_cproduct_b_operation():
    product = CProductB()
    assert product.operation() == "Result of Concrete Product B"


def test_cfabric_a_factory_method():
    factory = CFabricA()
    product = factory.factory_method()
    assert isinstance(product, CProductA)


def test_cfabric_b_factory_method():
    factory = CFabricB()
    product = factory.factory_method()
    assert isinstance(product, CProductB)


def test_some_operation_cfabric_a():
    factory = CFabricA()
    result = factory.some_operation()
    assert result == "Creator: use Result of Concrete Product A"


def test_some_operation_cfabric_b():
    factory = CFabricB()
    result = factory.some_operation()
    assert result == "Creator: use Result of Concrete Product B"
