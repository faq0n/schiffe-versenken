class Ship:
    """A class representing a ship in a battleship game."""
    
    def __init__(self, name, size, position=None):
        """
        Initialize a ship.
        
        Args:
            name (str): The name of the ship
            size (int): The size/length of the ship (number of cells it occupies)
            position (tuple): Optional initial position as (row, col)
        """
        self.name = name
        self.size = size
        self._position = position
        self.health = size  # Health equals the size of the ship
        self.hits = 0  # Track number of hits
    
    def get_position(self):
        """
        Get the current position of the ship.
        
        Returns:
            tuple: Position as (row, col) or None if not placed
        """
        return self._position
    
    def set_position(self, row, col):
        """
        Set the position of the ship.
        
        Args:
            row (int): The row coordinate
            col (int): The column coordinate
        """
        self._position = (row, col)
    
    def hit(self):
        """
        Register a hit on the ship.
        
        Returns:
            bool: True if ship is sunk, False otherwise
        """
        if self.health > 0:
            self.health -= 1
            self.hits += 1
            return self.is_sunk()
        return False
    
    def is_sunk(self):
        """
        Check if the ship is sunk.
        
        Returns:
            bool: True if ship is sunk (health <= 0), False otherwise
        """
        return self.health <= 0
    
    def get_health(self):
        """
        Get the current health of the ship.
        
        Returns:
            int: The remaining health points
        """
        return self.health
    
    def get_hit_count(self):
        """
        Get the number of hits this ship has taken.
        
        Returns:
            int: The number of hits
        """
        return self.hits
    
    def is_placed(self):
        """
        Check if the ship has been placed on the board.
        
        Returns:
            bool: True if position is set, False otherwise
        """
        return self._position is not None
    
    def __str__(self):
        """String representation of the ship."""
        status = "Sunk" if self.is_sunk() else f"Health: {self.health}/{self.size}"
        pos = f"Position: {self._position}" if self.is_placed() else "Not placed"
        return f"{self.name} ({self.size} cells) - {status} - {pos}"
    
    def __repr__(self):
        """Developer-friendly representation of the ship."""
        return f"Ship(name='{self.name}', size={self.size}, position={self._position}, health={self.health})"
