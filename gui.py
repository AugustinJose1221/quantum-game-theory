import math
import pyxel
from enum import Enum
from functools import partial


class GameState(Enum):
    INTRO = 0
    PLAYER1 = 1
    PLAYER2 = 2
    PLAYER3 = 3
    PLAYER4 = 4
    CIRCUIT = 5
    RESULTS = 6


class GameTheoryApp:
    def __init__(self, width=160, height=120):

        self.game_state = GameState.PLAYER1

        self._width = width
        self._height = height
        self.state_1 = []
        self.state_2 = []
        self.state_3 = []
        self.state_4 = []
        
        self.all_states = [self.state_1, self.state_2, self.state_3, self.state_4]

        pyxel.init(160, 120, caption="Quantum Game Theory")

        pyxel.mouse(True)
        pyxel.image(0).load(0, 0,'blt.jpg')
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.game_state == GameState.INTRO:
            self.handle_intro_events()

        elif self.game_state == GameState.PLAYER1:
            self.handle_player1()
        elif self.game_state == GameState.PLAYER2:
            self.handle_player2()
        elif self.game_state == GameState.PLAYER3:
            self.handle_player3()
        elif self.game_state == GameState.PLAYER4:
            self.handle_player4()
        elif self.game_state == GameState.CIRCUIT:
            self.handle_circuit()
        elif self.game_state == GameState.RESULTS:
            self.handle_results()


    def draw(self):
        pyxel.cls(0)

        if self.game_state == GameState.INTRO:
            self.draw_introscreen()
        elif self.game_state == GameState.PLAYER1:
            self.draw_player1()
        elif self.game_state == GameState.PLAYER2:
            self.draw_player2()
        elif self.game_state == GameState.PLAYER3:
            self.draw_player3()
        elif self.game_state == GameState.PLAYER4:
            self.draw_player4()
        elif self.game_state == GameState.CIRCUIT:
            self.draw_circuit()
        elif self.game_state == GameState.RESULTS:
            self.draw_results()


    ### Pyxel screens ###
    def draw_introscreen(self):
        pyxel.cls(0)
        pyxel.text(40, 40, "Quantum Game Maker", pyxel.frame_count % 16)
        x = 40
        y = 60
        w = 70
        h = 20
        pyxel.rectb(x, y, w, h, 7)
        pyxel.text(47, 67, "Click to Start", 7)

    def draw_player1(self):
        pyxel.text(40, 45, "Gates - Player 1", pyxel.frame_count % 16)

        pyxel.rectb(110, 110, 30, 10, 7)
        pyxel.text(115, 112, "Next", 7)

        gates_list = ['W', 'I', 'X', 'Y', 'S', 'Z', 'H', 'T']

        width_nomargin = self._width / 5
        gates_len = len(gates_list)
        y = 65

        gate_labels = []
        if len(gates_list) > 5:
            gate_labels = gates_list[:5]

        spacing = (self._width - (2 * width_nomargin)) / len(gate_labels)
        x_starting_pos = []
        new = width_nomargin

        for i in range(len(gates_list)):
            if len(x_starting_pos) == 0:
                x_starting_pos.append(new)
            else:
                x_starting_pos.append(new+spacing)
                new += spacing

        for x_pos, gate in zip(x_starting_pos, gates_list[:5]):
            self.pyxel_button(gate, x_pos, y, 12, 12, 13)

        if len(gates_list) > 5:
            gates_len = 5
            gate_labels = gates_list[5:]
            y += 16
            spacing = (self._width - (2 * width_nomargin)) / gates_len
            x_starting_pos = []
            new = width_nomargin

            for i in range(len(gates_list)):
                if len(x_starting_pos) == 0:
                    x_starting_pos.append(new)
                else:
                    x_starting_pos.append(new+spacing)
                    new += spacing

            for x_pos, gate in zip(x_starting_pos, gate_labels):
                self.pyxel_button(gate, x_pos, y, 12, 12, 13)

        s = "Elapsed frame count is {}\n" "Current mouse position is ({},{})".format(
            pyxel.frame_count, pyxel.mouse_x, pyxel.mouse_y
        )
        pyxel.text(1, 1, s, 9)

        print(self.state_1)


    def draw_player2(self):
        pyxel.text(40, 45, "Gates - Player 2", pyxel.frame_count % 16)

        pyxel.rectb(110, 110, 30, 10, 7)
        pyxel.text(115, 112, "Next", 7)

        gates_list = ['W', 'I', 'X', 'Y', 'S', 'Z', 'H', 'T']

        width_nomargin = self._width / 5
        gates_len = len(gates_list)
        y = 65

        gate_labels = []
        if len(gates_list) > 5:
            gate_labels = gates_list[:5]

        spacing = (self._width - (2 * width_nomargin)) / len(gate_labels)
        x_starting_pos = []
        new = width_nomargin

        for i in range(len(gates_list)):
            if len(x_starting_pos) == 0:
                x_starting_pos.append(new)
            else:
                x_starting_pos.append(new+spacing)
                new += spacing

        for x_pos, gate in zip(x_starting_pos, gates_list[:5]):
            self.pyxel_button(gate, x_pos, y, 12, 12, 13)

        if len(gates_list) > 5:
            gates_len = 5
            gate_labels = gates_list[5:]
            y += 16
            spacing = (self._width - (2 * width_nomargin)) / gates_len
            x_starting_pos = []
            new = width_nomargin

            for i in range(len(gates_list)):
                if len(x_starting_pos) == 0:
                    x_starting_pos.append(new)
                else:
                    x_starting_pos.append(new+spacing)
                    new += spacing

            for x_pos, gate in zip(x_starting_pos, gate_labels):
                self.pyxel_button(gate, x_pos, y, 12, 12, 13)

        s = "Elapsed frame count is {}\n" "Current mouse position is ({},{})".format(
            pyxel.frame_count, pyxel.mouse_x, pyxel.mouse_y
        )
        pyxel.text(1, 1, s, 9)

    
    def draw_player3(self):
        pyxel.text(40, 45, "Gates - Player 3", pyxel.frame_count % 16)

        pyxel.rectb(110, 110, 30, 10, 7)
        pyxel.text(115, 112, "Next", 7)

        gates_list = ['W', 'I', 'X', 'Y', 'S', 'Z', 'H', 'T']

        width_nomargin = self._width / 5
        gates_len = len(gates_list)
        y = 65

        gate_labels = []
        if len(gates_list) > 5:
            gate_labels = gates_list[:5]

        spacing = (self._width - (2 * width_nomargin)) / len(gate_labels)
        x_starting_pos = []
        new = width_nomargin

        for i in range(len(gates_list)):
            if len(x_starting_pos) == 0:
                x_starting_pos.append(new)
            else:
                x_starting_pos.append(new+spacing)
                new += spacing

        for x_pos, gate in zip(x_starting_pos, gates_list[:5]):
            self.pyxel_button(gate, x_pos, y, 12, 12, 13)

        if len(gates_list) > 5:
            gates_len = 5
            gate_labels = gates_list[5:]
            y += 16
            spacing = (self._width - (2 * width_nomargin)) / gates_len
            x_starting_pos = []
            new = width_nomargin

            for i in range(len(gates_list)):
                if len(x_starting_pos) == 0:
                    x_starting_pos.append(new)
                else:
                    x_starting_pos.append(new+spacing)
                    new += spacing

            for x_pos, gate in zip(x_starting_pos, gate_labels):
                self.pyxel_button(gate, x_pos, y, 12, 12, 13)

        s = "Elapsed frame count is {}\n" "Current mouse position is ({},{})".format(
            pyxel.frame_count, pyxel.mouse_x, pyxel.mouse_y
        )
        pyxel.text(1, 1, s, 9)

    
    def draw_player4(self):
        pyxel.text(40, 45, "Gates - Player 4", pyxel.frame_count % 16)

        pyxel.rectb(110, 110, 30, 10, 7)
        pyxel.text(115, 112, "Next", 7)

        gates_list = ['W', 'I', 'X', 'Y', 'S', 'Z', 'H', 'T']

        width_nomargin = self._width / 5
        gates_len = len(gates_list)
        y = 65

        gate_labels = []
        if len(gates_list) > 5:
            gate_labels = gates_list[:5]

        spacing = (self._width - (2 * width_nomargin)) / len(gate_labels)
        x_starting_pos = []
        new = width_nomargin

        for i in range(len(gates_list)):
            if len(x_starting_pos) == 0:
                x_starting_pos.append(new)
            else:
                x_starting_pos.append(new+spacing)
                new += spacing

        for x_pos, gate in zip(x_starting_pos, gates_list[:5]):
            self.pyxel_button(gate, x_pos, y, 12, 12, 13)

        if len(gates_list) > 5:
            gates_len = 5
            gate_labels = gates_list[5:]
            y += 16
            spacing = (self._width - (2 * width_nomargin)) / gates_len
            x_starting_pos = []
            new = width_nomargin

            for i in range(len(gates_list)):
                if len(x_starting_pos) == 0:
                    x_starting_pos.append(new)
                else:
                    x_starting_pos.append(new+spacing)
                    new += spacing

            for x_pos, gate in zip(x_starting_pos, gate_labels):
                self.pyxel_button(gate, x_pos, y, 12, 12, 13)

#         s = "Elapsed frame count is {}\n" "Current mouse position is ({},{})".format(
#             pyxel.frame_count, pyxel.mouse_x, pyxel.mouse_y
#         )
#         pyxel.text(1, 1, s, 9)

        # call quantum logic file, input self.all_states



################RUNQISKIT###############################

    def draw_circuit(self):
        pyxel.rectb(110, 110, 30, 10, 7)
        pyxel.text(115, 112, "Next", 7)
        pyxel.blt(61, 66, 0, 0, 0, 50, 50)


    def draw_results(self):
        the_variable = ''.join(self.state_1)
        pyxel.text(67, 15, "Results", pyxel.frame_count % 16)
        pyxel.line(60,30,60,110,7)
        pyxel.text(20,40,"Player 1", 7)
        pyxel.text(80,40,the_variable, 7)
        pyxel.text(20,60,"Player 2", 7)
        pyxel.text(80,60,"Result 2", 7)
        pyxel.text(20,80,"Player 3", 7)
        pyxel.text(80,80,"Result 3", 7)
        pyxel.text(20,100,"Player 4", 7)
        pyxel.text(80,100,"Result 4", 7)


    ### Event handlers ###

    def handle_intro_events(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.game_state = GameState.PLAYER1  
    

    def handle_player1(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 32 and pyxel.mouse_x < 43 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print("w")
            self.state_1.append('w')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 51 and pyxel.mouse_x < 62 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('i')
            self.state_1.append('i')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 69 and pyxel.mouse_x < 81 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('x')
            self.state_1.append('x')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 89 and pyxel.mouse_x < 100 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('y')
            self.state_1.append('y')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 107 and pyxel.mouse_x < 119 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('s')
            self.state_1.append('s')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 32 and pyxel.mouse_x < 43 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('z')
            self.state_1.append('z')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 51 and pyxel.mouse_x < 61 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('h')
            self.state_1.append('h')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 70 and pyxel.mouse_x < 81 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('t')
            self.state_1.append('t')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 119 and pyxel.mouse_x < 139 and pyxel.mouse_y < 119 and pyxel.mouse_y > 110:
            self.game_state = GameState.PLAYER2

    def handle_player2(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 32 and pyxel.mouse_x < 43 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print("w")
            self.state_2.append('w')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 51 and pyxel.mouse_x < 62 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('i')
            self.state_2.append('i')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 69 and pyxel.mouse_x < 81 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('x')
            self.state_2.append('x')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 89 and pyxel.mouse_x < 100 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('y')
            self.state_2.append('y')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 107 and pyxel.mouse_x < 119 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('s')
            self.state_2.append('s')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 32 and pyxel.mouse_x < 43 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('z')
            self.state_2.append('z')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 51 and pyxel.mouse_x < 61 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('h')
            self.state_2.append('h')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 70 and pyxel.mouse_x < 81 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('t')
            self.state_2.append('t')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 119 and pyxel.mouse_x < 139 and pyxel.mouse_y < 119 and pyxel.mouse_y > 110:
            self.game_state = GameState.PLAYER3

    def handle_player3(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 32 and pyxel.mouse_x < 43 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print("w")
            self.state_3.append('w')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 51 and pyxel.mouse_x < 62 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('i')
            self.state_3.append('i')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 69 and pyxel.mouse_x < 81 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('x')
            self.state_3.append('x')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 89 and pyxel.mouse_x < 100 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('y')
            self.state_3.append('y')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 107 and pyxel.mouse_x < 119 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('s')
            self.state_3.append('s')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 32 and pyxel.mouse_x < 43 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('z')
            self.state_3.append('z')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 51 and pyxel.mouse_x < 61 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('h')
            self.state_3.append('h')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 70 and pyxel.mouse_x < 81 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('t')
            self.state_3.append('t')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 119 and pyxel.mouse_x < 139 and pyxel.mouse_y < 119 and pyxel.mouse_y > 110:
            self.game_state = GameState.PLAYER4
    
    def handle_player4(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 32 and pyxel.mouse_x < 43 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print("w")
            self.state_4.append('w')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 51 and pyxel.mouse_x < 62 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('i')
            self.state_4.append('i')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 69 and pyxel.mouse_x < 81 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('x')
            self.state_4.append('x')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 89 and pyxel.mouse_x < 100 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('y')
            self.state_4.append('y')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 107 and pyxel.mouse_x < 119 and pyxel.mouse_y < 76 and pyxel.mouse_y > 64:
            print('s')
            self.state_4.append('s')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 32 and pyxel.mouse_x < 43 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('z')
            self.state_4.append('z')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 51 and pyxel.mouse_x < 61 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('h')
            self.state_4.append('h')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 70 and pyxel.mouse_x < 81 and pyxel.mouse_y < 91 and pyxel.mouse_y > 81:
            print('t')
            self.state_4.append('t')
        elif pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 119 and pyxel.mouse_x < 139 and pyxel.mouse_y < 119 and pyxel.mouse_y > 110:
            self.game_state = GameState.RESULTS

    def handle_circuit(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 119 and pyxel.mouse_x < 139 and pyxel.mouse_y < 119 and pyxel.mouse_y > 110:
            self.game_state = GameState.RESULTS

    def handle_results(self):
        None

    ### Pyxel Function Wrappers ###

    def pyxel_button(self, text, x, y, width, height, colour):

        try:
            pyxel.rect(x, y, width, height, colour)
            pyxel.text(x + 4, y + 3, text, 0)
        except AttributeError as e:
            pass
        return (x, y, x + width, y + height)


    # def pyxel_button_centered(self, text, y):
    #     offset = math.ceil(len(text) * 4 / 2) + 3
    #     x = math.floor(self._width / 2) - offset
    #     return self.pyxel_button(text, x, y)


GameTheoryApp()
