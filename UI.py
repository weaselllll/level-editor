import Vector
import pygame

class BaseUI:
    position = Vector.Vec2(0, 0)
    label = "NULL"
    text = None
    font_name = 'microsoftsansserif'
    font_size = 20
    
    hover_color = (0xfa, 0xfa, 0xfa, 0xff)
    base_color = (0xaa, 0xaa, 0xaa, 0xaa)

    def createSurface(self, size):
        self.surface = pygame.Surface(
            (size.x, size.y),
            pygame.SRCALPHA
            ).convert_alpha()
        self.surface.fill(
            self.base_color
        )

    def setPosition(self, position: Vector.Vec2):
        self.position = position

    def getPosition(self):
        return self.position
    
    def getLabel(self):
        return self.label
    
    def setLabel(self, label: str):
        self.label = label

    def getSurface(self):
        return self.surface

class UIButton(BaseUI):
    def __init__(
            self,
            label: str,
            position: Vector.Vec2,
            size: Vector.Vec2,
            callback_functions
        ):

        self.createSurface(size)

        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.label = label
        self.position = position

        self.text = self.font.render(
            label,
            False,
            pygame.Color(0x10, 0x10, 0x10)
        )
        self.__text_center = self.text.get_rect(
            center=(size / 2).get()
        )

        self.__is_hover = False
        self.__callback_functions = callback_functions

    def checkHover(self, mouse_position):
        if self.surface.get_rect(
            topleft=self.position.get()
        ).collidepoint(mouse_position):
            self.__is_hover = True
        else:
            self.__is_hover = False

    def isHovered(self):
        return self.__is_hover
    
    def update(self):
        if self.__is_hover:
            self.surface.fill(
                self.hover_color
            )
        else:
            self.surface.fill(
                self.base_color
            )
            
        self.surface.blit(
            self.text,
            self.__text_center
        )

    def click(self, button: bool):
        if button and self.__is_hover:
            self.surface.fill("white")
            return self.__callback_functions()

class UILabel(BaseUI):
    def __init__(
            self,
            label: str,
            position: Vector.Vec2,
            size: Vector.Vec2
        ):
        
        self.createSurface(size)
        
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.label = label
        self.position = position

        self.text = self.font.render(
            label,
            False,
            pygame.Color(0x10, 0x10, 0x10)
        )
        self.__text_center = self.text.get_rect(
            center=(size / 2).get()
        )

    def update(self):
        self.surface.blit(
            self.text,
            self.__text_center
        )

class UICheckBox(BaseUI):
    def __init__(
            self,
            label: str,
            position: Vector.Vec2,
            size: Vector.Vec2,
            key,
            value: bool
        ):

        self.createSurface(size)

        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.label = label
        self.position = position
        self.surface.fill((0xaa, 0xaa, 0xaa, 50))
        self.text = self.font.render(
            label,
            False,
            pygame.Color(0x10, 0x10, 0x10)
        )
        self.__text_center = self.text.get_rect(
            center=(size / 2).get()
        )

        self.__mark = pygame.Surface(
            (5, size.y)
        )
        
        self.__key = key

        if value:
            self.__mark.fill(
                pygame.Color(0x10, 0xfa, 0x10)
            )
        else:
            self.__mark.fill(
                pygame.Color(0xfa, 0xfa, 0xfa)
            )
        self.surface.blit(
            self.__mark,
            (0, 0)
        )
        self.__is_hover = False
        self.__value = value

    def checkHover(self, mouse_position):
        if self.surface.get_rect(
            topleft=self.position.get()
        ).collidepoint(mouse_position):
            self.__is_hover = True
        else:
            self.__is_hover = False

    def isHovered(self):
        return self.__is_hover
    
    def update(self):
        if self.__is_hover:
            self.surface.fill(
                self.hover_color
            )
        else:
            self.surface.fill(
                self.base_color
            )

        self.surface.blit(
            self.text,
            self.__text_center
        )
            
        if self.__value:
            self.__mark.fill(
                pygame.Color(0x10, 0xfa, 0x10)
            )
        else:
            self.__mark.fill(
                pygame.Color(0xfa, 0xfa, 0xfa)
            )
        self.surface.blit(
            self.__mark,
            (0, 0)
        )

    def click(self, button: bool):
        if button and self.__is_hover:
            self.__value = not self.__value
        return self.__value
    
    def getKey(self):
        return self.__key
