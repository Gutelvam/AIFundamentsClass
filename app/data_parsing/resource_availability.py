class ResourceAvailability:
    """
    Represents the availability of a specific resource.

    Attributes:
        resource_name (str): The name or identifier of the resource.
        quantity (int): The total available quantity of the resource.
    """
    
    def __init__(self, resource_name, quantity):
        self.resource_name = resource_name
        self.quantity = quantity
