class Human:
    def __init__(self,name):
        self.name = name
    def send(self,msg):
        self.chat.dialog.append([self.name,msg])

        print("")


class Robot:

    def __init__(self,name):
        self.name = name

    def send(self,msg):
        self.chat.dialog.append([self.name,msg])





class Chat:
    def __init__(self):
        self.dialog=arr = [[None]*2]
    def connect_human(self,human):
        self.human=human
        human.chat=self
    def connect_robot(self,robot):
        self.robot=robot
        robot.chat=self
    def show_human_dialog(self):
        for i in range(1,self.dialog.__len__()):
            print("(" + self.dialog[i][0] + ") said :" + self.dialog[i][1])
            # if self.dialog[i][0] == self.human.name:
            #     print("("+self.dialog[i][0] + ") said :" + self.dialog[i][1])
            # if self.dialog[i][0] == self.robot.name:
            #     print("("+self.dialog[i][0] + ") said :" + self.dialog[i][1])
    def convertTobinary(self,msg):
        final=""
        for j in range(len(msg)):
            if msg[j] == "a" or msg[j] == "A" or msg[j] == "e" or msg[j] == "E" or msg[j] == "i" or msg[j] == "I" or msg[j] == "o" or msg[j] == "O" or msg[j] == "u" or msg[j] == "U"  :
                final=final+"0"
            else:
                final=final+"1"
        return final
    def show_robot_dialog(self):
        for i in range(1,self.dialog.__len__()):
            print("(" + self.dialog[i][0] + ") said :" + self.convertTobinary(self.dialog[i][1]))


        # for i in range(1,self.dialog.__len__()):
        #     for j in range(self.dialog[i].__len__()):




class Main:
    def main():
        human=Human("karl")
        robot=Robot("r2d2")
        chat1=Chat()
        chat1.connect_human(human)
        chat1.connect_robot(robot)

        human.send("hi robot")
        robot.send("hi !!!")
        robot.send("why u wanna talk to me")

        human.send("i wanna see how much the robots can understand")
        human.send("can i ?")
        robot.send("hh u cant check that !")


        chat1.show_human_dialog()
        chat1.show_robot_dialog()



    if __name__ == '__main__': main()

# thisdict =	{
#   "year": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# arr = [[None]*2]
# arr.append([1,2])
# print(arr)