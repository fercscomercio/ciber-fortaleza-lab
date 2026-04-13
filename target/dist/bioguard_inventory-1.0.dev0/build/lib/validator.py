def check_temp(t):
    """Certifica que la temperatura de almacenamiento sea óptima."""
    if t < 2 or t > 8:
        return False
    return True