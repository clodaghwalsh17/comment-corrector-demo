# Example courtesy of https://realpython.com/documenting-python-code/
class Animal:
    """
    A class used to represent an Animal. And more stuff on line 

    Attributes
    ----------
    says_str: str
        a formatted string printing what the animal says
    name: str
        the name of the animal
    sound: str
        the sound the animal makes
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound):
        """
        Parameters:
        ----------
        name: str
            the name of the animal
        sound: str
            the sound the animal makes
        """
        self.name = name
        self.sound = sound

    def says(self, sound=None):
        if self.sound is None and sound is None:
            raise NotImplementedError("Silent Animals are not supported!")

        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))