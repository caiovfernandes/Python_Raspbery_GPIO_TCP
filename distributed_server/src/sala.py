import json
from gpio import GPIOClass
from time import sleep

class Sala():
    def __init__(self, sala):
        self.sala = sala

        print(f"../assets/configuracao_sala_0{sala}.json")
        with open(f"../assets/configuracao_sala_0{sala}.json") as fp:
            self.json_sala = json.load(fp)

        self.host = self.json_sala["ip_servidor_central"]
        self.port = self.json_sala["porta_servidor_central"]

        self.lampada01 = {
            "gpio": 0,
            "gpio_object": None
        }
        self.lampada02 = {
            "gpio": 0,
            "gpio_object": None
        }
        self.projetor = {
            "gpio": 0,
            "gpio_object": None
        }
        self.ac = {
            "gpio": 0,
            "gpio_object": None
        }
        self.alarme = {
            "gpio": 0,
            "gpio_object": None
        }
        self.presenca = {
            "gpio": 0,
            "gpio_object": None
        }
        self.fumaca = {
            "gpio": 0,
            "gpio_object": None
        }
        self.janela = {
            "gpio": 0,
            "gpio_object": None
        }
        self.porta = {
            "gpio": 0,
            "gpio_object": None
        }
        self.contagem_in = {
            "gpio": 0,
            "gpio_object": None
        }
        self.contagem_out = {
            "gpio": 0,
            "gpio_object": None
        }
        self.temperatura_humidade = {
            "gpio": 0,
            "valor_temp": 0,
            "valor_humidade": 0,
            "gpio_object": None
        }

        for outputs in self.json_sala["outputs"]:
            self.lampada01["gpio"] = outputs["gpio"] if outputs["tag"] == "Lâmpada 01" else self.lampada01["gpio"]
            self.lampada02["gpio"] = outputs["gpio"] if outputs["tag"] == "Lâmpada 02" else self.lampada02["gpio"]
            self.projetor["gpio"] = outputs["gpio"] if outputs["tag"] == "Projetor Multimidia" else self.projetor["gpio"]
            self.ac["gpio"] = outputs["gpio"] if outputs["tag"] == "Ar-Condicionado (1º Andar)" else self.ac["gpio"]
            self.alarme["gpio"] = outputs["gpio"] if outputs["tag"] == "Sirene do Alarme" else self.alarme["gpio"]

        for inputs in self.json_sala["inputs"]:
            self.presenca["gpio"] = inputs["gpio"] if inputs["tag"] == "Sensor de Presença" else self.presenca["gpio"]
            self.fumaca["gpio"] = inputs["gpio"] if inputs["tag"] == "Sensor de Fumaça" else self.fumaca["gpio"]
            self.janela["gpio"] = inputs["gpio"] if inputs["tag"] == "Sensor de Janela" else self.janela["gpio"]
            self.porta["gpio"] = inputs["gpio"] if inputs["tag"] == "Sensor de Porta" else self.porta["gpio"]
            self.contagem_in["gpio"] = inputs["gpio"] if inputs["tag"] == "Sensor de Contagem de Pessoas Entrada" else self.contagem_in["gpio"]
            self.contagem_out["gpio"] = inputs["gpio"] if inputs["tag"] == "Sensor de Contagem de Pessoas Saída" else self.contagem_out["gpio"]
        for sensor in self.json_sala["sensor_temperatura"]:
            self.temperatura_humidade["gpio"] = sensor["gpio"] if sensor["tag"] == "Sensor de Temperatura e Umidade" else self.temperatura_humidade["gpio"]

        self.inicializa_objectos_gpio()

    def inicializa_objectos_gpio(self):
        for outputs in self.json_sala["outputs"]:
            self.lampada01["gpio_object"] = GPIOClass(self.lampada01["gpio"]) if outputs["tag"] == "Lâmpada 01" else self.lampada01["gpio_object"]
            self.lampada02["gpio_object"] = GPIOClass(self.lampada02["gpio"]) if outputs["tag"] == "Lâmpada 02" else self.lampada02["gpio_object"]
            self.projetor["gpio_object"] = GPIOClass(self.projetor["gpio"]) if outputs["tag"] == "Projetor Multimidia" else self.projetor["gpio_object"]
            self.ac["gpio_object"] = GPIOClass(self.ac["gpio"]) if outputs["tag"] == "Ar-Condicionado (1º Andar)" else self.ac["gpio_object"]
            self.alarme["gpio_object"] = GPIOClass(self.alarme["gpio"]) if outputs["tag"] == "Sirene do Alarme" else self.alarme["gpio_object"]

        for inputs in self.json_sala["inputs"]:
            self.presenca["gpio_object"] = GPIOClass(self.presenca["gpio"]) if inputs["tag"] == "Sensor de Presença" else self.presenca["gpio_object"]
            self.fumaca["gpio_object"] = GPIOClass(self.fumaca["gpio"]) if inputs["tag"] == "Sensor de Fumaça" else self.fumaca["gpio_object"]
            self.janela["gpio_object"] = GPIOClass(self.janela["gpio"]) if inputs["tag"] == "Sensor de Janela" else self.janela["gpio_object"]
            self.porta["gpio_object"] = GPIOClass(self.porta["gpio"]) if inputs["tag"] == "Sensor de Porta" else self.porta["gpio_object"]
            self.contagem_in["gpio_object"] = GPIOClass(self.contagem_in["gpio"]) if inputs["tag"] == "Sensor de Contagem de Pessoas Entrada" else self.contagem_in["gpio_object"]
            self.contagem_out["gpio_object"] = GPIOClass(self.contagem_out["gpio"]) if inputs["tag"] == "Sensor de Contagem de Pessoas Saída" else self.contagem_out["gpio_object"]

            
            for sensor in self.json_sala["sensor_temperatura"]:
                self.temperatura_humidade["gpio_object"] = GPIOClass(self.temperatura_humidade["gpio"]) if sensor["tag"] == "Sensor de Temperatura e Umidade" else self.temperatura_humidade["gpio_object"]


    def update_states(self):
        count = 0
        while(1):

            self.lampada01["gpio_object"].get_state()
            self.lampada02["gpio_object"].get_state()
            self.projetor["gpio_object"].get_state()
            self.ac["gpio_object"].get_state()
            self.alarme["gpio_object"].get_state()
            self.presenca["gpio_object"].get_state()
            self.fumaca["gpio_object"].get_state()
            self.janela["gpio_object"].get_state()
            self.porta["gpio_object"].get_state()
            self.contagem_in["gpio_object"].get_state()
            self.contagem_out["gpio_object"].get_state()


            self.temperatura_humidade["valor_humidade"], self.temperatura_humidade["valor_temp"] = self.temperatura_humidade["gpio_object"].get_temperatura_humidade(self.temperatura_humidade["gpio_object"].pino)


            self.lampada01["gpio_object"].set_state(self.lampada01["gpio_object"].status, self.lampada01["gpio_object"].pino)
            self.lampada02["gpio_object"].set_state(self.lampada02["gpio_object"].status, self.lampada02["gpio_object"].pino)
            self.projetor["gpio_object"].set_state(self.projetor["gpio_object"].status, self.projetor["gpio_object"].pino)
            self.ac["gpio_object"].set_state(self.ac["gpio_object"].status, self.ac["gpio_object"].pino)
            self.alarme["gpio_object"].set_state(self.alarme["gpio_object"].status, self.alarme["gpio_object"].pino)
            self.presenca["gpio_object"].set_state(self.presenca["gpio_object"].status, self.presenca["gpio_object"].pino)
            self.fumaca["gpio_object"].set_state(self.fumaca["gpio_object"].status, self.fumaca["gpio_object"].pino)
            self.janela["gpio_object"].set_state(self.janela["gpio_object"].status, self.janela["gpio_object"].pino)
            self.porta["gpio_object"].set_state(self.porta["gpio_object"].status, self.porta["gpio_object"].pino)
            self.contagem_in["gpio_object"].set_state(self.contagem_in["gpio_object"].status, self.contagem_in["gpio_object"].pino)
            self.contagem_out["gpio_object"].set_state(self.contagem_out["gpio_object"].status, self.contagem_out["gpio_object"].pino)
            # print(f"Contagem {count}")
            count+=1

            sleep(2)


        # self.lampada01["gpio_object"].get_state()
        # self.lampada02["gpio_object"].get_state()
        # self.projetor["gpio_object"].get_state()
        # self.ac["gpio_object"].get_state()
        # self.alarme["gpio_object"].get_state()
        # self.presenca["gpio_object"].get_state()
        # self.fumaca["gpio_object"].get_state()
        # self.janela["gpio_object"].get_state()
        # self.porta["gpio_object"].get_state()
        # self.contagem_in["gpio_object"].get_state()
        # self.contagem_out["gpio_object"].get_state()

            # self.print_states()


    def print_states(self):
        print("Lâmpada 01: ", str(self.lampada01["gpio_object"].status))
        print("Lâmpada 02: ", str(self.lampada02["gpio_object"].status))
        print("Projetor: ", str(self.projetor["gpio_object"].status))
        print("Ar-Condicionado: ", str(self.ac["gpio_object"].status))
        print("Alarme: ", str(self.alarme["gpio_object"].status))
        print("Presença: ", str(self.presenca["gpio_object"].status))
        print("Fumaça: ", str(self.fumaca["gpio_object"].status))
        print("Janela: ", str(self.janela["gpio_object"].status))
        print("Porta: ", str(self.porta["gpio_object"].status))
        print("Contagem Entrada: ", str(self.contagem_in["gpio_object"].status))
        print("Contagem Saída: ", str(self.contagem_out["gpio_object"].status))
        print("----------------")
        print("")


    def get_informacoes_sala(self):
        infos = {
            "lampada01": str(self.lampada01["gpio_object"].status),
            "lampada02": str(self.lampada02["gpio_object"].status),
            "projetor": str(self.projetor["gpio_object"].status),
            "ac": str(self.ac["gpio_object"].status),
            "alarme": str(self.alarme["gpio_object"].status),
            "presenca": str(self.presenca["gpio_object"].status),
            "fumaca": str(self.fumaca["gpio_object"].status),
            "janela": str(self.janela["gpio_object"].status),
            "porta": str(self.porta["gpio_object"].status),
            "contagem_in": str(self.contagem_in["gpio_object"].status),
            "contagem_out": str(self.contagem_out["gpio_object"].status),
            "Temperatura": str(self.temperatura_humidade["valor_temp"]),
            "Humidade": str(self.temperatura_humidade["valor_humidade"]),

        }
        return infos

    def set_attribute_value_by_name(self, attribute_name, value):
        self.lampada02["gpio_object"].status = eval(value) if attribute_name == "lampada02" else self.lampada02["gpio_object"].status
        self.lampada01["gpio_object"].status = eval(value) if attribute_name == "lampada01" else self.lampada01["gpio_object"].status
        self.projetor["gpio_object"].status = eval(value) if attribute_name == "projetor" else self.projetor["gpio_object"].status
        self.ac["gpio_object"].status = eval(value) if attribute_name == "ac" else self.ac["gpio_object"].status
        self.alarme["gpio_object"].status = eval(value) if attribute_name == "alarme" else self.alarme["gpio_object"].status
        self.presenca["gpio_object"].status = eval(value) if attribute_name == "presenca" else self.presenca["gpio_object"].status
        self.fumaca["gpio_object"].status = eval(value) if attribute_name == "fumaca" else self.fumaca["gpio_object"].status
        self.janela["gpio_object"].status = eval(value) if attribute_name == "janela" else self.janela["gpio_object"].status
        self.porta["gpio_object"].status = eval(value) if attribute_name == "porta" else self.porta["gpio_object"].status
        self.contagem_in["gpio_object"].status = eval(value) if attribute_name == "contagem_in" else self.contagem_in["gpio_object"].status
        self.contagem_out["gpio_object"].status = eval(value) if attribute_name == "contagem_out" else self.contagem_out["gpio_object"].status